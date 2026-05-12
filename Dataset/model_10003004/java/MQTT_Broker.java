





import java.util.List;
import java.util.ArrayList;

public class MQTT_Broker  {

    private String Subscribe;
    private int DeviceID;
    private String Publish;



    public MQTT_Broker(
        String Subscribe,        int DeviceID,        String Publish    ) {
        this.Subscribe = Subscribe;
        this.DeviceID = DeviceID;
        this.Publish = Publish;
    }


    public String getSubscribe() {
        return Subscribe;
    }

    public void setSubscribe(String Subscribe) {
        this.Subscribe = Subscribe;
    }
    public int getDeviceid() {
        return DeviceID;
    }

    public void setDeviceid(int DeviceID) {
        this.DeviceID = DeviceID;
    }
    public String getPublish() {
        return Publish;
    }

    public void setPublish(String Publish) {
        this.Publish = Publish;
    }


}