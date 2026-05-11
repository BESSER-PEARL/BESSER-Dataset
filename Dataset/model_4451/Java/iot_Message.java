





import java.util.List;
import java.util.ArrayList;

public class iot_Message  {

    private String msg;
    private String name;





    private iot_IotSystemSpec iot_iotsystemspec;


    public iot_Message(
        String msg,        String name    ) {
        this.msg = msg;
        this.name = name;
    }


    public String getMsg() {
        return msg;
    }

    public void setMsg(String msg) {
        this.msg = msg;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public iot_IotSystemSpec getIot_iotsystemspec() {
        return iot_iotsystemspec;
    }

    public void setIot_iotsystemspec(iot_IotSystemSpec iot_iotsystemspec) {
        this.iot_iotsystemspec = iot_iotsystemspec;
    }

}