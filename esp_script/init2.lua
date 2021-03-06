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
        print("conectando em gnmk-admin1")
        wifi.sta.disconnect()
        ssid = "GNMK-ADMIN1"
        psw = "g3n3t1c@g3n0m1k@"
        ip = "172.16.240.90"
        mask = "255.255.255.0"
        gate = "172.16.240.1"
        connect_wifi(ssid, psw, ip, mask, gate)
    elseif (counter==19) then
        print("conectando em gnmk-visitantes")
        wifi.sta.disconnect()
        ssid = "GNMK-VISITANTES"
        psw = "avidaprecisa"
        ip = "192.168.0.120"
        mask = "255.255.255.0"
        gate = "192.168.100.1"
        connect_wifi(ssid, psw, ip, mask, gate)
    end
    if (counter==39) then
        counter = 0
    else
        print(wifi.sta.status())
        counter = counter + 1
        send_request() 
    end

  end)

function connect_wifi(ssid, psw, ip, mask, gate)
    ntwr_name = ssid
    wifi.sta.config(ssid, psw)
    wifi.sta.setip({ip=ip,netmask=mask,gateway=gate})
    wifi.sta.connect()
end
