





import java.util.List;
import java.util.ArrayList;

public class HTML_OBJECT  {

    private String classid;
    private String standby;
    private String id;
    private String data;
    private String type;



    public HTML_OBJECT(
        String classid,        String standby,        String id,        String data,        String type    ) {
        this.classid = classid;
        this.standby = standby;
        this.id = id;
        this.data = data;
        this.type = type;
    }


    public String getClassid() {
        return classid;
    }

    public void setClassid(String classid) {
        this.classid = classid;
    }
    public String getStandby() {
        return standby;
    }

    public void setStandby(String standby) {
        this.standby = standby;
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
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}