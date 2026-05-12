





import java.util.List;
import java.util.ArrayList;

public class HTML_OBJECT  {

    private String type;
    private String standby;
    private String data;
    private String classid;
    private String id;



    public HTML_OBJECT(
        String type,        String standby,        String data,        String classid,        String id    ) {
        this.type = type;
        this.standby = standby;
        this.data = data;
        this.classid = classid;
        this.id = id;
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
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}