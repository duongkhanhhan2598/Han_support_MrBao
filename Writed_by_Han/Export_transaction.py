import json
import pandas as pd
import boto3
import traceback

def mergeDictionary(dict_1, dict_2):
   dict_3 = {**dict_1, **dict_2}
   for key, value in dict_3.items():
       if key in dict_1 and key in dict_2:
               dict_3[key] = [value , dict_1[key]]
   return dict_3


def export_trans_to_csv():
    list_trans = [
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "813e5810-bf0b-400a-9480-71b91e498377",
            "_score": "",
            "_source": {
                "partnerId": "",
                "bankCode": "",
                "status": "completed",
                "createdAt": "2023-05-18 15:43:18",
                "source": "card_transaction",
                "tranId": "813e5810-bf0b-400a-9480-71b91e498377",
                "toAccount": "",
                "logs": {},
                "accountType": "",
                "extData": {
                    "transaction_id": "853318",
                    "reason": "",
                    "response_code": "0000",
                    "system_time": "1684406598",
                    "amount": 50000000,
                    "merchant_category_code": "6011",
                    "capture_mode": "EMV",
                    "merchant": "CONG TY TAI CHINH FE C HO CHI MINH   VNM",
                    "type": "deduct authorisation",
                    "reference": "000000036120",
                    "request_time": "1684424596",
                    "balance": 0,
                    "tracking_number": "232643300023569",
                    "transaction_time": "1684399396",
                    "campaign": "F6794A1A-155D-0357-103EB2FE1F5E3028",
                    "terminal_id": "A1102124"
                },
                "tranParticular": "",
                "amount": 500000,
                "fromAccount": "000000036120",
                "updated_timestamp": 1684424599
            },
            "sort": [
                1684424599
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "c04d8faa-db16-4c6d-a1fc-6bc901403608",
            "_score": "",
            "_source": {
                "partnerId": "napas",
                "bankCode": "",
                "finRefDate": "2023-05-18T00:00:00.000",
                "status": "completed",
                "createdAt": "2023-05-18 13:53:18",
                "source": "napas_cashin",
                "toAccount": "000005059728",
                "tranId": "c04d8faa-db16-4c6d-a1fc-6bc901403608",
                "logs": {
                    "init": [
                        {
                            "message": "{}",
                            "datetime": "2023-05-18 13:53:18"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{ \"meta\":{\"contexturl\":\"\",\"REQUESTUUID\":\"b14e8a5f-afb4-46f5-b50f-86d824a27093\",\"GLOBALUUID\":\"b9462596-143e-4c71-b95d-3009f4d5d4c4\"}, \"data\":{\"XferTrnAddRs\":{\"tranId\":\"YD0001667\",\"tranDate\":\"2023-05-18T00:00:00.000\"}}} ",
                            "datetime": "2023-05-18 13:54:54"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "finRefId": "YD0001667",
                "tranParticular": "Napas topup cashin",
                "amount": 100000,
                "fromAccount": "1600400100010101",
                "updated_timestamp": 1684418096
            },
            "sort": [
                1684418096
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "c08dd716-69e7-4041-9b0c-79a4c573b682",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "init",
                "createdAt": "2023-04-25 13:54:43",
                "source": "mop_transfer",
                "tranId": "c08dd716-69e7-4041-9b0c-79a4c573b682",
                "toAccount": "000000611381",
                "logs": {
                    "init": [
                        {
                            "message": "{\"tran_id\": \"c08dd716-69e7-4041-9b0c-79a4c573b682\", \"bank_code\": \"546035\", \"amount\": \"97800\", \"from_account_number\": \"\", \"account_number\": \"000000611381\", \"tran_particulars\": \"MYBIZ NM2A8MCZCS3I S93P6YGTMWNM\"}",
                            "datetime": "2023-04-25 13:54:43"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "tranParticular": "MYBIZ NM2A8MCZCS3I S93P6YGTMWNM",
                "amount": "97800",
                "fromAccount": "",
                "updated_timestamp": 1682430884
            },
            "sort": [
                1682430884
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "3d6a958e-9145-41dd-93a1-53794b5b6ab6",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "init",
                "createdAt": "2023-04-25 13:52:27",
                "source": "mop_transfer",
                "tranId": "3d6a958e-9145-41dd-93a1-53794b5b6ab6",
                "toAccount": "000000611381",
                "logs": {
                    "init": [
                        {
                            "message": "{\"tran_id\": \"3d6a958e-9145-41dd-93a1-53794b5b6ab6\", \"bank_code\": \"546035\", \"amount\": \"48900\", \"from_account_number\": \"\", \"account_number\": \"000000611381\", \"tran_particulars\": \"MYBIZ NM2A8MCZCS3I XE5Z2HLNBAUS\"}",
                            "datetime": "2023-04-25 13:52:27"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "tranParticular": "MYBIZ NM2A8MCZCS3I XE5Z2HLNBAUS",
                "amount": "48900",
                "fromAccount": "",
                "updated_timestamp": 1682430748
            },
            "sort": [
                1682430748
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "f4c58fb3-01ba-4521-9fd8-f67d98cc6497",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "init",
                "createdAt": "2023-04-25 11:48:19",
                "source": "mop_transfer",
                "tranId": "f4c58fb3-01ba-4521-9fd8-f67d98cc6497",
                "toAccount": "000000611381",
                "logs": {
                    "init": [
                        {
                            "message": "{\"tran_id\": \"f4c58fb3-01ba-4521-9fd8-f67d98cc6497\", \"bank_code\": \"546035\", \"amount\": \"48900\", \"from_account_number\": \"\", \"account_number\": \"000000611381\", \"tran_particulars\": \"MYBIZ NM2A8MCZCS3I 5QOS01ZYI2RV\"}",
                            "datetime": "2023-04-25 11:48:19"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "tranParticular": "MYBIZ NM2A8MCZCS3I 5QOS01ZYI2RV",
                "amount": "48900",
                "fromAccount": "",
                "updated_timestamp": 1682423300
            },
            "sort": [
                1682423300
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "bac39416-cd29-4b34-9fa3-aaba55464fbb",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "init",
                "createdAt": "2023-04-25 11:40:38",
                "source": "mop_transfer",
                "tranId": "bac39416-cd29-4b34-9fa3-aaba55464fbb",
                "toAccount": "000000086736",
                "logs": {
                    "init": [
                        {
                            "message": "{\"tran_id\": \"bac39416-cd29-4b34-9fa3-aaba55464fbb\", \"bank_code\": \"546035\", \"amount\": \"48900\", \"from_account_number\": \"\", \"account_number\": \"000000086736\", \"tran_particulars\": \"MYBIZ NM2A8MCZCS3I HRNSKBFTMIR7\"}",
                            "datetime": "2023-04-25 11:40:38"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "tranParticular": "MYBIZ NM2A8MCZCS3I HRNSKBFTMIR7",
                "amount": "48900",
                "fromAccount": "",
                "updated_timestamp": 1682422838
            },
            "sort": [
                1682422838
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "371b52fd-3366-4fb9-acad-c64b12246af8",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "init",
                "createdAt": "2023-04-25 11:40:10",
                "source": "mop_transfer",
                "tranId": "371b52fd-3366-4fb9-acad-c64b12246af8",
                "toAccount": "000000086736",
                "logs": {
                    "init": [
                        {
                            "message": "{\"tran_id\": \"371b52fd-3366-4fb9-acad-c64b12246af8\", \"bank_code\": \"546035\", \"amount\": \"48900\", \"from_account_number\": \"\", \"account_number\": \"000000086736\", \"tran_particulars\": \"MYBIZ NM2A8MCZCS3I 9SBJ5BCI01PD\"}",
                            "datetime": "2023-04-25 11:40:10"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "tranParticular": "MYBIZ NM2A8MCZCS3I 9SBJ5BCI01PD",
                "amount": "48900",
                "fromAccount": "",
                "updated_timestamp": 1682422812
            },
            "sort": [
                1682422812
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "1a822d3f-493e-4770-b793-d9b088bfe1ce",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "init",
                "createdAt": "2023-04-25 11:37:10",
                "source": "mop_transfer",
                "tranId": "1a822d3f-493e-4770-b793-d9b088bfe1ce",
                "toAccount": "000000086736",
                "logs": {
                    "init": [
                        {
                            "message": "{\"tran_id\": \"1a822d3f-493e-4770-b793-d9b088bfe1ce\", \"bank_code\": \"546035\", \"amount\": \"22400\", \"from_account_number\": \"\", \"account_number\": \"000000086736\", \"tran_particulars\": \"MYBIZ NM2A8MCZCS3I YEE1MNO91U1I\"}",
                            "datetime": "2023-04-25 11:37:10"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "tranParticular": "MYBIZ NM2A8MCZCS3I YEE1MNO91U1I",
                "amount": "22400",
                "fromAccount": "",
                "updated_timestamp": 1682422632
            },
            "sort": [
                1682422632
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "f20ebb86-309b-404b-a3ac-9bc4b6d880e9",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "init",
                "createdAt": "2023-04-25 11:05:05",
                "source": "mop_transfer",
                "tranId": "f20ebb86-309b-404b-a3ac-9bc4b6d880e9",
                "toAccount": "000000086736",
                "logs": {
                    "init": [
                        {
                            "message": "{\"tran_id\": \"f20ebb86-309b-404b-a3ac-9bc4b6d880e9\", \"bank_code\": \"546035\", \"amount\": \"97800\", \"from_account_number\": \"\", \"account_number\": \"000000086736\", \"tran_particulars\": \"MYBIZ NM2A8MCZCS3I XS1DF66OS2W1\"}",
                            "datetime": "2023-04-25 11:05:05"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "tranParticular": "MYBIZ NM2A8MCZCS3I XS1DF66OS2W1",
                "amount": "97800",
                "fromAccount": "",
                "updated_timestamp": 1682420706
            },
            "sort": [
                1682420706
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "786aad04-562e-4ac0-9365-a3353bd966ce",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "init",
                "createdAt": "2023-04-25 11:02:03",
                "source": "mop_transfer",
                "tranId": "786aad04-562e-4ac0-9365-a3353bd966ce",
                "toAccount": "000000086736",
                "logs": {
                    "init": [
                        {
                            "message": "{\"tran_id\": \"786aad04-562e-4ac0-9365-a3353bd966ce\", \"bank_code\": \"546035\", \"amount\": \"97800\", \"from_account_number\": \"\", \"account_number\": \"000000086736\", \"tran_particulars\": \"MYBIZ NM2A8MCZCS3I 7M8CK121SLCM\"}",
                            "datetime": "2023-04-25 11:02:03"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "tranParticular": "MYBIZ NM2A8MCZCS3I 7M8CK121SLCM",
                "amount": "97800",
                "fromAccount": "",
                "updated_timestamp": 1682420524
            },
            "sort": [
                1682420524
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "1e7420e3-a024-4987-96bc-39b5f4275db3",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "init",
                "createdAt": "2023-04-25 10:59:12",
                "source": "mop_transfer",
                "tranId": "1e7420e3-a024-4987-96bc-39b5f4275db3",
                "toAccount": "000000086736",
                "logs": {
                    "init": [
                        {
                            "message": "{\"tran_id\": \"1e7420e3-a024-4987-96bc-39b5f4275db3\", \"bank_code\": \"546035\", \"amount\": \"97800\", \"from_account_number\": \"\", \"account_number\": \"000000086736\", \"tran_particulars\": \"MYBIZ NM2A8MCZCS3I EUZ756XI8DKU\"}",
                            "datetime": "2023-04-25 10:59:12"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "tranParticular": "MYBIZ NM2A8MCZCS3I EUZ756XI8DKU",
                "amount": "97800",
                "fromAccount": "",
                "updated_timestamp": 1682420354
            },
            "sort": [
                1682420354
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "2c3b8b0d-5319-4541-ae48-246f72ae2b5f",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "init",
                "createdAt": "2023-04-25 10:47:28",
                "source": "mop_transfer",
                "tranId": "2c3b8b0d-5319-4541-ae48-246f72ae2b5f",
                "toAccount": "000000086736",
                "logs": {
                    "init": [
                        {
                            "message": "{\"tran_id\": \"2c3b8b0d-5319-4541-ae48-246f72ae2b5f\", \"bank_code\": \"546035\", \"amount\": \"34000\", \"from_account_number\": \"\", \"account_number\": \"000000086736\", \"tran_particulars\": \"MYBIZ NM2A8MCZCS3I UK9J8Y8ER2X9\"}",
                            "datetime": "2023-04-25 10:47:28"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "tranParticular": "MYBIZ NM2A8MCZCS3I UK9J8Y8ER2X9",
                "amount": "34000",
                "fromAccount": "",
                "updated_timestamp": 1682419650
            },
            "sort": [
                1682419650
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "91d6ad41-aacc-4985-86f2-a8b19ed86f55",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "init",
                "createdAt": "2023-04-25 10:42:43",
                "source": "mop_transfer",
                "tranId": "91d6ad41-aacc-4985-86f2-a8b19ed86f55",
                "toAccount": "000000086736",
                "logs": {
                    "init": [
                        {
                            "message": "{\"tran_id\": \"91d6ad41-aacc-4985-86f2-a8b19ed86f55\", \"bank_code\": \"546035\", \"amount\": \"33600\", \"from_account_number\": \"\", \"account_number\": \"000000086736\", \"tran_particulars\": \"MYBIZ NM2A8MCZCS3I LN7KL7JB6QGG\"}",
                            "datetime": "2023-04-25 10:42:43"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "tranParticular": "MYBIZ NM2A8MCZCS3I LN7KL7JB6QGG",
                "amount": "33600",
                "fromAccount": "",
                "updated_timestamp": 1682419365
            },
            "sort": [
                1682419365
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "f23e3d04-f93e-4e9d-b69b-104f2aa0555f",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2023-02-01T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-11-18 11:08:36",
                "source": "mop_transfer",
                "toAccount": "000000001591",
                "tranId": "f23e3d04-f93e-4e9d-b69b-104f2aa0555f",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"362-784-4652\", \"id\": \"5e4af344-e3ee-4f28-b204-b05751b7c91a\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-11-18 11:08:38"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-11-18 11:08:36"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"f23e3d04-f93e-4e9d-b69b-104f2aa0555f\", \"otp\": \"123456\"}",
                            "datetime": "2022-11-18 11:08:45"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000020\", \"tranDate\": \"2023-02-01T00:00:00.000\"}}",
                            "datetime": "2022-11-18 11:08:46"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "5e4af344-e3ee-4f28-b204-b05751b7c91a"
                },
                "finRefId": "YD0000020",
                "tranParticular": "Chao chao",
                "amount": "10000",
                "fromAccount": "000000002720",
                "updated_timestamp": 1668769727
            },
            "sort": [
                1668769727
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "7b2fb09e-2421-4e59-87c6-e3a825863046",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2023-02-01T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-11-18 11:01:56",
                "source": "mop_transfer",
                "toAccount": "000000001591",
                "tranId": "7b2fb09e-2421-4e59-87c6-e3a825863046",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"362-784-4652\", \"id\": \"079a4d80-36ec-4a6d-a0e9-7175b4454615\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-11-18 11:01:58"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-11-18 11:01:56"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"7b2fb09e-2421-4e59-87c6-e3a825863046\", \"otp\": \"123456\"}",
                            "datetime": "2022-11-18 11:02:07"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000019\", \"tranDate\": \"2023-02-01T00:00:00.000\"}}",
                            "datetime": "2022-11-18 11:02:08"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "079a4d80-36ec-4a6d-a0e9-7175b4454615"
                },
                "finRefId": "YD0000019",
                "tranParticular": "...",
                "amount": "10000",
                "fromAccount": "000000002720",
                "updated_timestamp": 1668769329
            },
            "sort": [
                1668769329
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "70fe919b-b4f0-4a7e-849c-8d4524e3e71c",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2023-02-01T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-11-18 10:54:20",
                "source": "mop_transfer",
                "toAccount": "000000001560",
                "tranId": "70fe919b-b4f0-4a7e-849c-8d4524e3e71c",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"362-784-4652\", \"id\": \"1445cf82-de77-4198-9c12-f0adf9537876\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-11-18 10:54:21"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-11-18 10:54:20"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"70fe919b-b4f0-4a7e-849c-8d4524e3e71c\", \"otp\": \"123456\"}",
                            "datetime": "2022-11-18 10:54:30"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000018\", \"tranDate\": \"2023-02-01T00:00:00.000\"}}",
                            "datetime": "2022-11-18 10:54:31"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "1445cf82-de77-4198-9c12-f0adf9537876"
                },
                "finRefId": "YD0000018",
                "tranParticular": "Cncncnc",
                "amount": "10000",
                "fromAccount": "000000002720",
                "updated_timestamp": 1668768872
            },
            "sort": [
                1668768872
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "d7fde101-d1bd-4db3-aa68-571660e22e21",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2023-02-01T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-11-18 10:03:29",
                "source": "mop_transfer",
                "toAccount": "000000001560",
                "tranId": "d7fde101-d1bd-4db3-aa68-571660e22e21",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"362-784-4652\", \"id\": \"958ede73-cbcc-4204-be47-7ce6aea3ae91\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-11-18 10:03:31"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-11-18 10:03:29"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"d7fde101-d1bd-4db3-aa68-571660e22e21\", \"otp\": \"123456\"}",
                            "datetime": "2022-11-18 10:03:38"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000014\", \"tranDate\": \"2023-02-01T00:00:00.000\"}}",
                            "datetime": "2022-11-18 10:03:39"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "958ede73-cbcc-4204-be47-7ce6aea3ae91"
                },
                "finRefId": "YD0000014",
                "tranParticular": "Cnfjfn",
                "amount": "10000",
                "fromAccount": "000000002720",
                "updated_timestamp": 1668765819
            },
            "sort": [
                1668765819
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "35115ce5-3281-4148-aa46-7b4ec350a9a6",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2023-02-01T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-11-18 08:59:56",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "35115ce5-3281-4148-aa46-7b4ec350a9a6",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"362-784-4652\", \"id\": \"04cb17a0-19af-4261-b529-3e6ca22e00cb\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-11-18 08:59:58"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-11-18 08:59:56"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"35115ce5-3281-4148-aa46-7b4ec350a9a6\", \"otp\": \"123456\"}",
                            "datetime": "2022-11-18 09:00:09"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000013\", \"tranDate\": \"2023-02-01T00:00:00.000\"}}",
                            "datetime": "2022-11-18 09:00:10"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "04cb17a0-19af-4261-b529-3e6ca22e00cb"
                },
                "finRefId": "YD0000013",
                "tranParticular": "Mvmvmv",
                "amount": "10000",
                "fromAccount": "000000002720",
                "updated_timestamp": 1668762011
            },
            "sort": [
                1668762011
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "b87465b0-163a-4795-b0a8-9980dd5f925e",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2023-01-03T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-11-14 23:08:13",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "b87465b0-163a-4795-b0a8-9980dd5f925e",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"3f4caed8-564d-4eb6-8a6a-a9a9da5bc8c5\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-11-14 23:08:15"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-11-14 23:08:13"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"b87465b0-163a-4795-b0a8-9980dd5f925e\", \"otp\": \"123456\"}",
                            "datetime": "2022-11-14 23:08:24"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000061\", \"tranDate\": \"2023-01-03T00:00:00.000\"}}",
                            "datetime": "2022-11-14 23:08:26"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "3f4caed8-564d-4eb6-8a6a-a9a9da5bc8c5"
                },
                "finRefId": "YD0000061",
                "tranParticular": "OD000001",
                "amount": "32000",
                "fromAccount": "000000002762",
                "updated_timestamp": 1668467307
            },
            "sort": [
                1668467307
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "8a89bd21-f7f9-4a07-b830-ec32f81d5d42",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2023-01-01T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-11-08 22:03:11",
                "source": "mop_transfer",
                "toAccount": "000000001491",
                "tranId": "8a89bd21-f7f9-4a07-b830-ec32f81d5d42",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"b272182a-dbd8-40ac-84df-64c47fb7e503\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-11-08 22:03:13"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-11-08 22:03:11"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"8a89bd21-f7f9-4a07-b830-ec32f81d5d42\", \"otp\": \"123456\"}",
                            "datetime": "2022-11-08 22:03:20"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000008\", \"tranDate\": \"2023-01-01T00:00:00.000\"}}",
                            "datetime": "2022-11-08 22:03:21"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "b272182a-dbd8-40ac-84df-64c47fb7e503"
                },
                "finRefId": "YD0000008",
                "tranParticular": "Test",
                "amount": "50000",
                "fromAccount": "000000002762",
                "updated_timestamp": 1667945002
            },
            "sort": [
                1667945002
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "1491ecdc-8708-4551-817a-11aecfa8d09e",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-31T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-11-08 11:05:46",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "1491ecdc-8708-4551-817a-11aecfa8d09e",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"1b367fd6-bcd1-4595-95eb-8ce3dfd04bbe\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-11-08 11:05:48"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-11-08 11:05:46"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"1491ecdc-8708-4551-817a-11aecfa8d09e\", \"otp\": \"123456\"}",
                            "datetime": "2022-11-08 11:05:56"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000440\", \"tranDate\": \"2022-12-31T00:00:00.000\"}}",
                            "datetime": "2022-11-08 11:05:57"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "1b367fd6-bcd1-4595-95eb-8ce3dfd04bbe"
                },
                "finRefId": "YD0000440",
                "tranParticular": "PO000063",
                "amount": "30000",
                "fromAccount": "000000002762",
                "updated_timestamp": 1667905558
            },
            "sort": [
                1667905558
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "17084048-b442-462e-b521-ee55e087cd30",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-31T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-11-04 21:16:26",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "17084048-b442-462e-b521-ee55e087cd30",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"52919a20-3e9b-43b9-90de-1fc70ce02963\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-11-04 21:16:28"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-11-04 21:16:26"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"17084048-b442-462e-b521-ee55e087cd30\", \"otp\": \"123456\"}",
                            "datetime": "2022-11-04 21:16:38"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000392\", \"tranDate\": \"2022-12-31T00:00:00.000\"}}",
                            "datetime": "2022-11-04 21:16:40"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "52919a20-3e9b-43b9-90de-1fc70ce02963"
                },
                "finRefId": "YD0000392",
                "tranParticular": "PO000048",
                "amount": "2000",
                "fromAccount": "000000002762",
                "updated_timestamp": 1667596601
            },
            "sort": [
                1667596601
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "db502203-c7c7-4e0a-bc85-0d9bd4bf3d0c",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-31T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-11-04 21:15:06",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "db502203-c7c7-4e0a-bc85-0d9bd4bf3d0c",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"7c3ebfc5-9a00-45c8-a6b3-da602c03805e\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-11-04 21:15:09"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-11-04 21:15:06"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"db502203-c7c7-4e0a-bc85-0d9bd4bf3d0c\", \"otp\": \"123456\"}",
                            "datetime": "2022-11-04 21:15:18"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000391\", \"tranDate\": \"2022-12-31T00:00:00.000\"}}",
                            "datetime": "2022-11-04 21:15:19"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "7c3ebfc5-9a00-45c8-a6b3-da602c03805e"
                },
                "finRefId": "YD0000391",
                "tranParticular": "PO000048",
                "amount": "300",
                "fromAccount": "000000002762",
                "updated_timestamp": 1667596520
            },
            "sort": [
                1667596520
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "6972cb75-6b5c-4074-95d8-b451fb53f59f",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-31T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-11-04 21:13:21",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "6972cb75-6b5c-4074-95d8-b451fb53f59f",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"26f84df1-512c-4377-b247-2e0dccf5ef52\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-11-04 21:13:23"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-11-04 21:13:21"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"6972cb75-6b5c-4074-95d8-b451fb53f59f\", \"otp\": \"123456\"}",
                            "datetime": "2022-11-04 21:13:30"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000390\", \"tranDate\": \"2022-12-31T00:00:00.000\"}}",
                            "datetime": "2022-11-04 21:13:32"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "26f84df1-512c-4377-b247-2e0dccf5ef52"
                },
                "finRefId": "YD0000390",
                "tranParticular": "PO000048",
                "amount": "3000",
                "fromAccount": "000000002762",
                "updated_timestamp": 1667596414
            },
            "sort": [
                1667596414
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "d900b263-4f5d-428b-9d55-1fcf692a9dd9",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "otp_gen",
                "createdAt": "2022-11-04 20:57:27",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "d900b263-4f5d-428b-9d55-1fcf692a9dd9",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"2976f07e-6f6f-4e7d-a128-91db40917a54\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-11-04 20:57:54"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-11-04 20:57:27"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "2976f07e-6f6f-4e7d-a128-91db40917a54"
                },
                "tranParticular": "PO000048",
                "amount": "200",
                "fromAccount": "000000002762",
                "updated_timestamp": 1667595475
            },
            "sort": [
                1667595475
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "2c35cf72-24cf-4508-a026-8d71dddf3793",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "otp_gen",
                "createdAt": "2022-11-04 20:56:44",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "2c35cf72-24cf-4508-a026-8d71dddf3793",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"c94982b7-f73b-4125-9505-e5e06a159841\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-11-04 20:57:10"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-11-04 20:56:44"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "c94982b7-f73b-4125-9505-e5e06a159841"
                },
                "tranParticular": "PO000048",
                "amount": "200",
                "fromAccount": "000000002762",
                "updated_timestamp": 1667595431
            },
            "sort": [
                1667595431
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "ae82cc4a-498f-463a-913f-5b962382259e",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "otp_gen",
                "createdAt": "2022-11-04 20:28:09",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "ae82cc4a-498f-463a-913f-5b962382259e",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"6a09fee0-d2e9-4900-8b58-eda8160af46b\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-11-04 20:28:37"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-11-04 20:28:09"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "6a09fee0-d2e9-4900-8b58-eda8160af46b"
                },
                "tranParticular": "PO000048",
                "amount": "10000",
                "fromAccount": "000000002762",
                "updated_timestamp": 1667593718
            },
            "sort": [
                1667593718
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "5a0fec2f-86df-4d3d-9a03-1237ad93debe",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "init",
                "createdAt": "2022-11-04 20:27:36",
                "source": "mop_transfer",
                "tranId": "5a0fec2f-86df-4d3d-9a03-1237ad93debe",
                "toAccount": "000000001496",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-11-04 20:27:36"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {},
                "tranParticular": "PO000048",
                "amount": "10000",
                "fromAccount": "000000002762",
                "updated_timestamp": 1667593657
            },
            "sort": [
                1667593657
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "dd2bd304-2ded-4283-b5d0-cc548e263179",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-31T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-11-04 18:11:29",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "dd2bd304-2ded-4283-b5d0-cc548e263179",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"85c4c53b-4f71-419a-9c17-32132b824ffd\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-11-04 18:11:31"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-11-04 18:11:29"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"dd2bd304-2ded-4283-b5d0-cc548e263179\", \"otp\": \"123456\"}",
                            "datetime": "2022-11-04 18:11:38"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000389\", \"tranDate\": \"2022-12-31T00:00:00.000\"}}",
                            "datetime": "2022-11-04 18:11:39"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "85c4c53b-4f71-419a-9c17-32132b824ffd"
                },
                "finRefId": "YD0000389",
                "tranParticular": "Test",
                "amount": "5000",
                "fromAccount": "000000002762",
                "updated_timestamp": 1667585500
            },
            "sort": [
                1667585500
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "b4982be4-5896-45b3-bed2-7a9a53927422",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-31T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-11-04 18:09:58",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "b4982be4-5896-45b3-bed2-7a9a53927422",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"362-784-4652\", \"id\": \"6c773d80-f25a-4946-af15-6d2459f6589a\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-11-04 18:10:00"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-11-04 18:09:58"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"b4982be4-5896-45b3-bed2-7a9a53927422\", \"otp\": \"123456\"}",
                            "datetime": "2022-11-04 18:10:07"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000388\", \"tranDate\": \"2022-12-31T00:00:00.000\"}}",
                            "datetime": "2022-11-04 18:10:08"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "6c773d80-f25a-4946-af15-6d2459f6589a"
                },
                "finRefId": "YD0000388",
                "tranParticular": "Mmmm",
                "amount": "1000",
                "fromAccount": "000000002720",
                "updated_timestamp": 1667585409
            },
            "sort": [
                1667585409
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "8f000f9e-7607-4cd6-ac4d-2e52cb5b8c92",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-31T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-11-04 17:26:10",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "8f000f9e-7607-4cd6-ac4d-2e52cb5b8c92",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"7f81ad51-9015-4f4e-a820-7dec4548a079\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-11-04 17:26:12"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-11-04 17:26:10"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"8f000f9e-7607-4cd6-ac4d-2e52cb5b8c92\", \"otp\": \"123456\"}",
                            "datetime": "2022-11-04 17:26:19"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000387\", \"tranDate\": \"2022-12-31T00:00:00.000\"}}",
                            "datetime": "2022-11-04 17:26:21"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "7f81ad51-9015-4f4e-a820-7dec4548a079"
                },
                "finRefId": "YD0000387",
                "tranParticular": "Test",
                "amount": "2000",
                "fromAccount": "000000002762",
                "updated_timestamp": 1667582782
            },
            "sort": [
                1667582782
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "e0aad3ca-b438-458b-a28b-c32978219353",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-31T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-11-04 17:22:12",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "e0aad3ca-b438-458b-a28b-c32978219353",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"2bba55b3-96d9-468f-84f1-59c18b1443f6\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-11-04 17:22:14"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-11-04 17:22:12"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"e0aad3ca-b438-458b-a28b-c32978219353\", \"otp\": \"123456\"}",
                            "datetime": "2022-11-04 17:22:20"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000386\", \"tranDate\": \"2022-12-31T00:00:00.000\"}}",
                            "datetime": "2022-11-04 17:22:21"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "2bba55b3-96d9-468f-84f1-59c18b1443f6"
                },
                "finRefId": "YD0000386",
                "tranParticular": "PO000040",
                "amount": "100",
                "fromAccount": "000000002762",
                "updated_timestamp": 1667582542
            },
            "sort": [
                1667582542
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "18ddaf5e-bbd8-4ed1-a843-8134e3359de0",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-31T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-11-04 17:12:41",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "18ddaf5e-bbd8-4ed1-a843-8134e3359de0",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"bfed2db1-17f6-4400-a0fc-3f80be873cc2\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-11-04 17:12:43"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-11-04 17:12:41"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"18ddaf5e-bbd8-4ed1-a843-8134e3359de0\", \"otp\": \"123456\"}",
                            "datetime": "2022-11-04 17:12:50"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000385\", \"tranDate\": \"2022-12-31T00:00:00.000\"}}",
                            "datetime": "2022-11-04 17:12:51"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "bfed2db1-17f6-4400-a0fc-3f80be873cc2"
                },
                "finRefId": "YD0000385",
                "tranParticular": "PO000040",
                "amount": "3000",
                "fromAccount": "000000002762",
                "updated_timestamp": 1667581972
            },
            "sort": [
                1667581972
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "1fca5774-f98c-4d9c-8508-e640d31201d6",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-31T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-11-04 17:10:45",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "1fca5774-f98c-4d9c-8508-e640d31201d6",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"9f82a857-b6cf-4d94-9212-626cbb00ea60\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-11-04 17:10:47"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-11-04 17:10:45"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"1fca5774-f98c-4d9c-8508-e640d31201d6\", \"otp\": \"123456\"}",
                            "datetime": "2022-11-04 17:11:05"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000384\", \"tranDate\": \"2022-12-31T00:00:00.000\"}}",
                            "datetime": "2022-11-04 17:11:06"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "9f82a857-b6cf-4d94-9212-626cbb00ea60"
                },
                "finRefId": "YD0000384",
                "tranParticular": "PO000040",
                "amount": "2000",
                "fromAccount": "000000002762",
                "updated_timestamp": 1667581868
            },
            "sort": [
                1667581868
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "6de1ac3f-218a-4d10-b154-c0688d0506ab",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-31T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-11-04 17:07:20",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "6de1ac3f-218a-4d10-b154-c0688d0506ab",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"2cf9618f-af00-42bb-b9a2-17d573fbc36a\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-11-04 17:07:22"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-11-04 17:07:20"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"6de1ac3f-218a-4d10-b154-c0688d0506ab\", \"otp\": \"123456\"}",
                            "datetime": "2022-11-04 17:07:35"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000383\", \"tranDate\": \"2022-12-31T00:00:00.000\"}}",
                            "datetime": "2022-11-04 17:07:36"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "2cf9618f-af00-42bb-b9a2-17d573fbc36a"
                },
                "finRefId": "YD0000383",
                "tranParticular": "PO000040",
                "amount": "1099",
                "fromAccount": "000000002762",
                "updated_timestamp": 1667581657
            },
            "sort": [
                1667581657
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "4cb8faa3-100a-4bb7-8189-153ba7c57078",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-31T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-11-04 17:04:07",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "4cb8faa3-100a-4bb7-8189-153ba7c57078",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"25faa510-7578-43dd-bbb6-800caf811bc0\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-11-04 17:04:10"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-11-04 17:04:07"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"4cb8faa3-100a-4bb7-8189-153ba7c57078\", \"otp\": \"123456\"}",
                            "datetime": "2022-11-04 17:04:19"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000382\", \"tranDate\": \"2022-12-31T00:00:00.000\"}}",
                            "datetime": "2022-11-04 17:04:20"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "25faa510-7578-43dd-bbb6-800caf811bc0"
                },
                "finRefId": "YD0000382",
                "tranParticular": "PO000040",
                "amount": "300",
                "fromAccount": "000000002762",
                "updated_timestamp": 1667581461
            },
            "sort": [
                1667581461
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "148f3582-282e-47b2-a699-9811449186fb",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-31T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-11-04 16:57:49",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "148f3582-282e-47b2-a699-9811449186fb",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"57c14d9c-38a5-4255-a7ba-1e3ad3a5b8e1\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-11-04 16:57:51"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-11-04 16:57:49"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"148f3582-282e-47b2-a699-9811449186fb\", \"otp\": \"123456\"}",
                            "datetime": "2022-11-04 16:57:59"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000381\", \"tranDate\": \"2022-12-31T00:00:00.000\"}}",
                            "datetime": "2022-11-04 16:58:00"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "57c14d9c-38a5-4255-a7ba-1e3ad3a5b8e1"
                },
                "finRefId": "YD0000381",
                "tranParticular": "PO000039",
                "amount": "2000",
                "fromAccount": "000000002762",
                "updated_timestamp": 1667581081
            },
            "sort": [
                1667581081
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "5cef935b-7227-4951-a4ab-599b0a1e09e0",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-31T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-11-04 16:54:49",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "5cef935b-7227-4951-a4ab-599b0a1e09e0",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"024ba8de-f733-4f65-9744-14d3b86dde44\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-11-04 16:54:51"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-11-04 16:54:49"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"5cef935b-7227-4951-a4ab-599b0a1e09e0\", \"otp\": \"123456\"}",
                            "datetime": "2022-11-04 16:54:59"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000380\", \"tranDate\": \"2022-12-31T00:00:00.000\"}}",
                            "datetime": "2022-11-04 16:55:00"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "024ba8de-f733-4f65-9744-14d3b86dde44"
                },
                "finRefId": "YD0000380",
                "tranParticular": "Test",
                "amount": "25000",
                "fromAccount": "000000002762",
                "updated_timestamp": 1667580901
            },
            "sort": [
                1667580901
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "da006e13-1efa-42f6-8b18-a3a392a712b0",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-31T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-11-03 15:56:11",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "da006e13-1efa-42f6-8b18-a3a392a712b0",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"ee560758-8b80-438c-91c7-5647b642e3d7\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-11-03 15:56:13"
                        },
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"51ba2aae-8271-4527-a38e-d91a8dd9d904\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-11-03 15:58:02"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-11-03 15:56:11"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"da006e13-1efa-42f6-8b18-a3a392a712b0\", \"otp\": \"123456\"}",
                            "datetime": "2022-11-03 15:58:08"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000361\", \"tranDate\": \"2022-12-31T00:00:00.000\"}}",
                            "datetime": "2022-11-03 15:58:09"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "51ba2aae-8271-4527-a38e-d91a8dd9d904"
                },
                "finRefId": "YD0000361",
                "tranParticular": "PO000013",
                "amount": "4000",
                "fromAccount": "000000002762",
                "updated_timestamp": 1667491090
            },
            "sort": [
                1667491090
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "1bcfe1f4-1c3c-4965-8c68-dd388a2d171c",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-31T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-11-02 16:20:05",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "1bcfe1f4-1c3c-4965-8c68-dd388a2d171c",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"93508201-ab9a-4f28-96ea-572a01dd80ec\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-11-02 16:20:10"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-11-02 16:20:05"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"1bcfe1f4-1c3c-4965-8c68-dd388a2d171c\", \"otp\": \"123456\"}",
                            "datetime": "2022-11-02 16:20:25"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000284\", \"tranDate\": \"2022-12-31T00:00:00.000\"}}",
                            "datetime": "2022-11-02 16:20:26"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "93508201-ab9a-4f28-96ea-572a01dd80ec"
                },
                "finRefId": "YD0000284",
                "tranParticular": "Test",
                "amount": "5000",
                "fromAccount": "000000002762",
                "updated_timestamp": 1667406027
            },
            "sort": [
                1667406027
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "ba3e3414-9f25-4b02-9e0d-c3a7eb4168de",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-31T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-11-02 16:17:28",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "ba3e3414-9f25-4b02-9e0d-c3a7eb4168de",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"2ba14035-f98e-4c02-b615-4ad07e8a9d8b\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-11-02 16:17:30"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-11-02 16:17:28"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"ba3e3414-9f25-4b02-9e0d-c3a7eb4168de\", \"otp\": \"123456\"}",
                            "datetime": "2022-11-02 16:17:39"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000283\", \"tranDate\": \"2022-12-31T00:00:00.000\"}}",
                            "datetime": "2022-11-02 16:17:40"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "2ba14035-f98e-4c02-b615-4ad07e8a9d8b"
                },
                "finRefId": "YD0000283",
                "tranParticular": "Test",
                "amount": "20000",
                "fromAccount": "000000002762",
                "updated_timestamp": 1667405861
            },
            "sort": [
                1667405861
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "3cf53a2e-59a4-48f3-ac0f-bc479b69264f",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-31T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-10-26 16:59:59",
                "source": "mop_transfer",
                "toAccount": "000000001497",
                "tranId": "3cf53a2e-59a4-48f3-ac0f-bc479b69264f",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"e28fded6-e259-4cb8-ae32-70ed88b452a6\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-10-26 17:00:01"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-10-26 16:59:59"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"3cf53a2e-59a4-48f3-ac0f-bc479b69264f\", \"otp\": \"123456\"}",
                            "datetime": "2022-10-26 17:00:09"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000031\", \"tranDate\": \"2022-12-31T00:00:00.000\"}}",
                            "datetime": "2022-10-26 17:00:10"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "e28fded6-e259-4cb8-ae32-70ed88b452a6"
                },
                "finRefId": "YD0000031",
                "tranParticular": "Bleble",
                "amount": "10000",
                "fromAccount": "000000002762",
                "updated_timestamp": 1666803612
            },
            "sort": [
                1666803612
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "425f3727-946d-4bd8-97dd-a455a011db4b",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-31T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-10-26 10:30:30",
                "source": "mop_transfer",
                "toAccount": "000000001497",
                "tranId": "425f3727-946d-4bd8-97dd-a455a011db4b",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"b33b8812-4143-4736-9214-b486287160c5\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-10-26 10:30:32"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-10-26 10:30:30"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"425f3727-946d-4bd8-97dd-a455a011db4b\", \"otp\": \"123456\"}",
                            "datetime": "2022-10-26 10:30:42"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000026\", \"tranDate\": \"2022-12-31T00:00:00.000\"}}",
                            "datetime": "2022-10-26 10:30:43"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "b33b8812-4143-4736-9214-b486287160c5"
                },
                "finRefId": "YD0000026",
                "tranParticular": "Mô tả nè",
                "amount": "10000",
                "fromAccount": "000000002762",
                "updated_timestamp": 1666780244
            },
            "sort": [
                1666780244
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "fc8784e9-07b7-499f-bcd8-4bd4471764c9",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-31T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-10-26 10:28:56",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "fc8784e9-07b7-499f-bcd8-4bd4471764c9",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"3ef05149-bb0c-40dc-9a30-0a9bee3fbade\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-10-26 10:28:58"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-10-26 10:28:56"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"fc8784e9-07b7-499f-bcd8-4bd4471764c9\", \"otp\": \"123456\"}",
                            "datetime": "2022-10-26 10:29:08"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000025\", \"tranDate\": \"2022-12-31T00:00:00.000\"}}",
                            "datetime": "2022-10-26 10:29:09"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "3ef05149-bb0c-40dc-9a30-0a9bee3fbade"
                },
                "finRefId": "YD0000025",
                "tranParticular": "Test",
                "amount": "25000",
                "fromAccount": "000000002762",
                "updated_timestamp": 1666780150
            },
            "sort": [
                1666780150
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "8cd76554-6ea9-47b7-9f83-ea92086222e1",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-31T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-10-26 10:09:05",
                "source": "mop_transfer",
                "toAccount": "000000001498",
                "tranId": "8cd76554-6ea9-47b7-9f83-ea92086222e1",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"38856f6f-1e53-4959-9268-489cd5b03582\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-10-26 10:09:10"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-10-26 10:09:05"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"8cd76554-6ea9-47b7-9f83-ea92086222e1\", \"otp\": \"123456\"}",
                            "datetime": "2022-10-26 10:09:21"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000024\", \"tranDate\": \"2022-12-31T00:00:00.000\"}}",
                            "datetime": "2022-10-26 10:09:22"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "38856f6f-1e53-4959-9268-489cd5b03582"
                },
                "finRefId": "YD0000024",
                "tranParticular": "Trả 12k",
                "amount": "12000",
                "fromAccount": "000000002762",
                "updated_timestamp": 1666778963
            },
            "sort": [
                1666778963
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "8b2d1914-44b5-4563-8a20-0e9ec56ec74f",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-31T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-10-26 10:07:00",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "8b2d1914-44b5-4563-8a20-0e9ec56ec74f",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"8b23c638-f7b1-417e-9533-064aa68cae20\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-10-26 10:07:02"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-10-26 10:07:00"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"8b2d1914-44b5-4563-8a20-0e9ec56ec74f\", \"otp\": \"123456\"}",
                            "datetime": "2022-10-26 10:07:10"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000023\", \"tranDate\": \"2022-12-31T00:00:00.000\"}}",
                            "datetime": "2022-10-26 10:07:10"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "8b23c638-f7b1-417e-9533-064aa68cae20"
                },
                "finRefId": "YD0000023",
                "tranParticular": "Mô tả nè",
                "amount": "50000",
                "fromAccount": "000000002762",
                "updated_timestamp": 1666778831
            },
            "sort": [
                1666778831
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "f65f1be4-e9c0-4934-937f-ac8d94a77e6a",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "init",
                "createdAt": "2022-10-25 10:35:38",
                "source": "mop_transfer",
                "tranId": "f65f1be4-e9c0-4934-937f-ac8d94a77e6a",
                "toAccount": "000000086736",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-10-25 10:35:38"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {},
                "tranParticular": "mybiz#775a3498-ba1c-4882-be3d-9629457896f7#6FDECV94BCVU",
                "amount": "2000",
                "fromAccount": "",
                "updated_timestamp": 1666694139
            },
            "sort": [
                1666694139
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "a4269ff0-307b-4428-b453-d9e5fc8918f2",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "init",
                "createdAt": "2022-10-25 10:30:11",
                "source": "mop_transfer",
                "tranId": "a4269ff0-307b-4428-b453-d9e5fc8918f2",
                "toAccount": "000000086736",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-10-25 10:30:11"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {},
                "tranParticular": "mybiz#775a3498-ba1c-4882-be3d-9629457896f7#ZYODXUL56YS2",
                "amount": "2000",
                "fromAccount": "",
                "updated_timestamp": 1666693812
            },
            "sort": [
                1666693812
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "a6056a26-b677-4895-b64f-6ef6de0f1b8a",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "init",
                "createdAt": "2022-10-25 10:29:33",
                "source": "mop_transfer",
                "tranId": "a6056a26-b677-4895-b64f-6ef6de0f1b8a",
                "toAccount": "000000086736",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-10-25 10:29:33"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {},
                "tranParticular": "mybiz#775a3498-ba1c-4882-be3d-9629457896f7#T9S88YA40RL3",
                "amount": "2000",
                "fromAccount": "",
                "updated_timestamp": 1666693774
            },
            "sort": [
                1666693774
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "1dec25ca-48fc-405d-908c-b8fcf3e3d142",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "init",
                "createdAt": "2022-10-25 10:29:31",
                "source": "mop_transfer",
                "tranId": "1dec25ca-48fc-405d-908c-b8fcf3e3d142",
                "toAccount": "000000086736",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-10-25 10:29:31"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {},
                "tranParticular": "mybiz#775a3498-ba1c-4882-be3d-9629457896f7#2OZB3V7PBX55",
                "amount": "2000",
                "fromAccount": "",
                "updated_timestamp": 1666693772
            },
            "sort": [
                1666693772
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "96feaa8c-0262-4ca0-beb5-9ca0270b3391",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "init",
                "createdAt": "2022-10-25 10:22:25",
                "source": "mop_transfer",
                "tranId": "96feaa8c-0262-4ca0-beb5-9ca0270b3391",
                "toAccount": "000000086736",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-10-25 10:22:25"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {},
                "tranParticular": "mybiz#775a3498-ba1c-4882-be3d-9629457896f7#JMNM1APTH5R1",
                "amount": "1000",
                "fromAccount": "",
                "updated_timestamp": 1666693346
            },
            "sort": [
                1666693346
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "3b5cf95a-785d-4aba-9554-6a4b67208eed",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "init",
                "createdAt": "2022-10-25 10:22:15",
                "source": "mop_transfer",
                "tranId": "3b5cf95a-785d-4aba-9554-6a4b67208eed",
                "toAccount": "000000086736",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-10-25 10:22:15"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {},
                "tranParticular": "mybiz#775a3498-ba1c-4882-be3d-9629457896f7#DJ53FHI81L52",
                "amount": "1000",
                "fromAccount": "",
                "updated_timestamp": 1666693336
            },
            "sort": [
                1666693336
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "a0745ddd-1007-4648-b3ea-2aa13604c50c",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "init",
                "createdAt": "2022-10-25 10:22:05",
                "source": "mop_transfer",
                "tranId": "a0745ddd-1007-4648-b3ea-2aa13604c50c",
                "toAccount": "000000086736",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-10-25 10:22:05"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {},
                "tranParticular": "mybiz#775a3498-ba1c-4882-be3d-9629457896f7#1SGR2G1H4QL9",
                "amount": "1000",
                "fromAccount": "",
                "updated_timestamp": 1666693326
            },
            "sort": [
                1666693326
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "7ab7871c-8824-44aa-a7ef-1a21bced1016",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "init",
                "createdAt": "2022-10-25 10:20:09",
                "source": "mop_transfer",
                "tranId": "7ab7871c-8824-44aa-a7ef-1a21bced1016",
                "toAccount": "000000086736",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-10-25 10:20:09"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {},
                "tranParticular": "mybiz#775a3498-ba1c-4882-be3d-9629457896f7#99W4BBK033YT",
                "amount": "2000",
                "fromAccount": "",
                "updated_timestamp": 1666693210
            },
            "sort": [
                1666693210
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "92e839e6-f299-4598-822d-e2fa51ca2dc5",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-31T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-10-25 09:57:05",
                "source": "mop_transfer",
                "toAccount": "000000001964",
                "tranId": "92e839e6-f299-4598-822d-e2fa51ca2dc5",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0786637948\", \"id\": \"fe3b8779-c1aa-411d-84da-9559ccb64b57\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-10-25 09:57:10"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-10-25 09:57:05"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"92e839e6-f299-4598-822d-e2fa51ca2dc5\", \"otp\": \"123456\"}",
                            "datetime": "2022-10-25 09:57:27"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000010\", \"tranDate\": \"2022-12-31T00:00:00.000\"}}",
                            "datetime": "2022-10-25 09:57:28"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "fe3b8779-c1aa-411d-84da-9559ccb64b57"
                },
                "finRefId": "YD0000010",
                "tranParticular": "Test 2",
                "amount": "200000",
                "fromAccount": "000000002768",
                "updated_timestamp": 1666691849
            },
            "sort": [
                1666691849
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "8002b744-db29-430b-8709-e17d3cf4ac14",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-31T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-10-25 09:53:14",
                "source": "mop_transfer",
                "toAccount": "000000001964",
                "tranId": "8002b744-db29-430b-8709-e17d3cf4ac14",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0786637948\", \"id\": \"bb66a695-1e33-4c00-b4b9-ea1a54ccd6df\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-10-25 09:53:18"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-10-25 09:53:14"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"8002b744-db29-430b-8709-e17d3cf4ac14\", \"otp\": \"123456\"}",
                            "datetime": "2022-10-25 09:53:46"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000009\", \"tranDate\": \"2022-12-31T00:00:00.000\"}}",
                            "datetime": "2022-10-25 09:53:47"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "bb66a695-1e33-4c00-b4b9-ea1a54ccd6df"
                },
                "finRefId": "YD0000009",
                "tranParticular": "Test",
                "amount": "100000",
                "fromAccount": "000000002768",
                "updated_timestamp": 1666691629
            },
            "sort": [
                1666691629
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "fcb3c9ab-08b8-4d27-9e63-10c899104961",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-31T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-10-24 16:11:10",
                "source": "mop_transfer",
                "toAccount": "000000002017",
                "tranId": "fcb3c9ab-08b8-4d27-9e63-10c899104961",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"b38a9249-2661-497a-9830-735608426c7f\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-10-24 16:11:12"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-10-24 16:11:10"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"fcb3c9ab-08b8-4d27-9e63-10c899104961\", \"otp\": \"123456\"}",
                            "datetime": "2022-10-24 16:11:20"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000003\", \"tranDate\": \"2022-12-31T00:00:00.000\"}}",
                            "datetime": "2022-10-24 16:11:21"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "b38a9249-2661-497a-9830-735608426c7f"
                },
                "finRefId": "YD0000003",
                "tranParticular": "Test transfer",
                "amount": "250000",
                "fromAccount": "000000002762",
                "updated_timestamp": 1666627882
            },
            "sort": [
                1666627882
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "68c07e21-8c50-48e3-8fa9-6ed73374a97d",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-30T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-10-21 17:55:28",
                "source": "mop_transfer",
                "toAccount": "000000001497",
                "tranId": "68c07e21-8c50-48e3-8fa9-6ed73374a97d",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"0115b936-eb87-4efd-aa5c-21f92c654813\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-10-21 17:55:30"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-10-21 17:55:28"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"68c07e21-8c50-48e3-8fa9-6ed73374a97d\", \"otp\": \"123456\"}",
                            "datetime": "2022-10-21 17:55:36"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000014\", \"tranDate\": \"2022-12-30T00:00:00.000\"}}",
                            "datetime": "2022-10-21 17:55:37"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "0115b936-eb87-4efd-aa5c-21f92c654813"
                },
                "finRefId": "YD0000014",
                "tranParticular": "Đêm qua em tuyệt lắm",
                "amount": "125000",
                "fromAccount": "000000002762",
                "updated_timestamp": 1666374938
            },
            "sort": [
                1666374938
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "c8545da2-ada7-4cb0-9160-73e1b45d49ce",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-30T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-10-21 17:46:50",
                "source": "mop_transfer",
                "toAccount": "000000001497",
                "tranId": "c8545da2-ada7-4cb0-9160-73e1b45d49ce",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"179ca892-2515-4036-ad46-b864a27d1432\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-10-21 17:46:52"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-10-21 17:46:50"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"c8545da2-ada7-4cb0-9160-73e1b45d49ce\", \"otp\": \"123456\"}",
                            "datetime": "2022-10-21 17:46:59"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000013\", \"tranDate\": \"2022-12-30T00:00:00.000\"}}",
                            "datetime": "2022-10-21 17:47:00"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "179ca892-2515-4036-ad46-b864a27d1432"
                },
                "finRefId": "YD0000013",
                "tranParticular": "Test lah",
                "amount": "2500000",
                "fromAccount": "000000002762",
                "updated_timestamp": 1666374420
            },
            "sort": [
                1666374420
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "a7607517-d386-431e-84b5-689c12115e3c",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-29T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-10-21 14:32:40",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "a7607517-d386-431e-84b5-689c12115e3c",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"ea8b2682-5aaf-4e4a-8249-65e60cec1377\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-10-21 14:32:43"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-10-21 14:32:40"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"a7607517-d386-431e-84b5-689c12115e3c\", \"otp\": \"123456\"}",
                            "datetime": "2022-10-21 14:32:50"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000031\", \"tranDate\": \"2022-12-29T00:00:00.000\"}}",
                            "datetime": "2022-10-21 14:32:51"
                        }
                    ]
                },
                "typeTran": "out",
                "accountType": "A",
                "extData": {
                    "otpId": "ea8b2682-5aaf-4e4a-8249-65e60cec1377"
                },
                "finRefId": "YD0000031",
                "tranParticular": "101010",
                "amount": "10000",
                "fromAccount": "000000002762",
                "updated_timestamp": 1666362772
            },
            "sort": [
                1666362772
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "6283377e-6bac-49e3-bf96-6799be978458",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-29T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-10-19 16:49:21",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "6283377e-6bac-49e3-bf96-6799be978458",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"448a8817-b6e5-4f58-b5a0-61953aabe08c\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-10-19 16:49:23"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-10-19 16:49:21"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"6283377e-6bac-49e3-bf96-6799be978458\", \"otp\": \"123456\"}",
                            "datetime": "2022-10-19 16:49:32"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000012\", \"tranDate\": \"2022-12-29T00:00:00.000\"}}",
                            "datetime": "2022-10-19 16:49:33"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "448a8817-b6e5-4f58-b5a0-61953aabe08c"
                },
                "finRefId": "YD0000012",
                "tranParticular": "Thanh toán mới",
                "amount": "50000",
                "fromAccount": "000000002762",
                "updated_timestamp": 1666198175
            },
            "sort": [
                1666198175
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "4bf6a337-1cae-4c47-abfd-ba2fd4721b4a",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-29T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-10-19 16:47:39",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "4bf6a337-1cae-4c47-abfd-ba2fd4721b4a",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"f18d823a-eea3-4423-a78b-0e6f4a4dfcc8\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-10-19 16:47:42"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-10-19 16:47:39"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"4bf6a337-1cae-4c47-abfd-ba2fd4721b4a\", \"otp\": \"123456\"}",
                            "datetime": "2022-10-19 16:47:51"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000011\", \"tranDate\": \"2022-12-29T00:00:00.000\"}}",
                            "datetime": "2022-10-19 16:47:53"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "f18d823a-eea3-4423-a78b-0e6f4a4dfcc8"
                },
                "finRefId": "YD0000011",
                "tranParticular": "Thanh toán cho Quang",
                "amount": "50000",
                "fromAccount": "000000002762",
                "updated_timestamp": 1666198074
            },
            "sort": [
                1666198074
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "b6c314f7-7071-406c-8dc9-fcbf9f92a26a",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-17 18:01:38",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "b6c314f7-7071-406c-8dc9-fcbf9f92a26a",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-17 18:01:38"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"b6c314f7-7071-406c-8dc9-fcbf9f92a26a\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-17 18:02:19"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000325\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-17 18:02:20"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "finRefId": "YD0000325",
                "tranParticular": "Abc",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747615
            },
            "sort": [
                1665747615
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "5eae0eba-453f-4df7-b6cf-a14cd247fa8d",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-16 10:52:09",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "5eae0eba-453f-4df7-b6cf-a14cd247fa8d",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-16 10:52:09"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"5eae0eba-453f-4df7-b6cf-a14cd247fa8d\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-16 10:52:44"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000287\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-16 10:52:46"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "964952",
                    "otpTS": 1660621930
                },
                "finRefId": "YD0000287",
                "tranParticular": "Abc",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747615
            },
            "sort": [
                1665747615
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "628c70b7-8bb8-4c4f-a38b-ac12e6b84147",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-16 11:14:02",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "628c70b7-8bb8-4c4f-a38b-ac12e6b84147",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-16 11:14:02"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"628c70b7-8bb8-4c4f-a38b-ac12e6b84147\", \"otp\": \"000000\"}",
                            "datetime": "2022-08-16 11:36:05"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000288\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-16 11:36:06"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "328169",
                    "otpTS": 1660624539
                },
                "finRefId": "YD0000288",
                "tranParticular": "test transfer 100.000 to test account",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747614
            },
            "sort": [
                1665747614
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "ff6d85d2-cfee-4c7b-8ca8-6aebfc1690e4",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "error",
                "createdAt": "2022-09-23 13:53:44",
                "source": "mop_transfer",
                "toAccount": "000000001491",
                "tranId": "ff6d85d2-cfee-4c7b-8ca8-6aebfc1690e4",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"716a7d5c-a986-4c1b-b439-19fdfaaf3d23\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-09-23 13:53:46"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-09-23 13:53:44"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"ff6d85d2-cfee-4c7b-8ca8-6aebfc1690e4\", \"otp\": \"123456\"}",
                            "datetime": "2022-09-23 13:53:58"
                        }
                    ],
                    "error": [
                        {
                            "message": "\"{\\\"meta\\\": {\\\"REQUESTUUID\\\": \\\"30478556-b462-4fc7-96df-5424f0ee10bf\\\",\\\"GLOBALUUID\\\": \\\"0c9f89b8-b64a-4e9a-86ef-08a1eff1d842\\\",\\\"contexturl\\\":\\\"\\\"},\\\"errorDetails\\\":[{\\\"errorDesc\\\" :\\\"Finacle System Error Occurred!!! Please contact System Administrator.\\\",\\\"errorCode\\\" :\\\"4140\\\"}]}\"",
                            "datetime": "2022-09-23 13:54:15"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "716a7d5c-a986-4c1b-b439-19fdfaaf3d23"
                },
                "tranParticular": "Mô tả",
                "amount": "20000",
                "fromAccount": "000000002683",
                "updated_timestamp": 1665747614
            },
            "sort": [
                1665747614
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "b216b0da-5693-48f3-b390-3c2f953b9d9c",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-08 09:59:33",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "b216b0da-5693-48f3-b390-3c2f953b9d9c",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-08 09:59:33"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"b216b0da-5693-48f3-b390-3c2f953b9d9c\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-08 09:59:42"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000195\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-08 09:59:43"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "463354",
                    "otpTS": 1659927574
                },
                "finRefId": "YD0000195",
                "tranParticular": "test transfer 100.000 to test account",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747614
            },
            "sort": [
                1665747614
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "5ef7e611-de01-4252-a2e7-3db2bfdc7ee0",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-20T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-09-20 14:58:58",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "5ef7e611-de01-4252-a2e7-3db2bfdc7ee0",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0973370149\", \"id\": \"ba99a4ba-b392-4e0c-a39a-f444336234c6\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-09-20 14:59:01"
                        },
                        {
                            "message": "{\"phone\": \"0973370149\", \"id\": \"82c5d86a-4f40-4679-87d4-6803957fac83\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-09-20 15:24:03"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-09-20 14:58:58"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"5ef7e611-de01-4252-a2e7-3db2bfdc7ee0\", \"otp\": \"123456\"}",
                            "datetime": "2022-09-20 14:59:13"
                        },
                        {
                            "message": "{\"tranId\": \"5ef7e611-de01-4252-a2e7-3db2bfdc7ee0\", \"otp\": \"123456\"}",
                            "datetime": "2022-09-20 15:24:16"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000047\", \"tranDate\": \"2022-12-20T00:00:00.000\"}}",
                            "datetime": "2022-09-20 14:59:37"
                        },
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000048\", \"tranDate\": \"2022-12-20T00:00:00.000\"}}",
                            "datetime": "2022-09-20 15:24:40"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "82c5d86a-4f40-4679-87d4-6803957fac83"
                },
                "finRefId": "YD0000047",
                "tranParticular": "100000",
                "amount": "10000",
                "fromAccount": "000000002607",
                "updated_timestamp": 1665747614
            },
            "sort": [
                1665747614
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "4c5b85af-df89-4405-a485-b553e8e67619",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-20T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-09-20 10:48:16",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "4c5b85af-df89-4405-a485-b553e8e67619",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0973370149\", \"id\": \"112dbc5f-b70b-4a6b-921f-db3451e932be\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-09-20 10:48:20"
                        },
                        {
                            "message": "{\"phone\": \"0973370149\", \"id\": \"4013329d-6982-4e4a-a86d-ce2411e3e601\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-09-20 11:12:46"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-09-20 10:48:16"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"4c5b85af-df89-4405-a485-b553e8e67619\", \"otp\": \"123456\"}",
                            "datetime": "2022-09-20 10:48:39"
                        },
                        {
                            "message": "{\"tranId\": \"4c5b85af-df89-4405-a485-b553e8e67619\", \"otp\": \"123456\"}",
                            "datetime": "2022-09-20 11:12:58"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000037\", \"tranDate\": \"2022-12-20T00:00:00.000\"}}",
                            "datetime": "2022-09-20 10:49:00"
                        },
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000039\", \"tranDate\": \"2022-12-20T00:00:00.000\"}}",
                            "datetime": "2022-09-20 11:13:23"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "4013329d-6982-4e4a-a86d-ce2411e3e601"
                },
                "finRefId": "YD0000037",
                "tranParticular": "Gjfjdjs",
                "amount": "100000",
                "fromAccount": "000000002607",
                "updated_timestamp": 1665747614
            },
            "sort": [
                1665747614
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "cde51b30-d83f-4524-9816-4ae138e080e8",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-11 12:01:56",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "cde51b30-d83f-4524-9816-4ae138e080e8",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-11 12:01:56"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"cde51b30-d83f-4524-9816-4ae138e080e8\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-11 12:02:08"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000245\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-11 12:02:09"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "605701",
                    "otpTS": 1660194117
                },
                "finRefId": "YD0000245",
                "tranParticular": "Abc",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747613
            },
            "sort": [
                1665747613
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "f9223083-9ff2-405b-b4f0-7c0beca0a9b3",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "otp_verified",
                "createdAt": "2022-07-14 15:49:09",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "f9223083-9ff2-405b-b4f0-7c0beca0a9b3",
                "accountType": "A",
                "data": {
                    "otp": "594290",
                    "otpTS": 1657788550
                },
                "tranParticular": "test transfer to UBank",
                "amount": "1500000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747613
            },
            "sort": [
                1665747613
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "cf301d39-af3b-4191-9f12-c58a076120c7",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "otp_gen",
                "createdAt": "2022-08-16 14:37:27",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "cf301d39-af3b-4191-9f12-c58a076120c7",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-16 14:37:27"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "658977",
                    "otpTS": 1660635466
                },
                "tranParticular": "test transfer 100.000 to test account",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747613
            },
            "sort": [
                1665747613
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "1900b71e-0f9f-4e07-a847-bb3a63797a67",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-18 17:38:06",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "1900b71e-0f9f-4e07-a847-bb3a63797a67",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-18 17:38:06"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"1900b71e-0f9f-4e07-a847-bb3a63797a67\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-18 17:38:20"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000397\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-18 17:38:22"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "finRefId": "YD0000397",
                "tranParticular": "Abc",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747612
            },
            "sort": [
                1665747612
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "f00e6b34-caaa-4a61-8d7c-b7534efdea5c",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-22 10:14:36",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "f00e6b34-caaa-4a61-8d7c-b7534efdea5c",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-22 10:14:36"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"f00e6b34-caaa-4a61-8d7c-b7534efdea5c\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-22 10:14:47"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000435\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-22 10:14:49"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "finRefId": "YD0000435",
                "tranParticular": "test transfer to MB bank 7",
                "amount": "50000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747612
            },
            "sort": [
                1665747612
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "5bb6ffc5-e79a-44c8-a8aa-8412186bb114",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-20T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-09-20 13:44:06",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "5bb6ffc5-e79a-44c8-a8aa-8412186bb114",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0973370149\", \"id\": \"2967b7f1-0eff-4b5a-a499-c7900ead43b9\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-09-20 13:44:10"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-09-20 13:44:06"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"5bb6ffc5-e79a-44c8-a8aa-8412186bb114\", \"otp\": \"123456\"}",
                            "datetime": "2022-09-20 13:44:24"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000044\", \"tranDate\": \"2022-12-20T00:00:00.000\"}}",
                            "datetime": "2022-09-20 13:44:50"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "2967b7f1-0eff-4b5a-a499-c7900ead43b9"
                },
                "finRefId": "YD0000044",
                "tranParticular": "1133",
                "amount": "10000",
                "fromAccount": "000000002607",
                "updated_timestamp": 1665747612
            },
            "sort": [
                1665747612
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "4919e863-5d58-4f01-aea4-f3f61995a364",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-18T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-08-25 11:54:20",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "4919e863-5d58-4f01-aea4-f3f61995a364",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0348076886\", \"id\": \"3eafc03c-bba9-4143-9f19-61dead680dbf\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-08-25 11:54:22"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-25 11:54:20"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"4919e863-5d58-4f01-aea4-f3f61995a364\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-25 11:54:34"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000584\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-25 11:54:36"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "3eafc03c-bba9-4143-9f19-61dead680dbf"
                },
                "finRefId": "YD0000584",
                "tranParticular": "Addggh",
                "amount": "10000",
                "fromAccount": "000000002540",
                "updated_timestamp": 1665747612
            },
            "sort": [
                1665747612
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "c2979460-892e-48f2-b55f-f4660b624c68",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-20T00:00:00.000",
                "status": "error",
                "createdAt": "2022-09-20 15:46:31",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "c2979460-892e-48f2-b55f-f4660b624c68",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0973370149\", \"id\": \"5a18365b-e2a7-40df-88a3-b34129420b2a\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-09-20 15:46:34"
                        },
                        {
                            "message": "{\"phone\": \"0973370149\", \"id\": \"afdd34e3-4303-4f73-8fd7-4c79f1e6957f\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-09-20 16:03:58"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-09-20 15:46:31"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"c2979460-892e-48f2-b55f-f4660b624c68\", \"otp\": \"123456\"}",
                            "datetime": "2022-09-20 15:46:56"
                        },
                        {
                            "message": "{\"tranId\": \"c2979460-892e-48f2-b55f-f4660b624c68\", \"otp\": \"123456\"}",
                            "datetime": "2022-09-20 16:04:15"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000049\", \"tranDate\": \"2022-12-20T00:00:00.000\"}}",
                            "datetime": "2022-09-20 15:47:21"
                        }
                    ],
                    "error": [
                        {
                            "message": "\"{\\\"message\\\": \\\"Endpoint request timed out\\\"}\"",
                            "datetime": "2022-09-20 16:04:44"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "afdd34e3-4303-4f73-8fd7-4c79f1e6957f"
                },
                "finRefId": "YD0000049",
                "tranParticular": "11111",
                "amount": "15000",
                "fromAccount": "000000002607",
                "updated_timestamp": 1665747611
            },
            "sort": [
                1665747611
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "7825e25f-6c2a-4663-a6d6-70217673430e",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-07-14 17:29:36",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "7825e25f-6c2a-4663-a6d6-70217673430e",
                "accountType": "A",
                "data": {
                    "otp": "090095",
                    "otpTS": 1657794577
                },
                "finRefId": "YD0000071",
                "tranParticular": "Payment for merchant UBank",
                "amount": "3000000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747611
            },
            "sort": [
                1665747611
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "04d50617-1d59-4fd3-b929-4c7d42b18b1f",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-08 17:54:10",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "04d50617-1d59-4fd3-b929-4c7d42b18b1f",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-08 17:54:10"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"04d50617-1d59-4fd3-b929-4c7d42b18b1f\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-08 17:54:19"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000202\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-08 17:54:20"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "061413",
                    "otpTS": 1659956051
                },
                "finRefId": "YD0000202",
                "tranParticular": "PO000076-THANH TOÁN",
                "amount": "400000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747611
            },
            "sort": [
                1665747611
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "a185c2ef-f80e-44dc-b8d4-463fcced145a",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-19 10:40:08",
                "source": "mop_transfer",
                "toAccount": "000000001491",
                "tranId": "a185c2ef-f80e-44dc-b8d4-463fcced145a",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-19 10:40:08"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"a185c2ef-f80e-44dc-b8d4-463fcced145a\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-19 10:40:17"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000402\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-19 10:40:18"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "finRefId": "YD0000402",
                "tranParticular": "Test",
                "amount": "20000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747610
            },
            "sort": [
                1665747610
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "a7aa5435-cabc-44b1-9cd6-6821442e03f0",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-16 17:30:24",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "a7aa5435-cabc-44b1-9cd6-6821442e03f0",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-16 17:30:24"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"a7aa5435-cabc-44b1-9cd6-6821442e03f0\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-16 17:30:31"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000304\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-16 17:30:33"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "016206",
                    "otpTS": 1660645824
                },
                "finRefId": "YD0000304",
                "tranParticular": "Abc",
                "amount": "80000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747610
            },
            "sort": [
                1665747610
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "844ba8ee-7dde-41aa-84f8-fd4b08b1649e",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-24T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-09-29 16:44:57",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "844ba8ee-7dde-41aa-84f8-fd4b08b1649e",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0973370149\", \"id\": \"28ed9b4f-c4c6-4f8e-bf2f-67457e759550\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-09-29 16:44:59"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-09-29 16:44:57"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"844ba8ee-7dde-41aa-84f8-fd4b08b1649e\", \"otp\": \"123456\"}",
                            "datetime": "2022-09-29 16:45:14"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000019\", \"tranDate\": \"2022-12-24T00:00:00.000\"}}",
                            "datetime": "2022-09-29 16:45:37"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "28ed9b4f-c4c6-4f8e-bf2f-67457e759550"
                },
                "finRefId": "YD0000019",
                "tranParticular": "Test",
                "amount": "100000",
                "fromAccount": "000000002607",
                "updated_timestamp": 1665747610
            },
            "sort": [
                1665747610
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "80db6d0e-05a5-4b8a-a2ca-aaa342b0b56e",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-17 14:08:55",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "80db6d0e-05a5-4b8a-a2ca-aaa342b0b56e",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-17 14:08:55"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"80db6d0e-05a5-4b8a-a2ca-aaa342b0b56e\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-17 14:09:04"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000322\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-17 14:09:05"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "702432",
                    "otpTS": 1660720136
                },
                "finRefId": "YD0000322",
                "tranParticular": "Abc",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747610
            },
            "sort": [
                1665747610
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "3d73434d-1c5e-43c3-97d3-381c52fa9cfb",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "otp_gen",
                "createdAt": "2022-08-16 14:56:39",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "3d73434d-1c5e-43c3-97d3-381c52fa9cfb",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-16 14:56:39"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "688281",
                    "otpTS": 1660636599
                },
                "tranParticular": "Abc",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747609
            },
            "sort": [
                1665747609
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "f9c95886-3512-4eac-9863-ed3d2eb831a1",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-18T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-08-24 15:56:09",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "f9c95886-3512-4eac-9863-ed3d2eb831a1",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-24 15:56:09"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"f9c95886-3512-4eac-9863-ed3d2eb831a1\", \"otp\": \"190840\"}",
                            "datetime": "2022-08-24 15:57:03"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000538\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-24 15:57:05"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "53b07448-3d2f-4104-a553-66cf84a4b203"
                },
                "finRefId": "YD0000538",
                "tranParticular": "test transfer to MB bank 7",
                "amount": "50000",
                "fromAccount": "000000002540",
                "updated_timestamp": 1665747609
            },
            "sort": [
                1665747609
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "148f8ead-1f39-4789-94e0-81d61f38c730",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-16 16:49:43",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "148f8ead-1f39-4789-94e0-81d61f38c730",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-16 16:49:43"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"148f8ead-1f39-4789-94e0-81d61f38c730\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-16 16:49:51"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000295\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-16 16:49:52"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "350399",
                    "otpTS": 1660643384
                },
                "finRefId": "YD0000295",
                "tranParticular": "Abc",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747609
            },
            "sort": [
                1665747609
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "17da876d-4dbc-4e5c-bae0-34f903962345",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "init",
                "createdAt": "2022-08-18 18:15:19",
                "source": "mop_transfer",
                "tranId": "17da876d-4dbc-4e5c-bae0-34f903962345",
                "toAccount": "000000001491",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-18 18:15:19"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "tranParticular": "111",
                "amount": "10000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747609
            },
            "sort": [
                1665747609
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "7343a869-3a6c-4fe6-a075-60b2067bdc2d",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-19 10:46:14",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "7343a869-3a6c-4fe6-a075-60b2067bdc2d",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-19 10:46:14"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"7343a869-3a6c-4fe6-a075-60b2067bdc2d\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-19 10:46:35"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000403\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-19 10:46:36"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "finRefId": "YD0000403",
                "tranParticular": "Abcdfegehdj",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747608
            },
            "sort": [
                1665747608
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "4e8f8065-97a1-4213-af70-3e644d6c2b5e",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "error",
                "createdAt": "2022-09-23 15:49:18",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "4e8f8065-97a1-4213-af70-3e644d6c2b5e",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"5baef20a-2cf3-4499-a4d6-6b64364635f1\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-09-23 15:49:20"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-09-23 15:49:18"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"4e8f8065-97a1-4213-af70-3e644d6c2b5e\", \"otp\": \"123456\"}",
                            "datetime": "2022-09-23 15:49:33"
                        }
                    ],
                    "error": [
                        {
                            "message": "\"{\\\"meta\\\": {\\\"REQUESTUUID\\\": \\\"f728c45a-b5e0-4498-a61e-af0857df8e3f\\\",\\\"GLOBALUUID\\\": \\\"4c1dfdba-0f45-4b48-8be3-3b1216b8965b\\\",\\\"contexturl\\\":\\\"\\\"},\\\"errorDetails\\\":[{\\\"errorDesc\\\" :\\\"Finacle System Error Occurred!!! Please contact System Administrator.\\\",\\\"errorCode\\\" :\\\"4140\\\"}]}\"",
                            "datetime": "2022-09-23 15:49:48"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "5baef20a-2cf3-4499-a4d6-6b64364635f1"
                },
                "tranParticular": "Test",
                "amount": "50000",
                "fromAccount": "000000002683",
                "updated_timestamp": 1665747608
            },
            "sort": [
                1665747608
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "1f744c2c-87a5-430d-8356-0a79f9c0b286",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "otp_gen",
                "createdAt": "2022-08-17 14:12:14",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "1f744c2c-87a5-430d-8356-0a79f9c0b286",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-17 14:12:14"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "136119",
                    "otpTS": 1660720334
                },
                "tranParticular": "Abc",
                "amount": "1000000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747607
            },
            "sort": [
                1665747607
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "ef19c268-4bf0-46a4-a7fe-4535a0289697",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "otp_gen",
                "createdAt": "2022-08-15 14:33:00",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "ef19c268-4bf0-46a4-a7fe-4535a0289697",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-15 14:33:00"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "125925",
                    "otpTS": 1660548780
                },
                "tranParticular": "ABC",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747607
            },
            "sort": [
                1665747607
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "807309af-f2dd-4b7a-82a5-95e05e969c88",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-07-14 16:01:08",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "807309af-f2dd-4b7a-82a5-95e05e969c88",
                "accountType": "A",
                "data": {
                    "otp": "210253",
                    "otpTS": 1657789269
                },
                "finRefId": "YD0000064",
                "tranParticular": "test transfer to UBank",
                "amount": "1500000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747607
            },
            "sort": [
                1665747607
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "445c1697-bbe9-4485-89f9-81817708d7e9",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-04 15:46:14",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "445c1697-bbe9-4485-89f9-81817708d7e9",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-04 15:46:14"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"445c1697-bbe9-4485-89f9-81817708d7e9\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-04 15:46:31"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000183\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-04 15:46:32"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "596455",
                    "otpTS": 1659602775
                },
                "finRefId": "YD0000183",
                "tranParticular": "Testing",
                "amount": "50000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747607
            },
            "sort": [
                1665747607
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "20b41920-cc8f-4d93-9ed8-c44be041c3e4",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-18T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-08-25 15:04:52",
                "source": "mop_transfer",
                "toAccount": "000000001497",
                "tranId": "20b41920-cc8f-4d93-9ed8-c44be041c3e4",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0348076886\", \"id\": \"1e725a5c-0fa6-418c-a29a-15614d17b91a\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-08-25 15:04:54"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-25 15:04:52"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"20b41920-cc8f-4d93-9ed8-c44be041c3e4\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-25 15:05:02"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000608\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-25 15:05:04"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "1e725a5c-0fa6-418c-a29a-15614d17b91a"
                },
                "finRefId": "YD0000608",
                "tranParticular": "Abc",
                "amount": "10000",
                "fromAccount": "000000002540",
                "updated_timestamp": 1665747607
            },
            "sort": [
                1665747607
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "d072a46b-2cdf-4f90-bc2a-45d6186b01a4",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "otp_verified",
                "createdAt": "2022-08-08 17:28:22",
                "source": "mop_transfer",
                "toAccount": "4002205098117",
                "tranId": "d072a46b-2cdf-4f90-bc2a-45d6186b01a4",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-08 17:28:22"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"d072a46b-2cdf-4f90-bc2a-45d6186b01a4\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-08 17:29:03"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "291841",
                    "otpTS": 1659954503
                },
                "tranParticular": "Aaaaa",
                "amount": "58000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747606
            },
            "sort": [
                1665747606
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "edcc194f-70fa-44dd-9036-6c341a80ca7e",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "otp_gen",
                "createdAt": "2022-08-16 16:19:11",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "edcc194f-70fa-44dd-9036-6c341a80ca7e",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-16 16:19:11"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "040342",
                    "otpTS": 1660641551
                },
                "tranParticular": "test transfer 100.000 to test account",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747606
            },
            "sort": [
                1665747606
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "ada675f5-82f7-47c5-af78-068143ccd0ad",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "init",
                "createdAt": "2022-07-14 09:29:33",
                "source": "mop_transfer",
                "tranId": "ada675f5-82f7-47c5-af78-068143ccd0ad",
                "toAccount": "000033780214",
                "accountType": "A",
                "data": {},
                "tranParticular": "test transfer to UBank",
                "amount": "1500000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747605
            },
            "sort": [
                1665747605
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "2467eb1d-9681-4000-b1da-3631adaf5600",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-16 17:54:00",
                "source": "mop_transfer",
                "toAccount": "000000001491",
                "tranId": "2467eb1d-9681-4000-b1da-3631adaf5600",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-16 17:54:00"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"2467eb1d-9681-4000-b1da-3631adaf5600\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-16 17:54:08"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000306\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-16 17:54:10"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "084558",
                    "otpTS": 1660647241
                },
                "finRefId": "YD0000306",
                "tranParticular": "test transfer to MB bank 7",
                "amount": "50000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747605
            },
            "sort": [
                1665747605
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "e01d2362-54ca-416e-a9de-61562a11cc52",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-26T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-10-04 14:22:09",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "e01d2362-54ca-416e-a9de-61562a11cc52",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0973370149\", \"id\": \"c1ab214b-3f8e-45c1-8a3e-7bf2d178ede2\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-10-04 14:22:12"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-10-04 14:22:09"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"e01d2362-54ca-416e-a9de-61562a11cc52\", \"otp\": \"123456\"}",
                            "datetime": "2022-10-04 14:22:28"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000005\", \"tranDate\": \"2022-12-26T00:00:00.000\"}}",
                            "datetime": "2022-10-04 14:22:29"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "c1ab214b-3f8e-45c1-8a3e-7bf2d178ede2"
                },
                "finRefId": "YD0000005",
                "tranParticular": "Testing",
                "amount": "100000",
                "fromAccount": "000000002720",
                "updated_timestamp": 1665747605
            },
            "sort": [
                1665747605
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "8a67979e-b402-45fc-8770-6cc971e7f3f5",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-22 15:02:46",
                "source": "mop_transfer",
                "toAccount": "000000001491",
                "tranId": "8a67979e-b402-45fc-8770-6cc971e7f3f5",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-22 15:02:46"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"8a67979e-b402-45fc-8770-6cc971e7f3f5\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-22 15:02:57"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000448\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-22 15:02:59"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "finRefId": "YD0000448",
                "tranParticular": "Test trả tiền",
                "amount": "50000",
                "fromAccount": "000000002511",
                "updated_timestamp": 1665747605
            },
            "sort": [
                1665747605
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "78e3aa77-a833-4324-ac0b-c11ad7a1881d",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-18T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-08-25 14:56:59",
                "source": "mop_transfer",
                "toAccount": "000000001497",
                "tranId": "78e3aa77-a833-4324-ac0b-c11ad7a1881d",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0348076886\", \"id\": \"e77adb71-8adc-4d93-9e54-5c427575316e\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-08-25 14:57:01"
                        },
                        {
                            "message": "{\"phone\": \"0348076886\", \"id\": \"0ccbc66f-8207-4c08-a271-a79cfc349c0e\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-08-25 15:01:01"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-25 14:56:59"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"78e3aa77-a833-4324-ac0b-c11ad7a1881d\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-25 15:01:09"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000607\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-25 15:01:10"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "0ccbc66f-8207-4c08-a271-a79cfc349c0e"
                },
                "finRefId": "YD0000607",
                "tranParticular": "Abc",
                "amount": "10000",
                "fromAccount": "000000002540",
                "updated_timestamp": 1665747605
            },
            "sort": [
                1665747605
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "88eb9e4d-22b4-4bff-9759-a38bd9ac9643",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-20T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-09-22 14:47:46",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "88eb9e4d-22b4-4bff-9759-a38bd9ac9643",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0973370149\", \"id\": \"2b1a3a81-30cf-4ff4-ba52-03f359662ec3\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-09-22 14:47:48"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-09-22 14:47:46"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"88eb9e4d-22b4-4bff-9759-a38bd9ac9643\", \"otp\": \"123456\"}",
                            "datetime": "2022-09-22 14:48:05"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000068\", \"tranDate\": \"2022-12-20T00:00:00.000\"}}",
                            "datetime": "2022-09-22 14:48:28"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "2b1a3a81-30cf-4ff4-ba52-03f359662ec3"
                },
                "finRefId": "YD0000068",
                "tranParticular": "Test 20k",
                "amount": "20000",
                "fromAccount": "000000002607",
                "updated_timestamp": 1665747604
            },
            "sort": [
                1665747604
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "878a720c-d0d2-492e-9c5f-c87afce9ab19",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-18 16:13:14",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "878a720c-d0d2-492e-9c5f-c87afce9ab19",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-18 16:13:14"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"878a720c-d0d2-492e-9c5f-c87afce9ab19\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-18 16:13:30"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000385\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-18 16:13:31"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "finRefId": "YD0000385",
                "tranParticular": "Abc",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747604
            },
            "sort": [
                1665747604
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "50810eae-09c1-49ce-9379-a5895b2e4662",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-08 17:59:14",
                "source": "mop_transfer",
                "toAccount": "000000001933",
                "tranId": "50810eae-09c1-49ce-9379-a5895b2e4662",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-08 17:59:14"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"50810eae-09c1-49ce-9379-a5895b2e4662\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-08 17:59:22"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000204\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-08 17:59:23"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "631313",
                    "otpTS": 1659956354
                },
                "finRefId": "YD0000204",
                "tranParticular": "Tiền điện tháng 8",
                "amount": "120000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747604
            },
            "sort": [
                1665747604
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "5aac7394-79e3-4720-a237-9b40dfabc695",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "init",
                "createdAt": "2022-07-14 10:12:59",
                "source": "mop_transfer",
                "tranId": "5aac7394-79e3-4720-a237-9b40dfabc695",
                "toAccount": "000033780214",
                "accountType": "A",
                "data": {},
                "tranParticular": "test transfer to UBank",
                "amount": "1500000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747604
            },
            "sort": [
                1665747604
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "068327c0-a482-42cf-ba11-92efc211e18e",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "init",
                "createdAt": "2022-08-24 10:22:58",
                "source": "mop_transfer",
                "tranId": "068327c0-a482-42cf-ba11-92efc211e18e",
                "toAccount": "000000001496",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-24 10:22:58"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "tranParticular": "test transfer to MB bank 7",
                "amount": "50000",
                "fromAccount": "000000002535",
                "updated_timestamp": 1665747604
            },
            "sort": [
                1665747604
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "643f8b9c-3d17-484c-b697-37b55b5ccc22",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-20T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-09-20 16:07:53",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "643f8b9c-3d17-484c-b697-37b55b5ccc22",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0973370149\", \"id\": \"438498bc-4e97-441d-87ff-bc30ad8b20d0\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-09-20 16:07:55"
                        },
                        {
                            "message": "{\"phone\": \"0973370149\", \"id\": \"0ca82cb4-756d-4b75-bcea-b77f6be7b27b\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-09-20 16:24:02"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-09-20 16:07:53"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"643f8b9c-3d17-484c-b697-37b55b5ccc22\", \"otp\": \"123456\"}",
                            "datetime": "2022-09-20 16:08:26"
                        },
                        {
                            "message": "{\"tranId\": \"643f8b9c-3d17-484c-b697-37b55b5ccc22\", \"otp\": \"123456\"}",
                            "datetime": "2022-09-20 16:25:13"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000051\", \"tranDate\": \"2022-12-20T00:00:00.000\"}}",
                            "datetime": "2022-09-20 16:08:48"
                        },
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000052\", \"tranDate\": \"2022-12-20T00:00:00.000\"}}",
                            "datetime": "2022-09-20 16:25:38"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "0ca82cb4-756d-4b75-bcea-b77f6be7b27b"
                },
                "finRefId": "YD0000051",
                "tranParticular": "9999",
                "amount": "33333",
                "fromAccount": "000000002607",
                "updated_timestamp": 1665747604
            },
            "sort": [
                1665747604
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "2f31f815-75d7-4765-a0b3-5769911968c1",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-17 14:21:01",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "2f31f815-75d7-4765-a0b3-5769911968c1",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-17 14:21:01"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"2f31f815-75d7-4765-a0b3-5769911968c1\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-17 14:21:13"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000323\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-17 14:21:15"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "990162",
                    "otpTS": 1660720861
                },
                "finRefId": "YD0000323",
                "tranParticular": "Abc",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747603
            },
            "sort": [
                1665747603
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "73e9003e-a6ad-4ef9-b6fa-79c0278c9aff",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-10 09:54:08",
                "source": "mop_transfer",
                "toAccount": "000000001933",
                "tranId": "73e9003e-a6ad-4ef9-b6fa-79c0278c9aff",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-10 09:54:08"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"73e9003e-a6ad-4ef9-b6fa-79c0278c9aff\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-10 09:54:16"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000229\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-10 09:54:18"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "329136",
                    "otpTS": 1660100049
                },
                "finRefId": "YD0000229",
                "tranParticular": "test transfer 100.000 to test account",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747603
            },
            "sort": [
                1665747603
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "fc439f87-cd2b-45d8-a80d-3ecb351198d9",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-16 15:38:15",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "fc439f87-cd2b-45d8-a80d-3ecb351198d9",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-16 15:38:15"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"fc439f87-cd2b-45d8-a80d-3ecb351198d9\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-16 15:38:49"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000293\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-16 15:38:51"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "327902",
                    "otpTS": 1660639110
                },
                "finRefId": "YD0000293",
                "tranParticular": "Abc",
                "amount": "50000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747603
            },
            "sort": [
                1665747603
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "173fe93f-b092-44e5-8a99-86d4e62c1901",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-18T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-08-23 16:29:57",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "173fe93f-b092-44e5-8a99-86d4e62c1901",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-23 16:29:57"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"173fe93f-b092-44e5-8a99-86d4e62c1901\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-23 16:30:15"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000483\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-23 16:30:16"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "finRefId": "YD0000483",
                "tranParticular": "Test mô tả",
                "amount": "100000",
                "fromAccount": "000000002535",
                "updated_timestamp": 1665747602
            },
            "sort": [
                1665747602
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "6618ef21-5136-4570-b898-5b81e61e2e53",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "error",
                "createdAt": "2022-07-14 11:50:28",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "6618ef21-5136-4570-b898-5b81e61e2e53",
                "accountType": "A",
                "data": {
                    "otp": "458850",
                    "otpTS": 1657774230
                },
                "finRefId": "",
                "tranParticular": "test transfer to UBank",
                "amount": "1500000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747602
            },
            "sort": [
                1665747602
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "fd668351-e764-4de2-83c6-48049f51260c",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-04 16:39:20",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "fd668351-e764-4de2-83c6-48049f51260c",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-04 16:39:20"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"fd668351-e764-4de2-83c6-48049f51260c\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-04 16:39:30"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000184\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-04 16:39:31"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "179576",
                    "otpTS": 1659605961
                },
                "finRefId": "YD0000184",
                "tranParticular": "Testing",
                "amount": "20000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747602
            },
            "sort": [
                1665747602
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "e3f46f37-529f-4a18-98de-f0b3759dd36f",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-08 17:40:02",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "e3f46f37-529f-4a18-98de-f0b3759dd36f",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-08 17:40:02"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"e3f46f37-529f-4a18-98de-f0b3759dd36f\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-08 17:40:10"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000200\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-08 17:40:12"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "414280",
                    "otpTS": 1659955203
                },
                "finRefId": "YD0000200",
                "tranParticular": "test transfer 120.000 to test account",
                "amount": "120000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747602
            },
            "sort": [
                1665747602
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "4fe6decc-aeba-43b0-8b31-97984748620c",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "init",
                "createdAt": "2022-08-19 16:28:03",
                "source": "mop_transfer",
                "tranId": "4fe6decc-aeba-43b0-8b31-97984748620c",
                "toAccount": "000000001491",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-19 16:28:03"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "tranParticular": "PO000064-I2 VietNam Co.LTD",
                "amount": "18500",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747602
            },
            "sort": [
                1665747602
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "55b696cd-0cd7-42df-b1ef-965b7726685b",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "otp_gen",
                "createdAt": "2022-08-16 16:45:34",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "55b696cd-0cd7-42df-b1ef-965b7726685b",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-16 16:45:34"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "524885",
                    "otpTS": 1660643134
                },
                "tranParticular": "Abc",
                "amount": "10000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747601
            },
            "sort": [
                1665747601
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "e08a8f71-a770-4374-acf3-7837565c7796",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-18T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-08-25 10:52:12",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "e08a8f71-a770-4374-acf3-7837565c7796",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0348076886\", \"id\": \"2dbd9e0d-a8f6-4264-872d-9a7320fdeb98\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-08-25 10:52:17"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-25 10:52:12"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"e08a8f71-a770-4374-acf3-7837565c7796\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-25 10:52:41"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000583\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-25 10:52:42"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "2dbd9e0d-a8f6-4264-872d-9a7320fdeb98"
                },
                "finRefId": "YD0000583",
                "tranParticular": "Asdfhh do hjj",
                "amount": "10000",
                "fromAccount": "000000002540",
                "updated_timestamp": 1665747601
            },
            "sort": [
                1665747601
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "71fc7412-35ad-4424-817d-f7fb9d03f8e9",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-20T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-09-20 16:27:40",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "71fc7412-35ad-4424-817d-f7fb9d03f8e9",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0973370149\", \"id\": \"6c9145c2-4478-487a-b37f-a2bb609c1e47\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-09-20 16:27:43"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-09-20 16:27:40"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"71fc7412-35ad-4424-817d-f7fb9d03f8e9\", \"otp\": \"123456\"}",
                            "datetime": "2022-09-20 16:28:08"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000053\", \"tranDate\": \"2022-12-20T00:00:00.000\"}}",
                            "datetime": "2022-09-20 16:28:29"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "6c9145c2-4478-487a-b37f-a2bb609c1e47"
                },
                "finRefId": "YD0000053",
                "tranParticular": "11111",
                "amount": "10000",
                "fromAccount": "000000002607",
                "updated_timestamp": 1665747601
            },
            "sort": [
                1665747601
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "67a2abcd-26fa-45b8-b611-b34926c7d882",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "otp_gen",
                "createdAt": "2022-08-04 15:01:40",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "67a2abcd-26fa-45b8-b611-b34926c7d882",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-04 15:01:40"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "016089",
                    "otpTS": 1659600100
                },
                "tranParticular": "Testing",
                "amount": "50000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747601
            },
            "sort": [
                1665747601
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "dd9271a7-f49a-4370-9669-5b68a7fe01e9",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-19 10:47:17",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "dd9271a7-f49a-4370-9669-5b68a7fe01e9",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-19 10:47:17"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"dd9271a7-f49a-4370-9669-5b68a7fe01e9\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-19 10:47:40"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000404\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-19 10:47:43"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "finRefId": "YD0000404",
                "tranParticular": "Abc",
                "amount": "10000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747600
            },
            "sort": [
                1665747600
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "eca16150-8e7c-43ac-bcd4-19cf7b8c17bc",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-20T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-09-20 10:36:12",
                "source": "mop_transfer",
                "toAccount": "000000001469",
                "tranId": "eca16150-8e7c-43ac-bcd4-19cf7b8c17bc",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"26f58eaa-13ae-4f56-a01d-545357a98bb9\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-09-20 10:36:15"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-09-20 10:36:12"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"eca16150-8e7c-43ac-bcd4-19cf7b8c17bc\", \"otp\": \"123456\"}",
                            "datetime": "2022-09-20 10:36:36"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000036\", \"tranDate\": \"2022-12-20T00:00:00.000\"}}",
                            "datetime": "2022-09-20 10:37:02"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "26f58eaa-13ae-4f56-a01d-545357a98bb9"
                },
                "finRefId": "YD0000036",
                "tranParticular": "Mô tả nè",
                "amount": "50000",
                "fromAccount": "000000002683",
                "updated_timestamp": 1665747600
            },
            "sort": [
                1665747600
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "5969f129-9401-45a6-945a-f1262faacc68",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-20T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-09-23 15:51:13",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "5969f129-9401-45a6-945a-f1262faacc68",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0973370149\", \"id\": \"173918ba-26c6-453b-8121-d0394821b623\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-09-23 15:51:15"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-09-23 15:51:13"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"5969f129-9401-45a6-945a-f1262faacc68\", \"otp\": \"123456\"}",
                            "datetime": "2022-09-23 15:51:29"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000115\", \"tranDate\": \"2022-12-20T00:00:00.000\"}}",
                            "datetime": "2022-09-23 15:51:54"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "173918ba-26c6-453b-8121-d0394821b623"
                },
                "finRefId": "YD0000115",
                "tranParticular": "Test",
                "amount": "100000",
                "fromAccount": "000000002607",
                "updated_timestamp": 1665747600
            },
            "sort": [
                1665747600
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "6ea7f552-9fb3-4e67-91f8-e7862fa48df0",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "otp_gen",
                "createdAt": "2022-08-08 17:26:59",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "6ea7f552-9fb3-4e67-91f8-e7862fa48df0",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-08 17:26:59"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "297839",
                    "otpTS": 1659954419
                },
                "tranParticular": "PO000019 - Thanh toán",
                "amount": "70000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747600
            },
            "sort": [
                1665747600
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "cbf22172-612b-4936-8097-9d1630021a00",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-18T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-08-24 18:25:49",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "cbf22172-612b-4936-8097-9d1630021a00",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0348076886\", \"id\": \"a940df4b-9028-4667-8deb-bed0d7c79f10\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-08-24 18:25:54"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-24 18:25:49"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"cbf22172-612b-4936-8097-9d1630021a00\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-24 18:26:07"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000574\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-24 18:26:09"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "a940df4b-9028-4667-8deb-bed0d7c79f10"
                },
                "finRefId": "YD0000574",
                "tranParticular": "test transfer to MB bank 8",
                "amount": "10000",
                "fromAccount": "000000002540",
                "updated_timestamp": 1665747600
            },
            "sort": [
                1665747600
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "6681b0ce-2c1c-41f4-b094-8371ff082425",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "init",
                "createdAt": "2022-08-19 16:32:00",
                "source": "mop_transfer",
                "tranId": "6681b0ce-2c1c-41f4-b094-8371ff082425",
                "toAccount": "000000001491",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-19 16:32:00"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "tranParticular": "PO000078-I2 VietNam Co.LTD",
                "amount": "90000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747599
            },
            "sort": [
                1665747599
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "d5f280e6-c202-4652-9f2a-807ec1e9129f",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "otp_verified",
                "createdAt": "2022-07-14 15:54:41",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "d5f280e6-c202-4652-9f2a-807ec1e9129f",
                "accountType": "A",
                "data": {
                    "otp": "564086",
                    "otpTS": 1657788881
                },
                "tranParticular": "test transfer to UBank",
                "amount": "1500000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747599
            },
            "sort": [
                1665747599
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "d63fbd1e-77dd-4e6e-ad8a-41d9937a232a",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "error",
                "createdAt": "2022-09-23 13:24:49",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "d63fbd1e-77dd-4e6e-ad8a-41d9937a232a",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"c57d766a-6b1b-40fc-92a3-d441f580d047\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-09-23 13:24:51"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-09-23 13:24:49"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"d63fbd1e-77dd-4e6e-ad8a-41d9937a232a\", \"otp\": \"123456\"}",
                            "datetime": "2022-09-23 13:25:07"
                        }
                    ],
                    "error": [
                        {
                            "message": "\"{\\\"meta\\\": {\\\"REQUESTUUID\\\": \\\"e130eecf-9274-43c3-8685-c7efd0645fc7\\\",\\\"GLOBALUUID\\\": \\\"d7b25574-6074-4195-9efe-d69c9ee0cdca\\\",\\\"contexturl\\\":\\\"\\\"},\\\"errorDetails\\\":[{\\\"errorDesc\\\" :\\\"Finacle System Error Occurred!!! Please contact System Administrator.\\\",\\\"errorCode\\\" :\\\"4140\\\"}]}\"",
                            "datetime": "2022-09-23 13:25:22"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "c57d766a-6b1b-40fc-92a3-d441f580d047"
                },
                "tranParticular": "Test des",
                "amount": "56000",
                "fromAccount": "000000002683",
                "updated_timestamp": 1665747599
            },
            "sort": [
                1665747599
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "099b7010-fb09-444a-b3d6-ea1a0980a8ea",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "init",
                "createdAt": "2022-08-24 10:04:29",
                "source": "mop_transfer",
                "tranId": "099b7010-fb09-444a-b3d6-ea1a0980a8ea",
                "toAccount": "000000001496",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-24 10:04:29"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "tranParticular": "Hahaha",
                "amount": "50000",
                "fromAccount": "000000002535",
                "updated_timestamp": 1665747598
            },
            "sort": [
                1665747598
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "43cdfd03-08a1-4733-a365-7d06d0f4a3f6",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "init",
                "createdAt": "2022-07-14 11:42:12",
                "source": "mop_transfer",
                "tranId": "43cdfd03-08a1-4733-a365-7d06d0f4a3f6",
                "toAccount": "000033780214",
                "accountType": "A",
                "data": {},
                "tranParticular": "test transfer to UBank",
                "amount": "1500000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747598
            },
            "sort": [
                1665747598
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "d80744cc-1666-4d8e-94b9-3f6058e1f35d",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "otp_gen",
                "createdAt": "2022-08-25 11:01:52",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "d80744cc-1666-4d8e-94b9-3f6058e1f35d",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0348076886\", \"id\": \"6d995df7-c329-4b01-b121-1e9279b6eb1a\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-08-25 11:01:55"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-25 11:01:52"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "6d995df7-c329-4b01-b121-1e9279b6eb1a"
                },
                "tranParticular": "Anc",
                "amount": "10000",
                "fromAccount": "000000002540",
                "updated_timestamp": 1665747598
            },
            "sort": [
                1665747598
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "496b248b-719f-48bf-a6fe-a298e80a87fd",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-08 18:06:43",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "496b248b-719f-48bf-a6fe-a298e80a87fd",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-08 18:06:43"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"496b248b-719f-48bf-a6fe-a298e80a87fd\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-08 18:06:50"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000206\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-08 18:06:52"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "833303",
                    "otpTS": 1659956803
                },
                "finRefId": "YD0000206",
                "tranParticular": "PO000019 và PO000076",
                "amount": "470000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747598
            },
            "sort": [
                1665747598
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "f0a8fba3-292f-4507-a45d-e24a868d5ef5",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-16 18:17:00",
                "source": "mop_transfer",
                "toAccount": "000000001491",
                "tranId": "f0a8fba3-292f-4507-a45d-e24a868d5ef5",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-16 18:17:00"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"f0a8fba3-292f-4507-a45d-e24a868d5ef5\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-16 18:17:07"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000308\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-16 18:17:09"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "499701",
                    "otpTS": 1660648620
                },
                "finRefId": "YD0000308",
                "tranParticular": "test transfer to MB bank 7",
                "amount": "50000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747598
            },
            "sort": [
                1665747598
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "b0b1522b-a1af-479c-a48d-14023702bd35",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "otp_gen",
                "createdAt": "2022-08-16 14:40:20",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "b0b1522b-a1af-479c-a48d-14023702bd35",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-16 14:40:20"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "541907",
                    "otpTS": 1660635620
                },
                "tranParticular": "test transfer 100.000 to test account",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747598
            },
            "sort": [
                1665747598
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "7eea2ef7-cf9f-44de-9c9b-664dcb222115",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-18T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-08-23 21:46:20",
                "source": "mop_transfer",
                "toAccount": "000000001933",
                "tranId": "7eea2ef7-cf9f-44de-9c9b-664dcb222115",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-23 21:46:20"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"7eea2ef7-cf9f-44de-9c9b-664dcb222115\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-23 21:46:33"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000501\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-23 21:46:34"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "finRefId": "YD0000501",
                "tranParticular": "test transfer to MB bank 7",
                "amount": "50000",
                "fromAccount": "000000002535",
                "updated_timestamp": 1665747598
            },
            "sort": [
                1665747598
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "d9b090ac-c532-4fff-bdaa-14be1d9bd477",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-04 15:14:25",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "d9b090ac-c532-4fff-bdaa-14be1d9bd477",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-04 15:14:25"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"d9b090ac-c532-4fff-bdaa-14be1d9bd477\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-04 15:27:21"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000181\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-04 15:27:23"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "371627",
                    "otpTS": 1659600865
                },
                "finRefId": "YD0000181",
                "tranParticular": "Testing",
                "amount": "50000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747597
            },
            "sort": [
                1665747597
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "aca22edb-9573-498d-a10e-ea3554a4d4e6",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "error",
                "createdAt": "2022-09-23 13:52:23",
                "source": "mop_transfer",
                "toAccount": "000000001491",
                "tranId": "aca22edb-9573-498d-a10e-ea3554a4d4e6",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"54b73be4-659b-4dff-805f-caa39d8acfcc\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-09-23 13:52:25"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-09-23 13:52:23"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"aca22edb-9573-498d-a10e-ea3554a4d4e6\", \"otp\": \"123456\"}",
                            "datetime": "2022-09-23 13:52:37"
                        }
                    ],
                    "error": [
                        {
                            "message": "\"{\\\"meta\\\": {\\\"REQUESTUUID\\\": \\\"0672e881-df4f-4113-8d5d-45cb96429e90\\\",\\\"GLOBALUUID\\\": \\\"06a54e87-6a6c-490b-9d62-94639dcdfda7\\\",\\\"contexturl\\\":\\\"\\\"},\\\"errorDetails\\\":[{\\\"errorDesc\\\" :\\\"Finacle System Error Occurred!!! Please contact System Administrator.\\\",\\\"errorCode\\\" :\\\"4140\\\"}]}\"",
                            "datetime": "2022-09-23 13:52:55"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "54b73be4-659b-4dff-805f-caa39d8acfcc"
                },
                "tranParticular": "Tes",
                "amount": "50000",
                "fromAccount": "000000002683",
                "updated_timestamp": 1665747597
            },
            "sort": [
                1665747597
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "60ff6000-e956-492c-8c67-ea80bfe21e35",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-05 10:27:25",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "60ff6000-e956-492c-8c67-ea80bfe21e35",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-05 10:27:25"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"60ff6000-e956-492c-8c67-ea80bfe21e35\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-05 10:27:35"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000189\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-05 10:27:37"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "209782",
                    "otpTS": 1659670046
                },
                "finRefId": "YD0000189",
                "tranParticular": "test transfer 100.000 to test account",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747597
            },
            "sort": [
                1665747597
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "543efc14-4b00-49ec-a98f-a9b01992fd5d",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-18T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-08-25 11:58:29",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "543efc14-4b00-49ec-a98f-a9b01992fd5d",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0348076886\", \"id\": \"bc92189b-dd7b-4de0-ba6d-a9968181c6f6\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-08-25 11:58:31"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-25 11:58:29"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"543efc14-4b00-49ec-a98f-a9b01992fd5d\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-25 11:58:40"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000585\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-25 11:58:41"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "bc92189b-dd7b-4de0-ba6d-a9968181c6f6"
                },
                "finRefId": "YD0000585",
                "tranParticular": "Ghjkk",
                "amount": "10000",
                "fromAccount": "000000002540",
                "updated_timestamp": 1665747597
            },
            "sort": [
                1665747597
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "d66780db-2bdd-4afe-9720-57a1d67394c2",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-18 18:02:23",
                "source": "mop_transfer",
                "toAccount": "000000001419",
                "tranId": "d66780db-2bdd-4afe-9720-57a1d67394c2",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-18 18:02:23"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"d66780db-2bdd-4afe-9720-57a1d67394c2\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-18 18:02:35"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000399\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-18 18:02:36"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "finRefId": "YD0000399",
                "tranParticular": "Hieu hieu",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747597
            },
            "sort": [
                1665747597
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "4b6d8355-5822-40bc-92d2-8aec09b1b7dc",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-19T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-09-07 09:48:12",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "4b6d8355-5822-40bc-92d2-8aec09b1b7dc",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0973370149\", \"id\": \"2d213891-b214-4f26-952a-68f083245a88\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-09-07 09:48:13"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-09-07 09:48:12"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"4b6d8355-5822-40bc-92d2-8aec09b1b7dc\", \"otp\": \"123456\"}",
                            "datetime": "2022-09-07 09:48:24"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000040\", \"tranDate\": \"2022-12-19T00:00:00.000\"}}",
                            "datetime": "2022-09-07 09:48:25"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "2d213891-b214-4f26-952a-68f083245a88"
                },
                "finRefId": "YD0000040",
                "tranParticular": "Abcxyz",
                "amount": "10000",
                "fromAccount": "000000002607",
                "updated_timestamp": 1665747597
            },
            "sort": [
                1665747597
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "af680d60-448e-48cd-8751-f4357f7af8e8",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "otp_gen",
                "createdAt": "2022-08-24 10:43:33",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "af680d60-448e-48cd-8751-f4357f7af8e8",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-24 10:43:33"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "749e3ae4-54df-400b-a95d-889eced7eca8"
                },
                "tranParticular": "test transfer to MB bank 7",
                "amount": "50000",
                "fromAccount": "000000002535",
                "updated_timestamp": 1665747597
            },
            "sort": [
                1665747597
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "b6f8e31e-93e0-4e3e-97be-179aa8cd8142",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "otp_gen",
                "createdAt": "2022-08-16 15:24:44",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "b6f8e31e-93e0-4e3e-97be-179aa8cd8142",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-16 15:24:44"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "427416",
                    "otpTS": 1660638297
                },
                "tranParticular": "test transfer 100.000 to test account",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747597
            },
            "sort": [
                1665747597
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "6a26b103-a2ff-4a97-99c3-235d011452c8",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-19 10:29:04",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "6a26b103-a2ff-4a97-99c3-235d011452c8",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-19 10:29:04"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"6a26b103-a2ff-4a97-99c3-235d011452c8\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-19 10:29:17"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000401\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-19 10:29:18"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "finRefId": "YD0000401",
                "tranParticular": "Test",
                "amount": "20000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747596
            },
            "sort": [
                1665747596
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "92712383-2825-438c-b4b2-fb230950c4aa",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-18T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-08-25 14:36:40",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "92712383-2825-438c-b4b2-fb230950c4aa",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"5d1f0164-b5b9-44f8-a647-3629a83f756a\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-08-25 14:36:42"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-25 14:36:40"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"92712383-2825-438c-b4b2-fb230950c4aa\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-25 14:36:51"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000600\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-25 14:36:52"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "5d1f0164-b5b9-44f8-a647-3629a83f756a"
                },
                "finRefId": "YD0000600",
                "tranParticular": "Mô tả nè",
                "amount": "50000",
                "fromAccount": "000000002533",
                "updated_timestamp": 1665747596
            },
            "sort": [
                1665747596
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "dc85a3fa-4c27-4e8f-b397-d803d8bc4dc8",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-20T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-09-20 21:47:25",
                "source": "mop_transfer",
                "toAccount": "000000001491",
                "tranId": "dc85a3fa-4c27-4e8f-b397-d803d8bc4dc8",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"ee236965-142b-46d2-b961-84e60a1cd95c\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-09-20 21:47:28"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-09-20 21:47:25"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"dc85a3fa-4c27-4e8f-b397-d803d8bc4dc8\", \"otp\": \"123456\"}",
                            "datetime": "2022-09-20 21:47:44"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000057\", \"tranDate\": \"2022-12-20T00:00:00.000\"}}",
                            "datetime": "2022-09-20 21:48:11"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "ee236965-142b-46d2-b961-84e60a1cd95c"
                },
                "finRefId": "YD0000057",
                "tranParticular": "Test mô tả",
                "amount": "52000",
                "fromAccount": "000000002683",
                "updated_timestamp": 1665747596
            },
            "sort": [
                1665747596
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "000bb2d3-2bd2-4221-bbaf-c9e69f2908d7",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-18T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-08-23 16:39:07",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "000bb2d3-2bd2-4221-bbaf-c9e69f2908d7",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-23 16:39:07"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"000bb2d3-2bd2-4221-bbaf-c9e69f2908d7\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-23 16:39:19"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000495\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-23 16:39:21"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "finRefId": "YD0000495",
                "tranParticular": "Quang pro",
                "amount": "50000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747596
            },
            "sort": [
                1665747596
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "5a29b90e-ffe5-4417-8c8d-00b830731304",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-18T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-08-25 01:59:48",
                "source": "mop_transfer",
                "toAccount": "000000001497",
                "tranId": "5a29b90e-ffe5-4417-8c8d-00b830731304",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0348076886\", \"id\": \"296016f1-295e-4ed1-a2a6-f284833060e0\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-08-25 01:59:49"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-25 01:59:48"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"5a29b90e-ffe5-4417-8c8d-00b830731304\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-25 01:59:58"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000576\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-25 01:59:59"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "296016f1-295e-4ed1-a2a6-f284833060e0"
                },
                "finRefId": "YD0000576",
                "tranParticular": "test transfer to MB bank 8",
                "amount": "10000",
                "fromAccount": "000000002540",
                "updated_timestamp": 1665747596
            },
            "sort": [
                1665747596
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "94372d28-ce58-4d49-9d79-79ada13d7a8b",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-20T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-09-20 21:44:48",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "94372d28-ce58-4d49-9d79-79ada13d7a8b",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"eead20b1-e77d-4e9d-8c60-95c2281fc2d3\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-09-20 21:44:51"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-09-20 21:44:48"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"94372d28-ce58-4d49-9d79-79ada13d7a8b\", \"otp\": \"123456\"}",
                            "datetime": "2022-09-20 21:45:11"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000056\", \"tranDate\": \"2022-12-20T00:00:00.000\"}}",
                            "datetime": "2022-09-20 21:45:36"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "eead20b1-e77d-4e9d-8c60-95c2281fc2d3"
                },
                "finRefId": "YD0000056",
                "tranParticular": "Mô tả nè",
                "amount": "55000",
                "fromAccount": "000000002683",
                "updated_timestamp": 1665747596
            },
            "sort": [
                1665747596
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "0ebf8a85-56d0-4f9d-8166-5cb2e2872c45",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-12 09:34:23",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "0ebf8a85-56d0-4f9d-8166-5cb2e2872c45",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-12 09:34:23"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"0ebf8a85-56d0-4f9d-8166-5cb2e2872c45\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-12 09:34:56"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000263\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-12 09:34:58"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "933722",
                    "otpTS": 1660271663
                },
                "finRefId": "YD0000263",
                "tranParticular": "Abc",
                "amount": "208500",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747596
            },
            "sort": [
                1665747596
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "efd11f42-fd98-4d31-b6a7-af2cb025fb6d",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-20T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-09-22 11:06:06",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "efd11f42-fd98-4d31-b6a7-af2cb025fb6d",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0973370149\", \"id\": \"b612ecad-5773-4b1a-85ef-346eb838917c\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-09-22 11:06:13"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-09-22 11:06:06"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"efd11f42-fd98-4d31-b6a7-af2cb025fb6d\", \"otp\": \"123456\"}",
                            "datetime": "2022-09-22 11:06:24"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000066\", \"tranDate\": \"2022-12-20T00:00:00.000\"}}",
                            "datetime": "2022-09-22 11:06:47"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "b612ecad-5773-4b1a-85ef-346eb838917c"
                },
                "finRefId": "YD0000066",
                "tranParticular": "1111",
                "amount": "12000",
                "fromAccount": "000000002607",
                "updated_timestamp": 1665747596
            },
            "sort": [
                1665747596
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "e21e5517-2c90-4a8d-9655-d3b4ad51a5e5",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-07-14 15:11:57",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "e21e5517-2c90-4a8d-9655-d3b4ad51a5e5",
                "accountType": "A",
                "data": {
                    "otp": "215692",
                    "otpTS": 1657786318
                },
                "finRefId": "YD0000063",
                "tranParticular": "test transfer to UBank",
                "amount": "1500000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747596
            },
            "sort": [
                1665747596
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "b7dc2b45-24e1-4edf-91b9-3f9a0d069c69",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-19 10:50:06",
                "source": "mop_transfer",
                "toAccount": "000000001933",
                "tranId": "b7dc2b45-24e1-4edf-91b9-3f9a0d069c69",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-19 10:50:06"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"b7dc2b45-24e1-4edf-91b9-3f9a0d069c69\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-19 10:50:17"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000405\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-19 10:50:18"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "finRefId": "YD0000405",
                "tranParticular": "Quang tssst",
                "amount": "20000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747595
            },
            "sort": [
                1665747595
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "6c07643d-e6a9-41da-831d-39852f9f9cf5",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "otp_gen",
                "createdAt": "2022-08-16 16:52:42",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "6c07643d-e6a9-41da-831d-39852f9f9cf5",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-16 16:52:42"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "185458",
                    "otpTS": 1660643563
                },
                "tranParticular": "test transfer 100.000 to test account",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747595
            },
            "sort": [
                1665747595
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "a76d0b6a-5d51-454d-a1df-c72aadec2be1",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "otp_gen",
                "createdAt": "2022-08-16 15:09:22",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "a76d0b6a-5d51-454d-a1df-c72aadec2be1",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-16 15:09:22"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "747157",
                    "otpTS": 1660637362
                },
                "tranParticular": "Abc",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747595
            },
            "sort": [
                1665747595
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "90ba8da3-76e3-4be7-ace1-f154a4ebab0e",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-07-14 17:54:42",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "90ba8da3-76e3-4be7-ace1-f154a4ebab0e",
                "accountType": "A",
                "data": {
                    "otp": "766810",
                    "otpTS": 1657796083
                },
                "finRefId": "YD0000072",
                "tranParticular": "Payment for merchant UBank",
                "amount": "1000000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747595
            },
            "sort": [
                1665747595
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "e6ad4c08-8192-4c9a-9396-d3cdc289d59f",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "error",
                "createdAt": "2022-08-10 01:45:27",
                "source": "mop_transfer",
                "toAccount": "000000001493",
                "tranId": "e6ad4c08-8192-4c9a-9396-d3cdc289d59f",
                "logs": {
                    "error": [
                        {
                            "message": "\"{\\\"meta\\\": {\\\"REQUESTUUID\\\": \\\"e67dde7c-16de-4c6f-99e8-81453933caef\\\",\\\"GLOBALUUID\\\": \\\"f6ae1ec2-f621-48ce-bd06-0dff5ebd6509\\\",\\\"contexturl\\\":\\\"\\\"},\\\"errorDetails\\\":[{\\\"errorDesc\\\" :\\\"tranDtl.partTranDetailLL.<rec_0>.userPartTranCode.code - The user part transaction code is invalid. Part Txn. Code: [REFE01]\\\",\\\"errorCode\\\" :\\\"E4221\\\"},{\\\"errorDesc\\\" :\\\"tranDtl.partTranDetailLL.<rec_1>.acctId.foracid - The account has been closed.\\\",\\\"errorCode\\\" :\\\"342\\\"}]}\"",
                            "datetime": "2022-08-10 01:45:38"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-10 01:45:27"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"e6ad4c08-8192-4c9a-9396-d3cdc289d59f\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-10 01:45:36"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "783270",
                    "otpTS": 1660070727
                },
                "tranParticular": "test transfer 100.000 to test account",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747595
            },
            "sort": [
                1665747595
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "c8496aef-84af-47ef-8d9b-d76ae5997328",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-07-14 16:13:41",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "c8496aef-84af-47ef-8d9b-d76ae5997328",
                "accountType": "A",
                "data": {
                    "otp": "808366",
                    "otpTS": 1657790021
                },
                "finRefId": "YD0000067",
                "tranParticular": "test transfer to UBank",
                "amount": "1500000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747595
            },
            "sort": [
                1665747595
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "fb5ba9a7-a5a5-4f52-a3d9-7e6bd3d57000",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "otp_gen",
                "createdAt": "2022-08-16 10:11:45",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "fb5ba9a7-a5a5-4f52-a3d9-7e6bd3d57000",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-16 10:11:45"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "177659",
                    "otpTS": 1660619506
                },
                "tranParticular": "test transfer 100.000 to test account",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747594
            },
            "sort": [
                1665747594
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "ba9f9dbe-b5c7-4ebd-b049-1508c1034be1",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-08 10:32:51",
                "source": "mop_transfer",
                "toAccount": "000000001933",
                "tranId": "ba9f9dbe-b5c7-4ebd-b049-1508c1034be1",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-08 10:32:51"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"ba9f9dbe-b5c7-4ebd-b049-1508c1034be1\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-08 10:32:59"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000197\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-08 10:33:01"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "257301",
                    "otpTS": 1659929571
                },
                "finRefId": "YD0000197",
                "tranParticular": "test transfer 150.000 to test account",
                "amount": "150000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747594
            },
            "sort": [
                1665747594
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "a1080361-d94c-4a1e-a3cc-5e3240b67933",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-18 15:29:02",
                "source": "mop_transfer",
                "toAccount": "000000001491",
                "tranId": "a1080361-d94c-4a1e-a3cc-5e3240b67933",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-18 15:29:02"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"a1080361-d94c-4a1e-a3cc-5e3240b67933\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-18 15:29:30"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000377\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-18 15:29:32"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "finRefId": "YD0000377",
                "tranParticular": "PO000035-I2 VietNam Co.LTD",
                "amount": "253000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747594
            },
            "sort": [
                1665747594
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "b7c52637-8e06-488d-af02-5a2469782bfa",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-16 16:58:46",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "b7c52637-8e06-488d-af02-5a2469782bfa",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-16 16:58:46"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"b7c52637-8e06-488d-af02-5a2469782bfa\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-16 16:58:56"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000296\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-16 16:58:57"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "221781",
                    "otpTS": 1660643926
                },
                "finRefId": "YD0000296",
                "tranParticular": "Abc",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747594
            },
            "sort": [
                1665747594
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "15d7b91e-ccc6-4003-bff1-4c992a6e870a",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-23 12:17:36",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "15d7b91e-ccc6-4003-bff1-4c992a6e870a",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-23 12:17:36"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"15d7b91e-ccc6-4003-bff1-4c992a6e870a\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-23 12:17:47"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000455\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-23 12:17:49"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "finRefId": "YD0000455",
                "tranParticular": "Payment for Quang",
                "amount": "50000",
                "fromAccount": "000000002511",
                "updated_timestamp": 1665747594
            },
            "sort": [
                1665747594
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "e1b4b2dd-b852-426a-ba4e-12445675dbf5",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "error",
                "createdAt": "2022-08-10 09:38:34",
                "source": "mop_transfer",
                "toAccount": "000000001933",
                "tranId": "e1b4b2dd-b852-426a-ba4e-12445675dbf5",
                "logs": {
                    "error": [
                        {
                            "message": "\"{\\\"meta\\\": {\\\"REQUESTUUID\\\": \\\"32389f2f-0233-4759-8aac-84b63db6bbe1\\\",\\\"GLOBALUUID\\\": \\\"d26e9020-1f14-44bd-a36a-e2bcd5c255a7\\\",\\\"contexturl\\\":\\\"\\\"},\\\"errorDetails\\\":[{\\\"errorDesc\\\" :\\\"tranDtl.partTranDetailLL.<rec_0>.userPartTranCode.code - The user part transaction code is invalid. Part Txn. Code: [REFE01]\\\",\\\"errorCode\\\" :\\\"E4221\\\"}]}\"",
                            "datetime": "2022-08-10 09:38:43"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-10 09:38:34"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"e1b4b2dd-b852-426a-ba4e-12445675dbf5\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-10 09:38:42"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "556299",
                    "otpTS": 1660099115
                },
                "tranParticular": "test transfer 100.000 to test account",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747594
            },
            "sort": [
                1665747594
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "d68e70b3-a64b-4032-a93c-8126e88ceb57",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "otp_gen",
                "createdAt": "2022-08-16 15:41:52",
                "source": "mop_transfer",
                "toAccount": "000000001491",
                "tranId": "d68e70b3-a64b-4032-a93c-8126e88ceb57",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-16 15:41:52"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "457813",
                    "otpTS": 1660639312
                },
                "tranParticular": "Abc",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747593
            },
            "sort": [
                1665747593
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "dde63f9b-04a4-42a8-badf-2372b059a732",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-08 09:42:43",
                "source": "mop_transfer",
                "toAccount": "000000001933",
                "tranId": "dde63f9b-04a4-42a8-badf-2372b059a732",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-08 09:42:43"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"dde63f9b-04a4-42a8-badf-2372b059a732\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-08 09:44:47"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000194\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-08 09:44:48"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "490917",
                    "otpTS": 1659926564
                },
                "finRefId": "YD0000194",
                "tranParticular": "test transfer 140.000 to test account",
                "amount": "140000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747593
            },
            "sort": [
                1665747593
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "6716263d-bda3-45e1-a4ca-4d26703c084e",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "otp_gen",
                "createdAt": "2022-08-16 16:47:06",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "6716263d-bda3-45e1-a4ca-4d26703c084e",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-16 16:47:06"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "097633",
                    "otpTS": 1660643226
                },
                "tranParticular": "Abc",
                "amount": "50000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747593
            },
            "sort": [
                1665747593
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "0ac93cba-43f8-4580-bda4-7804d5fd1949",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-19T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-09-07 10:26:36",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "0ac93cba-43f8-4580-bda4-7804d5fd1949",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"9b910c11-f51f-4dc8-8dcc-0baafa28d6fe\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-09-07 10:26:38"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-09-07 10:26:36"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"0ac93cba-43f8-4580-bda4-7804d5fd1949\", \"otp\": \"123456\"}",
                            "datetime": "2022-09-07 10:26:45"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000042\", \"tranDate\": \"2022-12-19T00:00:00.000\"}}",
                            "datetime": "2022-09-07 10:26:46"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "9b910c11-f51f-4dc8-8dcc-0baafa28d6fe"
                },
                "finRefId": "YD0000042",
                "tranParticular": "Test data",
                "amount": "50000",
                "fromAccount": "000000002614",
                "updated_timestamp": 1665747593
            },
            "sort": [
                1665747593
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "ef441bf5-6519-4f77-80c0-c36712958bf3",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "error",
                "createdAt": "2022-09-23 13:48:07",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "ef441bf5-6519-4f77-80c0-c36712958bf3",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"22ead344-f07d-4039-a063-dde78a9ea63b\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-09-23 13:48:10"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-09-23 13:48:07"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"ef441bf5-6519-4f77-80c0-c36712958bf3\", \"otp\": \"123456\"}",
                            "datetime": "2022-09-23 13:48:24"
                        }
                    ],
                    "error": [
                        {
                            "message": "\"{\\\"meta\\\": {\\\"REQUESTUUID\\\": \\\"ce8fffc7-3c64-4cba-8b43-c9da0fe8ae0b\\\",\\\"GLOBALUUID\\\": \\\"7991be07-50dc-4ee7-8609-0fc3a6b9ebfa\\\",\\\"contexturl\\\":\\\"\\\"},\\\"errorDetails\\\":[{\\\"errorDesc\\\" :\\\"Finacle System Error Occurred!!! Please contact System Administrator.\\\",\\\"errorCode\\\" :\\\"4140\\\"}]}\"",
                            "datetime": "2022-09-23 13:48:47"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "22ead344-f07d-4039-a063-dde78a9ea63b"
                },
                "tranParticular": "Test",
                "amount": "50000",
                "fromAccount": "000000002683",
                "updated_timestamp": 1665747593
            },
            "sort": [
                1665747593
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "e7751a64-25d1-4b9c-9e6b-a0fef8e5b394",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "otp_gen",
                "createdAt": "2022-08-24 17:46:52",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "e7751a64-25d1-4b9c-9e6b-a0fef8e5b394",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0348076886\", \"id\": \"836d38e0-fb71-4567-b7b4-e98f2189b47e\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-08-24 17:46:57"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-24 17:46:52"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "836d38e0-fb71-4567-b7b4-e98f2189b47e"
                },
                "tranParticular": "Asdghnn",
                "amount": "10000",
                "fromAccount": "000000002540",
                "updated_timestamp": 1665747593
            },
            "sort": [
                1665747593
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "bf010abb-2f6a-457b-8f6f-191bec587e39",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-18 11:10:47",
                "source": "mop_transfer",
                "toAccount": "000000001491",
                "tranId": "bf010abb-2f6a-457b-8f6f-191bec587e39",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-18 11:10:47"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"bf010abb-2f6a-457b-8f6f-191bec587e39\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-18 11:10:59"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000339\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-18 11:11:00"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "finRefId": "YD0000339",
                "tranParticular": "Thanh toán cho I2 VietNam",
                "amount": "50000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747593
            },
            "sort": [
                1665747593
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "e476ea9f-f2ff-4de6-8f57-e43b28335c85",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "otp_gen",
                "createdAt": "2022-08-24 15:06:47",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "e476ea9f-f2ff-4de6-8f57-e43b28335c85",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-24 15:06:47"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "fff43f07-16da-49f0-a2c9-449c61570a93"
                },
                "tranParticular": "Abcbnn",
                "amount": "10000",
                "fromAccount": "000000002540",
                "updated_timestamp": 1665747593
            },
            "sort": [
                1665747593
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "2874e65c-5539-419c-b06f-e572db5894be",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-18T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-08-18 16:18:21",
                "source": "mop_transfer",
                "toAccount": "000000001491",
                "tranId": "2874e65c-5539-419c-b06f-e572db5894be",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-18 16:18:21"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"2874e65c-5539-419c-b06f-e572db5894be\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-18 16:18:46"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000386\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-18 16:18:48"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "finRefId": "YD0000386",
                "tranParticular": "PO000036-I2 VietNam Co.LTD",
                "amount": "751000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747592
            },
            "sort": [
                1665747592
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "d30fc08f-59e1-47d5-88d5-b3e94c423caf",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-18T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-08-23 23:04:09",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "d30fc08f-59e1-47d5-88d5-b3e94c423caf",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-23 23:04:09"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"d30fc08f-59e1-47d5-88d5-b3e94c423caf\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-23 23:04:20"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000504\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-23 23:04:22"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "finRefId": "YD0000504",
                "tranParticular": "Vâng",
                "amount": "10000",
                "fromAccount": "000000002540",
                "updated_timestamp": 1665747592
            },
            "sort": [
                1665747592
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "28239c1e-8419-4c85-b077-47b03371a4cd",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-05 11:55:27",
                "source": "mop_transfer",
                "toAccount": "000000001933",
                "tranId": "28239c1e-8419-4c85-b077-47b03371a4cd",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-05 11:55:27"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"28239c1e-8419-4c85-b077-47b03371a4cd\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-05 11:55:36"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000192\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-05 11:55:38"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "850083",
                    "otpTS": 1659675327
                },
                "finRefId": "YD0000192",
                "tranParticular": "test transfer 130.000 to test account",
                "amount": "130000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747592
            },
            "sort": [
                1665747592
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "879ea28f-ba44-4c09-b330-fe38d82b29e4",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "otp_gen",
                "createdAt": "2022-08-10 09:13:32",
                "source": "mop_transfer",
                "toAccount": "000000001933",
                "tranId": "879ea28f-ba44-4c09-b330-fe38d82b29e4",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-10 09:13:32"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "071987",
                    "otpTS": 1660097613
                },
                "tranParticular": "test transfer 100.000 to test account",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747592
            },
            "sort": [
                1665747592
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "4a9f7433-32f2-472d-9874-39fb513e8d3d",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-18T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-08-23 22:06:46",
                "source": "mop_transfer",
                "toAccount": "000000001491",
                "tranId": "4a9f7433-32f2-472d-9874-39fb513e8d3d",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-23 22:06:46"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"4a9f7433-32f2-472d-9874-39fb513e8d3d\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-23 22:06:59"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000502\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-23 22:07:00"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "finRefId": "YD0000502",
                "tranParticular": "test transfer to MB bank 7",
                "amount": "50000",
                "fromAccount": "000000002535",
                "updated_timestamp": 1665747592
            },
            "sort": [
                1665747592
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "aaa3580d-0076-4ef2-9d0e-3502297415d4",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "init",
                "createdAt": "2022-09-21 10:19:13",
                "source": "mop_transfer",
                "tranId": "aaa3580d-0076-4ef2-9d0e-3502297415d4",
                "toAccount": "000000001496",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-09-21 10:19:13"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "tranParticular": "Test",
                "amount": "55000",
                "fromAccount": "000000002683",
                "updated_timestamp": 1665747592
            },
            "sort": [
                1665747592
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "3f52cc2c-cd2b-4b24-b003-cd4b0d57d633",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-07-14 16:57:43",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "3f52cc2c-cd2b-4b24-b003-cd4b0d57d633",
                "accountType": "A",
                "data": {
                    "otp": "588431",
                    "otpTS": 1657792663
                },
                "finRefId": "YD0000069",
                "tranParticular": "Payment for merchant UBank",
                "amount": "2500000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747592
            },
            "sort": [
                1665747592
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "09d1c26a-66ed-4d93-9bea-b260e2cd0063",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "error",
                "createdAt": "2022-08-10 01:27:51",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "09d1c26a-66ed-4d93-9bea-b260e2cd0063",
                "logs": {
                    "error": [
                        {
                            "message": "\"{\\\"meta\\\": {\\\"REQUESTUUID\\\": \\\"2b9cec6a-9b32-4364-b710-8d6b3bd681a9\\\",\\\"GLOBALUUID\\\": \\\"7eebb353-939d-480d-82c3-b8d689f8beb3\\\",\\\"contexturl\\\":\\\"\\\"},\\\"errorDetails\\\":[{\\\"errorDesc\\\" :\\\"tranDtl.partTranDetailLL.<rec_0>.userPartTranCode.code - The user part transaction code is invalid. Part Txn. Code: [REFE01]\\\",\\\"errorCode\\\" :\\\"E4221\\\"}]}\"",
                            "datetime": "2022-08-10 01:28:02"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-10 01:27:51"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"09d1c26a-66ed-4d93-9bea-b260e2cd0063\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-10 01:28:01"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "368519",
                    "otpTS": 1660069672
                },
                "tranParticular": "Test new ui",
                "amount": "200000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747591
            },
            "sort": [
                1665747591
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "9cb76064-c82d-44a2-9d37-691c9f0ac3ab",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "otp_gen",
                "createdAt": "2022-08-16 16:29:24",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "9cb76064-c82d-44a2-9d37-691c9f0ac3ab",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-16 16:29:24"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "855967",
                    "otpTS": 1660642165
                },
                "tranParticular": "test transfer 100.000 to test account",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747591
            },
            "sort": [
                1665747591
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "efed5ec5-4554-4275-92be-bd5ff7479c04",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-05 11:30:33",
                "source": "mop_transfer",
                "toAccount": "000000001933",
                "tranId": "efed5ec5-4554-4275-92be-bd5ff7479c04",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-05 11:30:33"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"efed5ec5-4554-4275-92be-bd5ff7479c04\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-05 11:30:48"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000190\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-05 11:30:49"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "719622",
                    "otpTS": 1659673834
                },
                "finRefId": "YD0000190",
                "tranParticular": "test transfer 120.000 to test account",
                "amount": "120000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747591
            },
            "sort": [
                1665747591
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "3f051ece-df4b-47ed-80f5-9a09af54f01c",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-20T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-09-23 13:45:59",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "3f051ece-df4b-47ed-80f5-9a09af54f01c",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0973370149\", \"id\": \"c6829ffa-f0d2-4d74-8ef1-be03c2eee7a2\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-09-23 13:46:02"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-09-23 13:45:59"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"3f051ece-df4b-47ed-80f5-9a09af54f01c\", \"otp\": \"123456\"}",
                            "datetime": "2022-09-23 13:46:14"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000110\", \"tranDate\": \"2022-12-20T00:00:00.000\"}}",
                            "datetime": "2022-09-23 13:46:35"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "c6829ffa-f0d2-4d74-8ef1-be03c2eee7a2"
                },
                "finRefId": "YD0000110",
                "tranParticular": "1111",
                "amount": "100000",
                "fromAccount": "000000002607",
                "updated_timestamp": 1665747591
            },
            "sort": [
                1665747591
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "8b7cb398-0fb1-4fbd-869c-3e2e157e2452",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "otp_gen",
                "createdAt": "2022-08-24 15:13:52",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "8b7cb398-0fb1-4fbd-869c-3e2e157e2452",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-24 15:13:52"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "6f8bef11-caee-4053-87be-f81a5c25f363"
                },
                "tranParticular": "Ubank",
                "amount": "10000",
                "fromAccount": "000000002540",
                "updated_timestamp": 1665747590
            },
            "sort": [
                1665747590
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "167ef53f-f3ac-4963-b4bb-f79b56e5e4ea",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-12 17:37:17",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "167ef53f-f3ac-4963-b4bb-f79b56e5e4ea",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-12 17:37:17"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"167ef53f-f3ac-4963-b4bb-f79b56e5e4ea\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-12 17:37:33"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000283\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-12 17:37:34"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "483872",
                    "otpTS": 1660300638
                },
                "finRefId": "YD0000283",
                "tranParticular": "Abc",
                "amount": "10000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747590
            },
            "sort": [
                1665747590
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "bdd62202-d324-4916-b308-18a6c0e387e0",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-18T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-08-24 15:31:51",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "bdd62202-d324-4916-b308-18a6c0e387e0",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-24 15:31:51"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"bdd62202-d324-4916-b308-18a6c0e387e0\", \"otp\": \"627738\"}",
                            "datetime": "2022-08-24 15:38:49"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000537\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-24 15:38:50"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "6c4209ac-57af-470c-9757-32813399281a"
                },
                "finRefId": "YD0000537",
                "tranParticular": "test transfer to MB bank 7",
                "amount": "50000",
                "fromAccount": "000000002540",
                "updated_timestamp": 1665747590
            },
            "sort": [
                1665747590
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "e81f8edd-4774-4d9a-b140-9afef8f50c0a",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "error",
                "createdAt": "2022-08-10 01:57:36",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "e81f8edd-4774-4d9a-b140-9afef8f50c0a",
                "logs": {
                    "error": [
                        {
                            "message": "\"{\\\"meta\\\": {\\\"REQUESTUUID\\\": \\\"7a84e772-9837-475d-8b19-96a9e335a59a\\\",\\\"GLOBALUUID\\\": \\\"f8713b7c-5093-4864-80f7-e1aebf216e2c\\\",\\\"contexturl\\\":\\\"\\\"},\\\"errorDetails\\\":[{\\\"errorDesc\\\" :\\\"tranDtl.partTranDetailLL.<rec_0>.userPartTranCode.code - The user part transaction code is invalid. Part Txn. Code: [REFE01]\\\",\\\"errorCode\\\" :\\\"E4221\\\"}]}\"",
                            "datetime": "2022-08-10 01:57:45"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-10 01:57:36"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"e81f8edd-4774-4d9a-b140-9afef8f50c0a\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-10 01:57:44"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "956219",
                    "otpTS": 1660071456
                },
                "tranParticular": "test transfer 100.000 to test account",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747590
            },
            "sort": [
                1665747590
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "0cdb839d-dc94-4c74-b9cb-4b756cf9dd18",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-10 18:17:15",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "0cdb839d-dc94-4c74-b9cb-4b756cf9dd18",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-10 18:17:15"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"0cdb839d-dc94-4c74-b9cb-4b756cf9dd18\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-10 18:17:42"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000238\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-10 18:17:44"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "095662",
                    "otpTS": 1660130235
                },
                "finRefId": "YD0000238",
                "tranParticular": "Abc",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747590
            },
            "sort": [
                1665747590
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "a391c139-80a0-4a98-99ed-357b15eeb924",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "otp_verified",
                "createdAt": "2022-08-08 17:32:15",
                "source": "mop_transfer",
                "toAccount": "4002205098117",
                "tranId": "a391c139-80a0-4a98-99ed-357b15eeb924",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-08 17:32:15"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"a391c139-80a0-4a98-99ed-357b15eeb924\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-08 17:32:22"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "495705",
                    "otpTS": 1659954736
                },
                "tranParticular": "PO000076 - Thanh toán",
                "amount": "76000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747590
            },
            "sort": [
                1665747590
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "d2ca2e0c-e671-41d5-858d-911fa9f18feb",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-18T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-08-25 01:57:45",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "d2ca2e0c-e671-41d5-858d-911fa9f18feb",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0348076886\", \"id\": \"f57fce0b-7df9-4708-8fe7-d29118f3ebd8\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-08-25 01:57:47"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-25 01:57:45"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"d2ca2e0c-e671-41d5-858d-911fa9f18feb\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-25 01:57:54"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000575\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-25 01:57:56"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "f57fce0b-7df9-4708-8fe7-d29118f3ebd8"
                },
                "finRefId": "YD0000575",
                "tranParticular": "test transfer to MB bank 8",
                "amount": "10000",
                "fromAccount": "000000002540",
                "updated_timestamp": 1665747590
            },
            "sort": [
                1665747590
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "a995edeb-21a6-4cf2-a142-656ab491de22",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-18 16:33:58",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "a995edeb-21a6-4cf2-a142-656ab491de22",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-18 16:33:58"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"a995edeb-21a6-4cf2-a142-656ab491de22\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-18 16:34:21"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000389\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-18 16:34:23"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "finRefId": "YD0000389",
                "tranParticular": "Abc",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747590
            },
            "sort": [
                1665747590
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "33f390c2-75ce-407f-a999-466d084f110e",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-18T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-08-25 02:23:16",
                "source": "mop_transfer",
                "toAccount": "000000001469",
                "tranId": "33f390c2-75ce-407f-a999-466d084f110e",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0348076886\", \"id\": \"4e53d594-f7ae-4367-b825-a17fbc8b9244\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-08-25 02:23:21"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-25 02:23:16"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"33f390c2-75ce-407f-a999-466d084f110e\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-25 02:23:28"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000577\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-25 02:23:30"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "4e53d594-f7ae-4367-b825-a17fbc8b9244"
                },
                "finRefId": "YD0000577",
                "tranParticular": "Bbb",
                "amount": "10000",
                "fromAccount": "000000002540",
                "updated_timestamp": 1665747589
            },
            "sort": [
                1665747589
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "69f63f63-adc4-4315-8916-8085e95db159",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "init",
                "createdAt": "2022-08-18 17:44:20",
                "source": "mop_transfer",
                "tranId": "69f63f63-adc4-4315-8916-8085e95db159",
                "toAccount": "000000001496",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-18 17:44:20"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "tranParticular": "Abc",
                "amount": "10000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747589
            },
            "sort": [
                1665747589
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "186f8592-f801-4067-a96b-cc522cf36d92",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-18T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-08-25 14:50:30",
                "source": "mop_transfer",
                "toAccount": "000000001497",
                "tranId": "186f8592-f801-4067-a96b-cc522cf36d92",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0348076886\", \"id\": \"ba7d9782-1e16-45ce-987f-a20e962fb44b\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-08-25 14:50:32"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-25 14:50:30"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"186f8592-f801-4067-a96b-cc522cf36d92\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-25 14:50:42"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000603\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-25 14:50:44"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "ba7d9782-1e16-45ce-987f-a20e962fb44b"
                },
                "finRefId": "YD0000603",
                "tranParticular": "Abc",
                "amount": "10000",
                "fromAccount": "000000002540",
                "updated_timestamp": 1665747589
            },
            "sort": [
                1665747589
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "ae297fa5-ac79-48c9-94e1-a2e04d21dc75",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "otp_gen",
                "createdAt": "2022-08-16 14:55:35",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "ae297fa5-ac79-48c9-94e1-a2e04d21dc75",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-16 14:55:35"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "505112",
                    "otpTS": 1660636535
                },
                "tranParticular": "test transfer 100.000 to test account",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747589
            },
            "sort": [
                1665747589
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "2e2fa4a4-15c8-4e43-b842-95b588dc940e",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-18T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-08-25 12:03:50",
                "source": "mop_transfer",
                "toAccount": "000000001497",
                "tranId": "2e2fa4a4-15c8-4e43-b842-95b588dc940e",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0348076886\", \"id\": \"7c3862b5-ac5e-46d1-93d9-f1ed3a62c799\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-08-25 12:03:52"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-25 12:03:50"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"2e2fa4a4-15c8-4e43-b842-95b588dc940e\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-25 12:03:59"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000587\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-25 12:04:01"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "7c3862b5-ac5e-46d1-93d9-f1ed3a62c799"
                },
                "finRefId": "YD0000587",
                "tranParticular": "Cuahanghoa",
                "amount": "10000",
                "fromAccount": "000000002540",
                "updated_timestamp": 1665747589
            },
            "sort": [
                1665747589
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "df990483-dca1-4b54-841e-ae5fb8cf4bbb",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "otp_gen",
                "createdAt": "2022-08-11 17:59:54",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "df990483-dca1-4b54-841e-ae5fb8cf4bbb",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-11 17:59:54"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "460504",
                    "otpTS": 1660215595
                },
                "tranParticular": "Abc",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747589
            },
            "sort": [
                1665747589
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "c8ecb27e-a002-4272-af89-2b4f4eaec117",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-05 09:03:17",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "c8ecb27e-a002-4272-af89-2b4f4eaec117",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-05 09:03:17"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"c8ecb27e-a002-4272-af89-2b4f4eaec117\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-05 09:03:31"
                        },
                        {
                            "message": "{\"tranId\": \"c8ecb27e-a002-4272-af89-2b4f4eaec117\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-05 09:20:47"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000186\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-05 09:20:49"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "197033",
                    "otpTS": 1659664998
                },
                "finRefId": "YD0000186",
                "tranParticular": "test transfer to test account",
                "amount": "1500000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747589
            },
            "sort": [
                1665747589
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "6204bd80-3f60-4b7b-9011-f6623242d206",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-11 18:21:43",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "6204bd80-3f60-4b7b-9011-f6623242d206",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-11 18:21:43"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"6204bd80-3f60-4b7b-9011-f6623242d206\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-11 18:22:12"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000261\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-11 18:22:13"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "895399",
                    "otpTS": 1660216904
                },
                "finRefId": "YD0000261",
                "tranParticular": "Abc",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747588
            },
            "sort": [
                1665747588
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "eedfaa1a-2f68-4f50-bb29-2a2e4a3183e8",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-19 10:51:34",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "eedfaa1a-2f68-4f50-bb29-2a2e4a3183e8",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-19 10:51:34"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"eedfaa1a-2f68-4f50-bb29-2a2e4a3183e8\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-19 10:51:55"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000406\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-19 10:51:56"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "finRefId": "YD0000406",
                "tranParticular": "Abc",
                "amount": "200000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747588
            },
            "sort": [
                1665747588
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "825444cd-1713-422d-9e94-7eabe9b8b6e2",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "init",
                "createdAt": "2022-07-14 09:39:15",
                "source": "mop_transfer",
                "tranId": "825444cd-1713-422d-9e94-7eabe9b8b6e2",
                "toAccount": "000033780214",
                "accountType": "A",
                "data": {},
                "tranParticular": "test transfer to UBank",
                "amount": "1500000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747588
            },
            "sort": [
                1665747588
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "12c558c8-9ce9-4c8a-a586-013381447fd5",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "otp_gen",
                "createdAt": "2022-08-16 15:22:29",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "12c558c8-9ce9-4c8a-a586-013381447fd5",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-16 15:22:29"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "369346",
                    "otpTS": 1660638181
                },
                "tranParticular": "test transfer 100.000 to test account",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747588
            },
            "sort": [
                1665747588
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "486bb639-97db-4b02-a538-61719d48752f",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-19T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-09-07 10:27:21",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "486bb639-97db-4b02-a538-61719d48752f",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"4b401af3-7850-4708-a44c-9c01d3f3a299\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-09-07 10:27:23"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-09-07 10:27:21"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"486bb639-97db-4b02-a538-61719d48752f\", \"otp\": \"123456\"}",
                            "datetime": "2022-09-07 10:27:39"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000043\", \"tranDate\": \"2022-12-19T00:00:00.000\"}}",
                            "datetime": "2022-09-07 10:27:41"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "4b401af3-7850-4708-a44c-9c01d3f3a299"
                },
                "finRefId": "YD0000043",
                "tranParticular": "Test",
                "amount": "25000",
                "fromAccount": "000000002614",
                "updated_timestamp": 1665747588
            },
            "sort": [
                1665747588
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "77730126-7e34-45a5-9437-c7fe7edc20f1",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-20T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-09-21 10:21:27",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "77730126-7e34-45a5-9437-c7fe7edc20f1",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"1329e199-9153-490c-801f-a71c8a813946\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-09-21 10:21:29"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-09-21 10:21:27"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"77730126-7e34-45a5-9437-c7fe7edc20f1\", \"otp\": \"123456\"}",
                            "datetime": "2022-09-21 10:21:45"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000058\", \"tranDate\": \"2022-12-20T00:00:00.000\"}}",
                            "datetime": "2022-09-21 10:22:14"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "1329e199-9153-490c-801f-a71c8a813946"
                },
                "finRefId": "YD0000058",
                "tranParticular": "Test",
                "amount": "55000",
                "fromAccount": "000000002683",
                "updated_timestamp": 1665747588
            },
            "sort": [
                1665747588
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "6b2be8a7-3545-42f6-a91a-a4ef7a32aa7b",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "otp_gen",
                "createdAt": "2022-08-24 18:03:22",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "6b2be8a7-3545-42f6-a91a-a4ef7a32aa7b",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0348076886\", \"id\": \"07940e5e-58b0-44e0-b86d-6e4d75797508\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-08-24 18:03:27"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-24 18:03:22"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "07940e5e-58b0-44e0-b86d-6e4d75797508"
                },
                "tranParticular": "Hggg",
                "amount": "10000",
                "fromAccount": "000000002540",
                "updated_timestamp": 1665747588
            },
            "sort": [
                1665747588
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "fea41d0d-26ee-468d-9075-379e91745d95",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-18T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-08-25 12:00:12",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "fea41d0d-26ee-468d-9075-379e91745d95",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0348076886\", \"id\": \"7d537e4e-04f7-4eda-8a09-2f81044318da\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-08-25 12:00:15"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-25 12:00:12"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"fea41d0d-26ee-468d-9075-379e91745d95\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-25 12:00:25"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000586\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-25 12:00:27"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "7d537e4e-04f7-4eda-8a09-2f81044318da"
                },
                "finRefId": "YD0000586",
                "tranParticular": "Gghhjj",
                "amount": "10000",
                "fromAccount": "000000002540",
                "updated_timestamp": 1665747587
            },
            "sort": [
                1665747587
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "daa99c8f-d9f4-4f1e-a25c-96bd2d16d7aa",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-18T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-08-23 15:13:30",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "daa99c8f-d9f4-4f1e-a25c-96bd2d16d7aa",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-23 15:13:30"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"daa99c8f-d9f4-4f1e-a25c-96bd2d16d7aa\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-23 15:14:00"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000472\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-23 15:14:02"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "finRefId": "YD0000472",
                "tranParticular": "test transfer to MB bank 7",
                "amount": "50000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747587
            },
            "sort": [
                1665747587
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "31e64ce5-1fb4-46c0-829c-aa5940b4802f",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-08 17:51:09",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "31e64ce5-1fb4-46c0-829c-aa5940b4802f",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-08 17:51:09"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"31e64ce5-1fb4-46c0-829c-aa5940b4802f\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-08 17:51:19"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000201\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-08 17:51:20"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "623398",
                    "otpTS": 1659955870
                },
                "finRefId": "YD0000201",
                "tranParticular": "PO000076-thanh toán",
                "amount": "400000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747587
            },
            "sort": [
                1665747587
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "22356f1f-cba4-4968-9dba-fc8de4bad470",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-18 17:41:05",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "22356f1f-cba4-4968-9dba-fc8de4bad470",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-18 17:41:05"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"22356f1f-cba4-4968-9dba-fc8de4bad470\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-18 17:41:21"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000398\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-18 17:41:23"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "finRefId": "YD0000398",
                "tranParticular": "Abc",
                "amount": "10000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747587
            },
            "sort": [
                1665747587
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "feb94050-6fc9-4874-9091-df0517c42a8d",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-18 16:22:50",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "feb94050-6fc9-4874-9091-df0517c42a8d",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-18 16:22:50"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"feb94050-6fc9-4874-9091-df0517c42a8d\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-18 16:23:00"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000387\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-18 16:23:01"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "finRefId": "YD0000387",
                "tranParticular": "Trả 50K",
                "amount": "50000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747587
            },
            "sort": [
                1665747587
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "d3c77e20-d962-4923-b081-d651caa77918",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-18 17:05:28",
                "source": "mop_transfer",
                "toAccount": "000000001491",
                "tranId": "d3c77e20-d962-4923-b081-d651caa77918",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-18 17:05:28"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"d3c77e20-d962-4923-b081-d651caa77918\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-18 17:05:50"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000390\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-18 17:05:51"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {},
                "finRefId": "YD0000390",
                "tranParticular": "Mô tả",
                "amount": "50000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747586
            },
            "sort": [
                1665747586
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "1ac1bc58-2cb7-4b03-be55-5c46555e35e0",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-20T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-09-22 11:30:49",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "1ac1bc58-2cb7-4b03-be55-5c46555e35e0",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0973370149\", \"id\": \"3ec998dc-5694-4a4b-af6b-634823921914\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-09-22 11:30:51"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-09-22 11:30:49"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"1ac1bc58-2cb7-4b03-be55-5c46555e35e0\", \"otp\": \"123456\"}",
                            "datetime": "2022-09-22 11:31:07"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000067\", \"tranDate\": \"2022-12-20T00:00:00.000\"}}",
                            "datetime": "2022-09-22 11:31:31"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "3ec998dc-5694-4a4b-af6b-634823921914"
                },
                "finRefId": "YD0000067",
                "tranParticular": "Test 15k",
                "amount": "15000",
                "fromAccount": "000000002607",
                "updated_timestamp": 1665747585
            },
            "sort": [
                1665747585
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "4ef92559-cbfe-45c1-9571-5b85f219295e",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-16 17:32:02",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "4ef92559-cbfe-45c1-9571-5b85f219295e",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-16 17:32:02"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"4ef92559-cbfe-45c1-9571-5b85f219295e\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-16 17:32:11"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000305\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-16 17:32:14"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "881772",
                    "otpTS": 1660645923
                },
                "finRefId": "YD0000305",
                "tranParticular": "test transfer 100.000 to test account",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747585
            },
            "sort": [
                1665747585
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "2a69b03e-d899-46a7-b96d-254c472c682e",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "init",
                "createdAt": "2022-07-14 10:27:19",
                "source": "mop_transfer",
                "tranId": "2a69b03e-d899-46a7-b96d-254c472c682e",
                "toAccount": "000033780214",
                "accountType": "A",
                "data": {},
                "tranParticular": "test transfer to UBank",
                "amount": "1500000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747584
            },
            "sort": [
                1665747584
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "fb1519b0-c023-47e8-89c3-da26d2f628b2",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "otp_verified",
                "createdAt": "2022-07-14 11:09:23",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "fb1519b0-c023-47e8-89c3-da26d2f628b2",
                "accountType": "A",
                "data": {},
                "tranParticular": "test transfer to UBank",
                "amount": "1500000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747584
            },
            "sort": [
                1665747584
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "7d0b1ace-6ec6-4c48-aa5c-068002a64014",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "otp_gen",
                "createdAt": "2022-08-16 16:57:38",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "7d0b1ace-6ec6-4c48-aa5c-068002a64014",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-16 16:57:38"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "636197",
                    "otpTS": 1660643858
                },
                "tranParticular": "test transfer 100.000 to test account",
                "amount": "100000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747584
            },
            "sort": [
                1665747584
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "d9835239-5a0c-414c-9ee5-939b2dc57954",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-08 17:58:19",
                "source": "mop_transfer",
                "toAccount": "000033780214",
                "tranId": "d9835239-5a0c-414c-9ee5-939b2dc57954",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-08 17:58:19"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"d9835239-5a0c-414c-9ee5-939b2dc57954\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-08 17:58:27"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000203\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-08 17:58:29"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "576568",
                    "otpTS": 1659956299
                },
                "finRefId": "YD0000203",
                "tranParticular": "PO000076 and PO000019",
                "amount": "470000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747584
            },
            "sort": [
                1665747584
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "c765569b-5bd4-405e-a4a1-b2f68d92a5d5",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "finRefDate": "2022-12-20T00:00:00.000",
                "status": "completed",
                "createdAt": "2022-09-20 10:49:08",
                "source": "mop_transfer",
                "toAccount": "000000001496",
                "tranId": "c765569b-5bd4-405e-a4a1-b2f68d92a5d5",
                "logs": {
                    "otp_gen": [
                        {
                            "message": "{\"phone\": \"0522136255\", \"id\": \"543fc351-5502-4470-917e-08c7081704a1\", \"type\": \"mop_transfer\"}",
                            "datetime": "2022-09-20 10:49:11"
                        }
                    ],
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-09-20 10:49:08"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"c765569b-5bd4-405e-a4a1-b2f68d92a5d5\", \"otp\": \"123456\"}",
                            "datetime": "2022-09-20 10:49:25"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000038\", \"tranDate\": \"2022-12-20T00:00:00.000\"}}",
                            "datetime": "2022-09-20 10:49:50"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otpId": "543fc351-5502-4470-917e-08c7081704a1"
                },
                "finRefId": "YD0000038",
                "tranParticular": "Description",
                "amount": "50000",
                "fromAccount": "000000002683",
                "updated_timestamp": 1665747584
            },
            "sort": [
                1665747584
            ]
        },
        {
            "_index": "uat-pop-transaction",
            "_type": "data",
            "_id": "f2a32c5f-656e-4e2e-b110-de55b4eddb70",
            "_score": "",
            "_source": {
                "partnerId": "mybiz",
                "bankCode": "546035",
                "status": "completed",
                "createdAt": "2022-08-08 18:07:46",
                "source": "mop_transfer",
                "toAccount": "000000001933",
                "tranId": "f2a32c5f-656e-4e2e-b110-de55b4eddb70",
                "logs": {
                    "init": [
                        {
                            "message": "Init transaction record",
                            "datetime": "2022-08-08 18:07:46"
                        }
                    ],
                    "otp_verified": [
                        {
                            "message": "{\"tranId\": \"f2a32c5f-656e-4e2e-b110-de55b4eddb70\", \"otp\": \"123456\"}",
                            "datetime": "2022-08-08 18:07:53"
                        }
                    ],
                    "completed": [
                        {
                            "message": "{\"XferTrnAddRs\": {\"tranId\": \"YD0000207\", \"tranDate\": \"2022-12-18T00:00:00.000\"}}",
                            "datetime": "2022-08-08 18:07:54"
                        }
                    ]
                },
                "accountType": "A",
                "extData": {
                    "otp": "071182",
                    "otpTS": 1659956866
                },
                "finRefId": "YD0000207",
                "tranParticular": "Tiền điện tháng 8",
                "amount": "500000",
                "fromAccount": "000000002129",
                "updated_timestamp": 1665747583
            },
            "sort": [
                1665747583
            ]
        }
    ]
    if list_trans:
        try:
            list_export_card = []
            list_export_napas = []
            list_export_merc = []
            for item in list_trans:
                data = item.get('_source', {})
                source = data.get('source', '')
                general_data = {
                    'Transaction ID': data.get('tranId', ''),
                    'Create At': data.get('createdAt', ''),
                    'Transaction Particular': data.get('tranParticular', ''),
                    'From Account': data.get('fromAccount', ''),
                    'Account Type': data.get('accountType', ''),
                    'To Account': data.get('toAccount', ''),
                    'Partner ID': data.get('partnerId', ''),
                    'Bank Code': data.get('bankCode', ''),
                    'Transaction Amount': data.get('amount', ''),
                    'Transaction Status': data.get('status', '')
                }
                if source == 'card_transaction':
                    ext_data = data.get('extData', {})
                    temp_card = {
                        'Transaction Type': 'Card',
                        'Payment TransID': ext_data.get('transaction_id', ''),
                        'Reason': ext_data.get('reason', ''),
                        'Response Code': ext_data.get('response_code', ''),
                        'Payment Amount': ext_data.get('amount', ''),
                        'Merchant Category Code': ext_data.get('merchant_category_code', ''),
                        'Capture Mode': ext_data.get('capture_mode', ''),
                        'Merchant': ext_data.get('merchant', ''),
                        'Payment Type': ext_data.get('type', ''),
                        'Balance': ext_data.get('balance', ''),
                        'Tracking Number': ext_data.get('tracking_number', ''),
                        'Campaign': ext_data.get('campaign', ''),
                        'Terminal ID': ext_data.get('terminal_id', '')
                    }
                    data_export = mergeDictionary(general_data,temp_card)
                    list_export_card.append(data_export)
                elif source == 'mop_transfer':
                    tran_log = data.get('logs', {})
                    log_init = tran_log.get('init', [])
                    log_otp_gen = tran_log.get('otp_gen', [])
                    log_otp_verified = tran_log.get('otp_verified', [])
                    log_completed = tran_log.get('completed', [])
                    init = []
                    opt_gen = []
                    otp_verified = []
                    completed = []
                    if log_init:
                        for item_log in log_init:
                            datetime = item_log.get('datetime', '')
                            init.append(datetime)
                    elif log_otp_gen:
                        for item_log in log_otp_gen:
                            datetime = item_log.get('datetime', '')
                            message = item_log.get('message', '')
                            if message:
                                json_message = json.loads(message)
                                phone = json_message.get('phone', '')
                            else:
                                phone = ''
                            data = {
                                'Phone': phone,
                                'Datetime': datetime
                            }
                            opt_gen.append(data)
                    elif log_otp_verified:
                        for item_log in log_otp_verified:
                            datetime = item_log.get('datetime', '')
                            message = item_log.get('message', '')
                            if message:
                                json_message = json.loads(message)
                                otp = json_message.get('otp', '')
                            else:
                                otp = ''
                            data = {
                                'OTP': otp,
                                'Datetime': datetime
                            }
                            otp_verified.append(data)
                    elif log_completed:
                        for item_log in log_completed:
                            datetime = item_log.get('datetime', '')
                            message = item_log.get('message', '')
                            if message:
                                json_message = json.loads(message)
                                trans_id = json_message.get('XferTrnAddRs', {}).get('tranId', '')
                                trans_date = json_message.get('XferTrnAddRs', {}).get('tranDate', '')
                            else:
                                trans_id = ''
                                trans_date = ''
                            data = {
                                'finTransID': trans_id,
                                'finTransDate': trans_date,
                                'Datetime': datetime
                            }
                            completed.append(data)
                    temp_mer = {
                        'Transaction Type': 'Merchant',
                        'Init': init,
                        'OTP Gen': opt_gen,
                        'OTP Verified': otp_verified,
                        'Completed': completed
                    }
                    print(opt_gen)
                    data_export = mergeDictionary(general_data,temp_mer)
                    list_export_merc.append(data_export)
                else:
                    tran_log = data.get('logs', {})
                    log_init = tran_log.get('init', [])
                    log_process = tran_log.get('process', [])
                    log_completed = tran_log.get('completed', [])
                    init = []
                    process = []
                    completed = []
                    if log_init:
                        for item_log in log_init:
                            datetime = item_log.get('datetime', '')
                            init.append(datetime)
                    elif log_process:
                        for item_log in log_process:
                            datetime = item_log.get('datetime', '')
                            process.append(datetime)
                    elif log_completed:
                        for item_log in log_completed:
                            datetime = item_log.get('datetime', '')
                            message = item_log.get('message', '')
                            if message:
                                json_message = json.loads(message)
                                trans_id = json_message.get('XferTrnAddRs', {}).get('tranId', '')
                                trans_date = json_message.get('XferTrnAddRs', {}).get('tranDate', '')
                            else:
                                trans_id = ''
                                trans_date = ''
                            data = {
                                'finTransID': trans_id,
                                'finTransDate': trans_date,
                                'Datetime': datetime
                            }
                            completed.append(data)
                    temp_napas= {
                        'Transaction Type': 'Napas',
                        'Init': init,
                        'Process': process,
                        'Completed': completed
                    }
                    data_export = mergeDictionary(general_data,temp_napas)
                    list_export_napas.append(data_export)

            # PROCESS IN DATA FOR CSV
            file_name = 'Transaction.xlsx'
            # Create data in each sheet:
            # 1. Card
            df_sheet_1= pd.DataFrame(list_export_card)
            sheet_name_1 = 'Card_Cashin'
            # 2. Merchant
            df_sheet_2 = pd.DataFrame(list_export_merc)
            sheet_name_2 = 'Merchant_Transfer'
            # 3. Napas
            df_sheet_3 = pd.DataFrame(list_export_merc)
            sheet_name_3 = 'Napas_Cashin'
            with pd.ExcelWriter(file_name) as writer:
                df_sheet_1.to_excel(
                    writer,
                    sheet_name=sheet_name_1,
                    index=True,
                    index_label='No.',
                    header=True,
                    freeze_panes=(1, 1)
                )
                df_sheet_2.to_excel(
                    writer,
                    sheet_name=sheet_name_2,
                    index=True,
                    index_label='No.',
                    header=True,
                    freeze_panes=(1, 1)
                )
                df_sheet_3.to_excel(
                    writer,
                    sheet_name=sheet_name_3,
                    index=True,
                    index_label='No.',
                    header=True,
                    freeze_panes=(1, 1)
                )
            with open(file_name, "rb") as file:
                s3_client = boto3.client(
                    's3',
                    region_name='ap-southeast-1',
                    aws_access_key_id='',
                    aws_secret_access_key=''
                )
                bucket_name = ''
                s3_client.upload_fileobj(file, bucket_name, file_name)
                key = file_name
                http_method = 'GET'
                response = s3_client.generate_presigned_url(ClientMethod='get_object',
                                                            HttpMethod=http_method,
                                                            Params={'Bucket': bucket_name, 'Key': key},
                                                            ExpiresIn=1800)
                if len(response):
                    return {
                        'statusCode': 200,
                        'status': True,
                        'presigned_url': response,
                        'message': 'Presigned URL will be expired after 30 mins !'
                    }
                else:
                    return {
                        'statusCode': 400,
                        'status': False,
                        'message': 'Can not get Presigned URL !'
                    }
        except Exception as e:
            print('ERROR===>', e)
            traceback.print_exc()
            return{
                'statusCode': 500,
                'status': 'False',
                'message': 'Internal server error!'
            }
    return {
        'statusCode': 400,
        'status': 'False',
        'message': 'Missing Field!'
    }
