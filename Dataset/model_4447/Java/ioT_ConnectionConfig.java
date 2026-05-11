





import java.util.List;
import java.util.ArrayList;

public class ioT_ConnectionConfig extends Config {

    private String type;





    private ioT_WifiStatement iot_wifistatement;




    private ioT_ConnectStatement iot_connectstatement;


    public ioT_ConnectionConfig(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public ioT_WifiStatement getIot_wifistatement() {
        return iot_wifistatement;
    }

    public void setIot_wifistatement(ioT_WifiStatement iot_wifistatement) {
        this.iot_wifistatement = iot_wifistatement;
    }
    public ioT_ConnectStatement getIot_connectstatement() {
        return iot_connectstatement;
    }

    public void setIot_connectstatement(ioT_ConnectStatement iot_connectstatement) {
        this.iot_connectstatement = iot_connectstatement;
    }

}