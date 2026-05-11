





import java.util.List;
import java.util.ArrayList;

public class rdb_DB extends ERDInfo {

    private String url;
    private String id;
    private String comment;
    private String key;
    private String sid;
    private String dbType;



    public rdb_DB(
        String url,        String id,        String comment,        String key,        String sid,        String dbType    ) {
        super(
        );
        this.url = url;
        this.id = id;
        this.comment = comment;
        this.key = key;
        this.sid = sid;
        this.dbType = dbType;
    }


    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getSid() {
        return sid;
    }

    public void setSid(String sid) {
        this.sid = sid;
    }
    public String getDbtype() {
        return dbType;
    }

    public void setDbtype(String dbType) {
        this.dbType = dbType;
    }


}