from Chaoxing import Chaoxing
import os

# 你的Cookie信息
# 具体说明看文档
# cookies = "lv=1; fid=4049; _uid=152846892; uf=d9387224d3a6095b0e7ca8b539ad0c44f4089cc71f3a742f9b3e2793c64ba24dcba3c0868c3c246ec8395ccad96cd6ab913b662843f1f4ad6d92e371d7fdf644a53aa4ed5606e4fe22d37f0ce2a6151df36a78989c03308d3dd1dbd6d890c658bac5cbf60a93febf; _d=1636454492536; UID=152846892; vc=67F2DA8360ED46FE0FC16D2F155AF77C; vc2=7A3E634CBF243F8C14DEC3276B885082; vc3=ZZVkT1ox7FgDxTU5uOe%2F%2B2dhEVQovyF3wjAqgeTNVmWlOnRBCp2ngenCJs0X4LnZItcTUV5Oe0afKbpM04t5XXusMmUSizPNHf%2F4J3rb1ajU7fo4i5DNEYpX1Wm%2FhGxsTV5VlrsbqD9gg4mzLabfVLlFEgYI8RxqwP%2FXf2Ky%2Fkc%3D6027d6afd17e3c1dfb43f27fd3378aa8; xxtenc=afd2b5e71db2014ef2d92c81a9e24bd5; DSSTASH_LOG=C_38-UN_3119-US_152846892-T_1636454492538; k8s=0e591ffe0b44b93157cf7fd182ff28998dfcab05; jrose=010F8FEDC6A2AEDA23A8445B339C57D7.mooc-3230766634-b0rff; route=2fe558bdb0a1aea656e6ca70ad0cad20"
cookies = os.environ.get("COOKIE")
# ClassID
# classid = "43898759"
classid = os.environ.get("CLASSID")
# CourseID
# courseid = "217783959"
courseid = os.environ.get("COURSEID")
# 请求间隔时间,根据需要更改,单位:秒
# sleep_time = 0.5
sleep_time = float(os.environ.get("SLEEP_TIME"))
# 程序总执行时长,单位:分钟
# pass_time = 10
pass_time = float(os.environ.get("PASS_TIME"))
# 下面无需修改
cx = Chaoxing(cookies, classid, courseid, sleep_time, pass_time)
cx.run()
