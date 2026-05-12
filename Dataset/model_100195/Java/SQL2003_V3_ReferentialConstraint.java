





import java.util.List;
import java.util.ArrayList;

public class SQL2003_V3_ReferentialConstraint extends TableConstraint {

    private String delete_action;
    private String update_action;
    private String match;





    private SQL2003_V3_UniqueConstraint sql2003_v3_uniqueconstraint;


    public SQL2003_V3_ReferentialConstraint(
        String delete_action,        String update_action,        String match    ) {
        super(
        );
        this.delete_action = delete_action;
        this.update_action = update_action;
        this.match = match;
    }


    public String getDelete_action() {
        return delete_action;
    }

    public void setDelete_action(String delete_action) {
        this.delete_action = delete_action;
    }
    public String getUpdate_action() {
        return update_action;
    }

    public void setUpdate_action(String update_action) {
        this.update_action = update_action;
    }
    public String getMatch() {
        return match;
    }

    public void setMatch(String match) {
        this.match = match;
    }

    public SQL2003_V3_UniqueConstraint getSql2003_v3_uniqueconstraint() {
        return sql2003_v3_uniqueconstraint;
    }

    public void setSql2003_v3_uniqueconstraint(SQL2003_V3_UniqueConstraint sql2003_v3_uniqueconstraint) {
        this.sql2003_v3_uniqueconstraint = sql2003_v3_uniqueconstraint;
    }

}