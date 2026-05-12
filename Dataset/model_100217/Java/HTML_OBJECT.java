





import java.util.List;
import java.util.ArrayList;

public class HTML_OBJECT  {

    private String standby;
    private String type;
    private String classid;
    private String id;
    private String data;



    public HTML_OBJECT(
        String standby,        String type,        String classid,        String id,        String data    ) {
        this.standby = standby;
        this.type = type;
        this.classid = classid;
        this.id = id;
        this.data = data;
    }


    public String getStandby() {
        return standby;
    }

    public void setStandby(String standby) {
        this.standby = standby;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getClassid() {
        return classid;
    }

    public void setClassid(String classid) {
        this.classid = classid;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }


}