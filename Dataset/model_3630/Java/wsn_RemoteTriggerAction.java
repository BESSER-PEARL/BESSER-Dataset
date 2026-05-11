





import java.util.List;
import java.util.ArrayList;

public class wsn_RemoteTriggerAction extends , Action {

    private int code;
    private String data;



    public wsn_RemoteTriggerAction(
        int code,        String data    ) {
        super(
        );
        this.code = code;
        this.data = data;
    }


    public int getCode() {
        return code;
    }

    public void setCode(int code) {
        this.code = code;
    }
    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }


}