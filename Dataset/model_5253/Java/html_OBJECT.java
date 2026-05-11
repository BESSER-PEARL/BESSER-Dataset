





import java.util.List;
import java.util.ArrayList;

public class html_OBJECT  {

    private String type;
    private String data;
    private String id;
    private String classid;
    private String standby;



    public html_OBJECT(
        String type,        String data,        String id,        String classid,        String standby    ) {
        this.type = type;
        this.data = data;
        this.id = id;
        this.classid = classid;
        this.standby = standby;
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


}