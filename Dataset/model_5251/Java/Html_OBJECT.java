





import java.util.List;
import java.util.ArrayList;

public class Html_OBJECT  {

    private String data;
    private String classid;
    private String type;
    private String standby;



    public Html_OBJECT(
        String data,        String classid,        String type,        String standby    ) {
        this.data = data;
        this.classid = classid;
        this.type = type;
        this.standby = standby;
    }


    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }
    public String getClassid() {
        return classid;
    }

    public void setClassid(String classid) {
        this.classid = classid;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getStandby() {
        return standby;
    }

    public void setStandby(String standby) {
        this.standby = standby;
    }


}