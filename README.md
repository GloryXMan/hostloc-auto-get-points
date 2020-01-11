# Hostloc Auto Get Points
使用 GitHub Actions 自动获取 Hostloc 论坛积分

## 使用说明

Fork 本仓库，然后点击你的仓库右上角的 Settings，找到 Secrets 这一项，添加两个秘密环境变量。

![VIAs.png](https://img.xirikm.net/images/VIAs.png)

其中 `HOSTLOC_USERNAME` 是你在 Hostloc 的帐户名，`HOSTLOC_PASSWORD` 是你的帐户密码。

设置好环境变量后点击你的仓库上方的 Actions 选项，会打开一个如下的页面，点击 `I understand...` 按钮确认在 Fork 的仓库上启用 Github Actions 。

![VZ5E.png](https://img.xirikm.net/images/VZ5E.png)

最后在你这个 Fork 的仓库内随便改点什么（比如给 README 文件删掉几个字符）手动触发一次 Github Actions **（重要！！！测试发现 Fork 的仓库上 Github Actions 的定时任务不会自动执行，必须要手动触发一次后才能正常工作）** 。

仓库内包含的 GitHub Actions 脚本每天会在国际标准时间 17 点（北京时间凌晨 1 点）自动执行，你也可以通过 `Push` 操作手动触发 **（测试发现定时任务的执行可能有 5 到 10 分钟的延迟，属正常现象，耐心等待即可）** 。
