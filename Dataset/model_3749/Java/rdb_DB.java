





import java.util.List;
import java.util.ArrayList;

public class rdb_DB extends ERDInfo {

    private String url;
    private String key;
    private String comment;
    private String id;
    private String sid;
    private String dbType;





    private rdb_UserComment rdb_usercomment;




    private rdb_Style rdb_style;




    private List<rdb_Style> rdb_styles;


    public rdb_DB(
        String url,        String key,        String comment,        String id,        String sid,        String dbType    ) {
        super(
        );
        this.url = url;
        this.key = key;
        this.comment = comment;
        this.id = id;
        this.sid = sid;
        this.dbType = dbType;
        this.rdb_styles = new ArrayList<>();
    }

    public rdb_DB(
        String url,        String key,        String comment,        String id,        String sid,        String dbType        ArrayList<rdb_Style> rdb_styles    ) {
        this.url = url;
        this.key = key;
        this.comment = comment;
        this.id = id;
        this.sid = sid;
        this.dbType = dbType;
        this.rdb_styles = rdb_styles;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
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

    public rdb_UserComment getRdb_usercomment() {
        return rdb_usercomment;
    }

    public void setRdb_usercomment(rdb_UserComment rdb_usercomment) {
        this.rdb_usercomment = rdb_usercomment;
    }
    public rdb_Style getRdb_style() {
        return rdb_style;
    }

    public void setRdb_style(rdb_Style rdb_style) {
        this.rdb_style = rdb_style;
    }
    public List<rdb_Style> getRdb_styles() {
        return rdb_styles;
    }

    public void addRdb_style(Rdb_style rdb_style) {
        this.rdb_styles.add(rdb_style);
    }

}