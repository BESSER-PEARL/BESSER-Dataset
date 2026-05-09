





import java.util.List;
import java.util.ArrayList;

public class eTJ_LeaveDetails  {

    private String type;
    private String name;





    private eTJ_Leaves etj_leaves;


    public eTJ_LeaveDetails(
        String type,        String name    ) {
        this.type = type;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public eTJ_Leaves getEtj_leaves() {
        return etj_leaves;
    }

    public void setEtj_leaves(eTJ_Leaves etj_leaves) {
        this.etj_leaves = etj_leaves;
    }

}