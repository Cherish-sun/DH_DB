# -*- coding:utf-8 -*-
import os
from app.config import secure
from app.config.setting import PATH


class UserInfo:
    def __init__(self, payload: dict, user_id, user_name):
        self.role = payload.get('role')
        self.user_id = user_id
        self.job_id = payload.get('job_id')
        self.user_name = user_name
        self.db_name = str(self.user_id) + ":" + self.user_name + ":" + str(self.job_id) + ":" + self.role
        self.payload = payload
        self.init_path = secure.FDFS_INIT_PATH
        self.file_list = []
        if all([payload.get('leader_id'), payload.get('leader_name'), payload.get('leader_job_id'),
                payload.get('leader_role')]):
            self.leader_db_name = str(payload.get("leader_id")) + ":" + payload.get('leader_name') + \
                                  ":" + str(payload.get('leader_job_id')) + ":" + str(payload.get('leader_role'))

        else:
            self.leader_db_name = None


    # def start(self):
    #     """
    #
    #     替用户下载好数据
    #     先查MYSQL的路径
    #     然后下载，
    #     然后解压 ,如果下不到，证明客户没有数据。那就让他继续工作就行。这里不能让程序崩溃掉。
    #     下载时候要考虑两点，一个是自己的最后一次文件包，而是有没有别人给报送上来的表，要去查出来
    #     放到自己的草里面。相对应的人机无法，日周月年，都需要放到草里面。做两方面考虑。
    #     :param :
    #     :return:
    #     """
    #
    #     try:
    #
    #         os.mkdir(PATH)
    #         address,port= connection('db')
    #         # address = "127.0.0.1"
    #         # port = 5000
    #         d = {"user_id": self.user_id,"user_name":self.user_name}
    #         resp = requests.post("http://" + str(address) + ":" + str(port) + "/mysql/" + self.db_name + "/excel/find")
    #
    #         path = json.loads(resp.text)
    #
    #         if path :
    #             # path = path.encode()
    #
    #             download_fdfs(path)
    #
    #             File_utils.unzip()
    #             resp = requests.post(
    #                 "http://" + str(address) + ":" + str(port) + "/mysql/" + self.db_name + "/excel/find/submit",
    #                 json=d)
    #
    #             path = json.loads(resp.text)
    #             if path:
    #                 for file in path:
    #                     name = file[0]
    #                     filepath = file[1]
    #                     work_id = file[2]
    #                     date_id = file[3]
    #                     download_fdfs_file(filepath, name, work_id, date_id)
    #             else:
    #                 print("没有上报来的文件，继续工作")
    #         else:
    #             try:
    #
    #                 download_fdfs(self.initpath)
    #                 File_utils.unzip()
    #             except Exception as e:
    #                 print(e)
    #
    #             resp = requests.post(
    #                 "http://" + str(address) + ":" + str(port) + "/mysql/" + self.db_name + "/excel/find/submit",
    #                 json=d)
    #
    #             path = json.loads(resp.text)
    #             if path:
    #                 for file in path:
    #                     name = file[0]
    #                     filepath = file[1]
    #                     work_id = file[2]
    #                     date_id = file[3]
    #                     download_fdfs_file(filepath, name, work_id, date_id)
    #             else:
    #                 print("没有任何文件，已经系统初始化完成")

