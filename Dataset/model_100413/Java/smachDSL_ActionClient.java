





import java.util.List;
import java.util.ArrayList;

public class smachDSL_ActionClient  {

    private String actiontype;
    private String name;
    private String actionname;



    public smachDSL_ActionClient(
        String actiontype,        String name,        String actionname    ) {
        this.actiontype = actiontype;
        this.name = name;
        this.actionname = actionname;
    }


    public String getActiontype() {
        return actiontype;
    }

    public void setActiontype(String actiontype) {
        this.actiontype = actiontype;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getActionname() {
        return actionname;
    }

    public void setActionname(String actionname) {
        this.actionname = actionname;
    }


}