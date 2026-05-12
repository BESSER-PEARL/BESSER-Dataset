





import java.util.List;
import java.util.ArrayList;

public class HTML_OBJECT  {

    private String standby;
    private String classid;
    private String type;
    private String data;
    private String id;



    public HTML_OBJECT(
        String standby,        String classid,        String type,        String data,        String id    ) {
        this.standby = standby;
        this.classid = classid;
        this.type = type;
        this.data = data;
        this.id = id;
    }


    public String getStandby() {
        return standby;
    }

    public void setStandby(String standby) {
        this.standby = standby;
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
    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}