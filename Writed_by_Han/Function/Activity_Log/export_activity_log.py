import pandas as pd
import json
from datetime import datetime
import dateutil



# SET ROLE
def get_role(user_name):
    cs_manager = ['han.pham.2']
    cs_support = [
        'ly.do.1',
        'trinhle14',
        'phuong.lam.6',
        'minh.nguyen.42',
        'tram.huynh.9'
    ]
    cs_checking = [
        'huong.van.1',
        'quang.nguyen.41',
        'trinh.nguyen.34',
        'ngoc.huynh.14',
        'an.nguyen.62',
        'tam.vo.8'
    ]
    if user_name in cs_manager:
        return 'CS Manager'
    elif user_name in cs_support:
        return 'CS Support'
    elif user_name in cs_checking:
        return 'CS Checking'
    else:
        return 'CS'


# Export "Activity log" to file Excel
def export_activity_log(req_obj):
    hits = req_obj.get('hits', [])
    try:
        data_sheet_1 = []
        action_export_data = [
            'export_logs_activity'
        ]
        data_sheet_2 = []
        action_on_system = [
            'log_in',
            'log_out',
            'search_customer',
            'view_customer_detail',
            'get_balance',
            'history_transactions'
        ]
        data_sheet_3 = []
        admin_check_log = [
            'export_statement',
            'download_econtract',
            'manual_reissue_card',
            'sms_card_url',
            'stop_card',
            'edit_info',
            'unblock_casa',
            'freeze_account',
            'freeze_list_account',
            'unfreeze_account',
            'close_account',
            'refresh_update_account'
        ]
        for item in hits:
            source = item.get('_source', {})

            user_name = source.get('username', '')
            user_role = get_role(user_name)
            action_name = source.get('type', '')
            date_request = source.get('datetime', '').split()[0] if source.get('datetime', '') else ''
            time_request = source.get('datetime', '').split()[1] if source.get('datetime', '') else ''
            data = source.get('data', {})
            from_date = data.get('fromDate', '')
            to_date = data.get('toDate', '')
            export_from_date = data.get('date_from', '')
            export_to_date = data.get('date_to', '')
            cif_id = source.get('cifId', '')
            field_edit = list(source.get('data', {}).keys()) if source.get('data', {}).keys() else ''
            field_edit_beauty = str(field_edit).replace('[', '').replace(']', '')
            old_data = source.get('oldData', {})
            old_data_beauty = str([*old_data.values()]).replace('[', '').replace(']', '')
            new_data_beauty = str([*data.values()]).replace('[', '').replace(']', '')

            # SHEET 1 : Export data
            if action_name in action_export_data:
                row_excel_1 = {
                    'User Role': user_role,
                    'User Name': user_name,
                    'Date Request': date_request,
                    'Time Request': time_request,
                    'Action Name': action_name,
                    'Export from Date': export_from_date,
                    'Export to Date': export_to_date
                }
                data_sheet_1.append(row_excel_1)

            # SHEET 2 : Action on System - NOT YET DATA
            elif action_name in action_on_system:
                row_excel_2 = {
                    'User Role': user_role,
                    'User Name': user_name,
                    'Log-in Date': '',
                    'Log-in Time': '',
                    'Log-out Date': '',
                    'Log-out Time': '',
                    'Action Name': action_name,
                    'CIFID': cif_id,
                    'Search field': '',
                    'Search value': ''
                }
                data_sheet_2.append(row_excel_2)

            # SHEET 3 : Admin check log
            elif action_name in admin_check_log:
                row_excel_3 = {
                    'User Role': user_role,
                    'User Name': user_name,
                    'Date Request': date_request,
                    'Time Request': time_request,
                    'Action Name': action_name,
                    'CIFID': cif_id,
                    'Field Edit': field_edit_beauty,
                    'Old Data': old_data_beauty,
                    'New Data': new_data_beauty,
                    'From Date': from_date or export_from_date,
                    'To Date': to_date or export_to_date
                }
                data_sheet_3.append(row_excel_3)

        # TO EXCEL FILE
        sheet_name_1 = 'Export data check log'
        df_sheet_1 = pd.DataFrame(data_sheet_1)
        if not df_sheet_1.empty:
            df_sheet_1 = df_sheet_1.sort_values(by=['User Name', 'Date Request', 'Time Request'], ascending=False)
            df_sheet_1.reset_index(drop=True, inplace=True)
            df_sheet_1.index += 1

        sheet_name_2 = 'Action on System'
        df_sheet_2 = pd.DataFrame(data_sheet_2)
        if not df_sheet_2.empty:
            df_sheet_2 = df_sheet_2.sort_values(by=['User Name'], ascending=False)
            df_sheet_2.reset_index(drop=True, inplace=True)
            df_sheet_2.index += 1

        sheet_name_3 = 'Admin check log'
        df_sheet_3 = pd.DataFrame(data_sheet_3)
        if not df_sheet_3.empty:
            df_sheet_3 = df_sheet_3.sort_values(by=['User Name', 'Date Request', 'Time Request'], ascending=False)
            df_sheet_3.reset_index(drop=True, inplace=True)
            df_sheet_3.index += 1
        zoneVN = dateutil.tz.gettz('Asia/Bangkok')
        now_dt = datetime.now(zoneVN)
        current_date = now_dt.strftime('%d-%m-%Y')
        file_name = 'Admin_check_log_' + current_date + '.xlsx'
        with pd.ExcelWriter(file_name) as writer:
            df_sheet_1.to_excel(writer, sheet_name=sheet_name_1, index=True, index_label='No.', header=True, freeze_panes=(1, 1))
            df_sheet_2.to_excel(writer, sheet_name=sheet_name_2, index=True, index_label='No.', header=True, freeze_panes=(1, 1))
            df_sheet_3.to_excel(writer, sheet_name=sheet_name_3, index=True, index_label='No.', header=True, freeze_panes=(1, 1))
    except Exception as e:
        print('FAIL TO EXPORT EXCEL FILE', e)


# RUN FROM HERE
file = open('response.json')
data = json.load(file)
data_in = data.get('hits', {})
export_activity_log(data_in)