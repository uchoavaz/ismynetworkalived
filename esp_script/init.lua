counter = 0
ntwr_name = ""
function send_request()
  conn=net.createConnection(net.TCP, 0)
  conn:on("receive", function(conn, payload) print(payload) end)
  conn:connect(8005, "138.197.56.112")
  var="GET /catcher?network_name="..ntwr_name.." HTTP/1.1\r\nHost: 138.197.56.112\r\nConnection: keep-alive\r\nAccept: */*\r\n\r\n"
  conn:send(var)

end

tmr.alarm(0, 10000, 1, function()
    if (counter==0) then
        wifi.sta.disconnect()
        print("conectando em gnmk-lab1")
        ssid = "GNMK-LAB1"
        psw = "sc1m0n3g"
        ip = "172.16.225.25"
        mask = "255.255.255.0"
        gate = "172.16.225.1"
        connect_wifi(ssid, psw, ip, mask, gate)
    elseif (counter==4) then
        print("conectando em gnmk-admin1")
        wifi.sta.disconnect()
        ssid = "GNMK-ADMIN1"
        psw = "g3n3t1c@"
        ip = "172.16.225.26"
        mask = "255.255.255.0"
        gate = "172.16.225.1"
        connect_wifi(ssid, psw, ip, mask, gate)
    elseif (counter==9) then
        print("conectando em gnmk-lab3")
        wifi.sta.disconnect()
        ssid = "GNMK-LAB3"
        psw = "sc1m0n3g"
        ip = "172.16.225.27"
        mask = "255.255.255.0"
        gate = "172.16.225.1"
        connect_wifi(ssid, psw, ip, mask, gate)
    elseif (counter==14) then
        print("conectando em gnmk-visitantes")
        wifi.sta.disconnect()
        ssid = "GNMK-VISITANTES"
        psw = "geneticaparaavida"
        ip = "192.168.100.55"
        mask = "255.255.255.0"
        gate = "192.168.100.1"
        connect_wifi(ssid, psw, ip, mask, gate)
    end
    if (counter==19) then
        counter = 0
    end
    print(wifi.sta.status())
    counter = counter + 1
    send_request()
  end)

function connect_wifi(ssid, psw, ip, mask, gate)
    ntwr_name = ssid
    wifi.sta.config(ssid, psw)
    wifi.sta.setip({ip=ip,netmask=mask,gateway=gate})
    wifi.sta.connect()
end
