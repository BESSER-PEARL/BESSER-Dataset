





import java.util.List;
import java.util.ArrayList;

public class iot_BrokerSpec  {

    private int brokerPort;
    private String brokerHost;





    private iot_IotSystemSpec iot_iotsystemspec;


    public iot_BrokerSpec(
        int brokerPort,        String brokerHost    ) {
        this.brokerPort = brokerPort;
        this.brokerHost = brokerHost;
    }


    public int getBrokerport() {
        return brokerPort;
    }

    public void setBrokerport(int brokerPort) {
        this.brokerPort = brokerPort;
    }
    public String getBrokerhost() {
        return brokerHost;
    }

    public void setBrokerhost(String brokerHost) {
        this.brokerHost = brokerHost;
    }

    public iot_IotSystemSpec getIot_iotsystemspec() {
        return iot_iotsystemspec;
    }

    public void setIot_iotsystemspec(iot_IotSystemSpec iot_iotsystemspec) {
        this.iot_iotsystemspec = iot_iotsystemspec;
    }

}