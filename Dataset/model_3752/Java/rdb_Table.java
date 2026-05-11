





import java.util.List;
import java.util.ArrayList;

public class rdb_Table  {

    private String logicalName;
    private String comment;
    private String constraints;
    private String name;





    private List<rdb_Column> rdb_columns;




    private rdb_Relation rdb_relation;




    private rdb_Relation rdb_relation;




    private rdb_DB rdb_db;




    private List<rdb_Relation> rdb_relations;




    private rdb_DB rdb_db;




    private rdb_Column rdb_column;




    private List<rdb_Relation> rdb_relations;




    private rdb_UserComment rdb_usercomment;


    public rdb_Table(
        String logicalName,        String comment,        String constraints,        String name    ) {
        this.logicalName = logicalName;
        this.comment = comment;
        this.constraints = constraints;
        this.name = name;
        this.rdb_columns = new ArrayList<>();
        this.rdb_relations = new ArrayList<>();
        this.rdb_relations = new ArrayList<>();
    }

    public rdb_Table(
        String logicalName,        String comment,        String constraints,        String name        ArrayList<rdb_Column> rdb_columns,        ArrayList<rdb_Relation> rdb_relations,        ArrayList<rdb_Relation> rdb_relations    ) {
        this.logicalName = logicalName;
        this.comment = comment;
        this.constraints = constraints;
        this.name = name;
        this.rdb_columns = rdb_columns;
        this.rdb_relations = rdb_relations;
        this.rdb_relations = rdb_relations;
    }

    public String getLogicalname() {
        return logicalName;
    }

    public void setLogicalname(String logicalName) {
        this.logicalName = logicalName;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getConstraints() {
        return constraints;
    }

    public void setConstraints(String constraints) {
        this.constraints = constraints;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<rdb_Column> getRdb_columns() {
        return rdb_columns;
    }

    public void addRdb_column(Rdb_column rdb_column) {
        this.rdb_columns.add(rdb_column);
    }
    public rdb_Relation getRdb_relation() {
        return rdb_relation;
    }

    public void setRdb_relation(rdb_Relation rdb_relation) {
        this.rdb_relation = rdb_relation;
    }
    public rdb_Relation getRdb_relation() {
        return rdb_relation;
    }

    public void setRdb_relation(rdb_Relation rdb_relation) {
        this.rdb_relation = rdb_relation;
    }
    public rdb_DB getRdb_db() {
        return rdb_db;
    }

    public void setRdb_db(rdb_DB rdb_db) {
        this.rdb_db = rdb_db;
    }
    public List<rdb_Relation> getRdb_relations() {
        return rdb_relations;
    }

    public void addRdb_relation(Rdb_relation rdb_relation) {
        this.rdb_relations.add(rdb_relation);
    }
    public rdb_DB getRdb_db() {
        return rdb_db;
    }

    public void setRdb_db(rdb_DB rdb_db) {
        this.rdb_db = rdb_db;
    }
    public rdb_Column getRdb_column() {
        return rdb_column;
    }

    public void setRdb_column(rdb_Column rdb_column) {
        this.rdb_column = rdb_column;
    }
    public List<rdb_Relation> getRdb_relations() {
        return rdb_relations;
    }

    public void addRdb_relation(Rdb_relation rdb_relation) {
        this.rdb_relations.add(rdb_relation);
    }
    public rdb_UserComment getRdb_usercomment() {
        return rdb_usercomment;
    }

    public void setRdb_usercomment(rdb_UserComment rdb_usercomment) {
        this.rdb_usercomment = rdb_usercomment;
    }

}