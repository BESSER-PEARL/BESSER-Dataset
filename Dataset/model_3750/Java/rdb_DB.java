





import java.util.List;
import java.util.ArrayList;

public class rdb_DB extends ERDInfo {

    private String sid;
    private String comment;
    private String id;
    private String key;
    private String url;
    private String dbType;





    private List<rdb_Relation> rdb_relations;




    private rdb_Relation rdb_relation;




    private rdb_UserComment rdb_usercomment;




    private rdb_Table rdb_table;




    private rdb_Style rdb_style;




    private List<rdb_Style> rdb_styles;




    private List<rdb_Table> rdb_tables;


    public rdb_DB(
        String sid,        String comment,        String id,        String key,        String url,        String dbType    ) {
        super(
        );
        this.sid = sid;
        this.comment = comment;
        this.id = id;
        this.key = key;
        this.url = url;
        this.dbType = dbType;
        this.rdb_relations = new ArrayList<>();
        this.rdb_styles = new ArrayList<>();
        this.rdb_tables = new ArrayList<>();
    }

    public rdb_DB(
        String sid,        String comment,        String id,        String key,        String url,        String dbType        ArrayList<rdb_Relation> rdb_relations,        ArrayList<rdb_Style> rdb_styles,        ArrayList<rdb_Table> rdb_tables    ) {
        this.sid = sid;
        this.comment = comment;
        this.id = id;
        this.key = key;
        this.url = url;
        this.dbType = dbType;
        this.rdb_relations = rdb_relations;
        this.rdb_styles = rdb_styles;
        this.rdb_tables = rdb_tables;
    }

    public String getSid() {
        return sid;
    }

    public void setSid(String sid) {
        this.sid = sid;
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

    public List<rdb_Relation> getRdb_relations() {
        return rdb_relations;
    }

    public void addRdb_relation(Rdb_relation rdb_relation) {
        this.rdb_relations.add(rdb_relation);
    }
    public rdb_Relation getRdb_relation() {
        return rdb_relation;
    }

    public void setRdb_relation(rdb_Relation rdb_relation) {
        this.rdb_relation = rdb_relation;
    }
    public rdb_UserComment getRdb_usercomment() {
        return rdb_usercomment;
    }

    public void setRdb_usercomment(rdb_UserComment rdb_usercomment) {
        this.rdb_usercomment = rdb_usercomment;
    }
    public rdb_Table getRdb_table() {
        return rdb_table;
    }

    public void setRdb_table(rdb_Table rdb_table) {
        this.rdb_table = rdb_table;
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
    public List<rdb_Table> getRdb_tables() {
        return rdb_tables;
    }

    public void addRdb_table(Rdb_table rdb_table) {
        this.rdb_tables.add(rdb_table);
    }

}