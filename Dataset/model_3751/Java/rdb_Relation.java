





import java.util.List;
import java.util.ArrayList;

public class rdb_Relation  {

    private String column_name;
    private String constraint_name;
    private String bendpoint;
    private String referenced_column_name;
    private String comment;
    private String target_kind;
    private String source_kind;





    private rdb_Table rdb_table;




    private rdb_DB rdb_db;




    private rdb_Table rdb_table;




    private rdb_Table rdb_table;




    private rdb_DB rdb_db;




    private rdb_Table rdb_table;


    public rdb_Relation(
        String column_name,        String constraint_name,        String bendpoint,        String referenced_column_name,        String comment,        String target_kind,        String source_kind    ) {
        this.column_name = column_name;
        this.constraint_name = constraint_name;
        this.bendpoint = bendpoint;
        this.referenced_column_name = referenced_column_name;
        this.comment = comment;
        this.target_kind = target_kind;
        this.source_kind = source_kind;
    }


    public String getColumn_name() {
        return column_name;
    }

    public void setColumn_name(String column_name) {
        this.column_name = column_name;
    }
    public String getConstraint_name() {
        return constraint_name;
    }

    public void setConstraint_name(String constraint_name) {
        this.constraint_name = constraint_name;
    }
    public String getBendpoint() {
        return bendpoint;
    }

    public void setBendpoint(String bendpoint) {
        this.bendpoint = bendpoint;
    }
    public String getReferenced_column_name() {
        return referenced_column_name;
    }

    public void setReferenced_column_name(String referenced_column_name) {
        this.referenced_column_name = referenced_column_name;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getTarget_kind() {
        return target_kind;
    }

    public void setTarget_kind(String target_kind) {
        this.target_kind = target_kind;
    }
    public String getSource_kind() {
        return source_kind;
    }

    public void setSource_kind(String source_kind) {
        this.source_kind = source_kind;
    }

    public rdb_Table getRdb_table() {
        return rdb_table;
    }

    public void setRdb_table(rdb_Table rdb_table) {
        this.rdb_table = rdb_table;
    }
    public rdb_DB getRdb_db() {
        return rdb_db;
    }

    public void setRdb_db(rdb_DB rdb_db) {
        this.rdb_db = rdb_db;
    }
    public rdb_Table getRdb_table() {
        return rdb_table;
    }

    public void setRdb_table(rdb_Table rdb_table) {
        this.rdb_table = rdb_table;
    }
    public rdb_Table getRdb_table() {
        return rdb_table;
    }

    public void setRdb_table(rdb_Table rdb_table) {
        this.rdb_table = rdb_table;
    }
    public rdb_DB getRdb_db() {
        return rdb_db;
    }

    public void setRdb_db(rdb_DB rdb_db) {
        this.rdb_db = rdb_db;
    }
    public rdb_Table getRdb_table() {
        return rdb_table;
    }

    public void setRdb_table(rdb_Table rdb_table) {
        this.rdb_table = rdb_table;
    }

}