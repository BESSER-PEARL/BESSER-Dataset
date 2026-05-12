





import java.util.List;
import java.util.ArrayList;

public class SQL2003_ReferentialConstraint extends TableConstraint {

    private String delete_action;
    private String match;
    private String update_action;





    private SQL2003_UniqueConstraint sql2003_uniqueconstraint;


    public SQL2003_ReferentialConstraint(
        String delete_action,        String match,        String update_action    ) {
        super(
        );
        this.delete_action = delete_action;
        this.match = match;
        this.update_action = update_action;
    }


    public String getDelete_action() {
        return delete_action;
    }

    public void setDelete_action(String delete_action) {
        this.delete_action = delete_action;
    }
    public String getMatch() {
        return match;
    }

    public void setMatch(String match) {
        this.match = match;
    }
    public String getUpdate_action() {
        return update_action;
    }

    public void setUpdate_action(String update_action) {
        this.update_action = update_action;
    }

    public SQL2003_UniqueConstraint getSql2003_uniqueconstraint() {
        return sql2003_uniqueconstraint;
    }

    public void setSql2003_uniqueconstraint(SQL2003_UniqueConstraint sql2003_uniqueconstraint) {
        this.sql2003_uniqueconstraint = sql2003_uniqueconstraint;
    }

}