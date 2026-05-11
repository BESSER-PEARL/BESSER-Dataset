





import java.util.List;
import java.util.ArrayList;

public class vcml_DependencyNet extends VCObject {

    private String group;
    private String status;





    private List<vcml_Constraint> vcml_constraints;


    public vcml_DependencyNet(
        String group,        String status    ) {
        super(
        );
        this.group = group;
        this.status = status;
        this.vcml_constraints = new ArrayList<>();
    }

    public vcml_DependencyNet(
        String group,        String status        ArrayList<vcml_Constraint> vcml_constraints    ) {
        this.group = group;
        this.status = status;
        this.vcml_constraints = vcml_constraints;
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

    public List<vcml_Constraint> getVcml_constraints() {
        return vcml_constraints;
    }

    public void addVcml_constraint(Vcml_constraint vcml_constraint) {
        this.vcml_constraints.add(vcml_constraint);
    }

}