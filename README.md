# manage-ipset-banip
用flak实现的一个管理服务器IP黑名单的界面


# 准备工作 

```
apt-get install ipset
ipset create banthis hash:net maxelem 1000000
iptables -I INPUT -m set --match-set banthis src -p tcp --destination-port 80 -j DROP
iptables -I INPUT -m set --match-set banthis src -p tcp --destination-port 443 -j DROP
```
