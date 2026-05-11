





import java.util.List;
import java.util.ArrayList;

public class rdb_Relation  {

    private String referenced_column_name;
    private String target_kind;
    private String comment;
    private String constraint_name;
    private String source_kind;
    private String bendpoint;
    private String column_name;



    public rdb_Relation(
        String referenced_column_name,        String target_kind,        String comment,        String constraint_name,        String source_kind,        String bendpoint,        String column_name    ) {
        this.referenced_column_name = referenced_column_name;
        this.target_kind = target_kind;
        this.comment = comment;
        this.constraint_name = constraint_name;
        this.source_kind = source_kind;
        this.bendpoint = bendpoint;
        this.column_name = column_name;
    }


    public String getReferenced_column_name() {
        return referenced_column_name;
    }

    public void setReferenced_column_name(String referenced_column_name) {
        this.referenced_column_name = referenced_column_name;
    }
    public String getTarget_kind() {
        return target_kind;
    }

    public void setTarget_kind(String target_kind) {
        this.target_kind = target_kind;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getConstraint_name() {
        return constraint_name;
    }

    public void setConstraint_name(String constraint_name) {
        this.constraint_name = constraint_name;
    }
    public String getSource_kind() {
        return source_kind;
    }

    public void setSource_kind(String source_kind) {
        this.source_kind = source_kind;
    }
    public String getBendpoint() {
        return bendpoint;
    }

    public void setBendpoint(String bendpoint) {
        this.bendpoint = bendpoint;
    }
    public String getColumn_name() {
        return column_name;
    }

    public void setColumn_name(String column_name) {
        this.column_name = column_name;
    }


}