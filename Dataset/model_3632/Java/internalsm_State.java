





import java.util.List;
import java.util.ArrayList;

public class internalsm_State  {

    private String label;





    private internalsm_Event internalsm_event;




    private List<internalsm_TimeConstraint> internalsm_timeconstraints;


    public internalsm_State(
        String label    ) {
        this.label = label;
        this.internalsm_timeconstraints = new ArrayList<>();
    }

    public internalsm_State(
        String label        ArrayList<internalsm_TimeConstraint> internalsm_timeconstraints    ) {
        this.label = label;
        this.internalsm_timeconstraints = internalsm_timeconstraints;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public internalsm_Event getInternalsm_event() {
        return internalsm_event;
    }

    public void setInternalsm_event(internalsm_Event internalsm_event) {
        this.internalsm_event = internalsm_event;
    }
    public List<internalsm_TimeConstraint> getInternalsm_timeconstraints() {
        return internalsm_timeconstraints;
    }

    public void addInternalsm_timeconstraint(Internalsm_timeconstraint internalsm_timeconstraint) {
        this.internalsm_timeconstraints.add(internalsm_timeconstraint);
    }

}