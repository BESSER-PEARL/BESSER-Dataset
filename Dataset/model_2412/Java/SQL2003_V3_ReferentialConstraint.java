





import java.util.List;
import java.util.ArrayList;

public class SQL2003_V3_ReferentialConstraint extends TableConstraint {

    private String match;
    private String update_action;
    private String delete_action;



    public SQL2003_V3_ReferentialConstraint(
        String match,        String update_action,        String delete_action    ) {
        super(
        );
        this.match = match;
        this.update_action = update_action;
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
    public String getDelete_action() {
        return delete_action;
    }

    public void setDelete_action(String delete_action) {
        this.delete_action = delete_action;
    }


}