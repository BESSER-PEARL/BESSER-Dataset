





import java.util.List;
import java.util.ArrayList;

public class cbpmn_Activity extends FlowNode {

    private String type;





    private List<cbpmn_OCLConstraint> cbpmn_oclconstraints;




    private List<cbpmn_OCLConstraint> cbpmn_oclconstraints;




    private List<cbpmn_OCLConstraint> cbpmn_oclconstraints;




    private List<cbpmn_DataObjectReference> cbpmn_dataobjectreferences;




    private List<cbpmn_DataObjectReference> cbpmn_dataobjectreferences;


    public cbpmn_Activity(
        String type    ) {
        super(
        );
        this.type = type;
        this.cbpmn_oclconstraints = new ArrayList<>();
        this.cbpmn_oclconstraints = new ArrayList<>();
        this.cbpmn_oclconstraints = new ArrayList<>();
        this.cbpmn_dataobjectreferences = new ArrayList<>();
        this.cbpmn_dataobjectreferences = new ArrayList<>();
    }

    public cbpmn_Activity(
        String type        ArrayList<cbpmn_OCLConstraint> cbpmn_oclconstraints,        ArrayList<cbpmn_OCLConstraint> cbpmn_oclconstraints,        ArrayList<cbpmn_OCLConstraint> cbpmn_oclconstraints,        ArrayList<cbpmn_DataObjectReference> cbpmn_dataobjectreferences,        ArrayList<cbpmn_DataObjectReference> cbpmn_dataobjectreferences    ) {
        this.type = type;
        this.cbpmn_oclconstraints = cbpmn_oclconstraints;
        this.cbpmn_oclconstraints = cbpmn_oclconstraints;
        this.cbpmn_oclconstraints = cbpmn_oclconstraints;
        this.cbpmn_dataobjectreferences = cbpmn_dataobjectreferences;
        this.cbpmn_dataobjectreferences = cbpmn_dataobjectreferences;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<cbpmn_OCLConstraint> getCbpmn_oclconstraints() {
        return cbpmn_oclconstraints;
    }

    public void addCbpmn_oclconstraint(Cbpmn_oclconstraint cbpmn_oclconstraint) {
        this.cbpmn_oclconstraints.add(cbpmn_oclconstraint);
    }
    public List<cbpmn_OCLConstraint> getCbpmn_oclconstraints() {
        return cbpmn_oclconstraints;
    }

    public void addCbpmn_oclconstraint(Cbpmn_oclconstraint cbpmn_oclconstraint) {
        this.cbpmn_oclconstraints.add(cbpmn_oclconstraint);
    }
    public List<cbpmn_OCLConstraint> getCbpmn_oclconstraints() {
        return cbpmn_oclconstraints;
    }

    public void addCbpmn_oclconstraint(Cbpmn_oclconstraint cbpmn_oclconstraint) {
        this.cbpmn_oclconstraints.add(cbpmn_oclconstraint);
    }
    public List<cbpmn_DataObjectReference> getCbpmn_dataobjectreferences() {
        return cbpmn_dataobjectreferences;
    }

    public void addCbpmn_dataobjectreference(Cbpmn_dataobjectreference cbpmn_dataobjectreference) {
        this.cbpmn_dataobjectreferences.add(cbpmn_dataobjectreference);
    }
    public List<cbpmn_DataObjectReference> getCbpmn_dataobjectreferences() {
        return cbpmn_dataobjectreferences;
    }

    public void addCbpmn_dataobjectreference(Cbpmn_dataobjectreference cbpmn_dataobjectreference) {
        this.cbpmn_dataobjectreferences.add(cbpmn_dataobjectreference);
    }

}