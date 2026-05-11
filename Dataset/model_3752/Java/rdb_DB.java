





import java.util.List;
import java.util.ArrayList;

public class rdb_DB extends ERDInfo {

    private String comment;
    private String sid;
    private String id;
    private String key;
    private String url;
    private String dbType;





    private rdb_Relation rdb_relation;




    private List<rdb_Relation> rdb_relations;


    public rdb_DB(
        String comment,        String sid,        String id,        String key,        String url,        String dbType    ) {
        super(
        );
        this.comment = comment;
        this.sid = sid;
        this.id = id;
        this.key = key;
        this.url = url;
        this.dbType = dbType;
        this.rdb_relations = new ArrayList<>();
    }

    public rdb_DB(
        String comment,        String sid,        String id,        String key,        String url,        String dbType        ArrayList<rdb_Relation> rdb_relations    ) {
        this.comment = comment;
        this.sid = sid;
        this.id = id;
        this.key = key;
        this.url = url;
        this.dbType = dbType;
        this.rdb_relations = rdb_relations;
    }

    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getSid() {
        return sid;
    }

    public void setSid(String sid) {
        this.sid = sid;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public String getDbtype() {
        return dbType;
    }

    public void setDbtype(String dbType) {
        this.dbType = dbType;
    }

    public rdb_Relation getRdb_relation() {
        return rdb_relation;
    }

    public void setRdb_relation(rdb_Relation rdb_relation) {
        this.rdb_relation = rdb_relation;
    }
    public List<rdb_Relation> getRdb_relations() {
        return rdb_relations;
    }

    public void addRdb_relation(Rdb_relation rdb_relation) {
        this.rdb_relations.add(rdb_relation);
    }

}