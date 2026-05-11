





import java.util.List;
import java.util.ArrayList;

public class vcml_Procedure extends Dependency, VCObject {

    private String status;
    private String group;



    public vcml_Procedure(
        String status,        String group    ) {
        super(
        );
        this.status = status;
        this.group = group;
    }


    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }


}