





import java.util.List;
import java.util.ArrayList;

public class vcml_SelectionCondition extends Dependency, VCObject {

    private String group;
    private String status;



    public vcml_SelectionCondition(
        String group,        String status    ) {
        super(
        );
        this.group = group;
        this.status = status;
    }


    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }


}