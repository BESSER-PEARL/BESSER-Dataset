





import java.util.List;
import java.util.ArrayList;

public class qvtcorebase_BottomPattern extends CorePattern {






    private qvtcorebase_Area qvtcorebase_area;




    private List<qvtcorebase_EnforcementOperation> qvtcorebase_enforcementoperations;




    private qvtcorebase_EnforcementOperation qvtcorebase_enforcementoperation;




    private qvtcorebase_Area qvtcorebase_area;




    private List<qvtcorebase_Assignment> qvtcorebase_assignments;




    private qvtcorebase_Assignment qvtcorebase_assignment;


    public qvtcorebase_BottomPattern(
    ) {
        super(
        );
        this.qvtcorebase_enforcementoperations = new ArrayList<>();
        this.qvtcorebase_assignments = new ArrayList<>();
    }

    public qvtcorebase_BottomPattern(
        ArrayList<qvtcorebase_EnforcementOperation> qvtcorebase_enforcementoperations,        ArrayList<qvtcorebase_Assignment> qvtcorebase_assignments    ) {
        this.qvtcorebase_enforcementoperations = qvtcorebase_enforcementoperations;
        this.qvtcorebase_assignments = qvtcorebase_assignments;
    }


    public qvtcorebase_Area getQvtcorebase_area() {
        return qvtcorebase_area;
    }

    public void setQvtcorebase_area(qvtcorebase_Area qvtcorebase_area) {
        this.qvtcorebase_area = qvtcorebase_area;
    }
    public List<qvtcorebase_EnforcementOperation> getQvtcorebase_enforcementoperations() {
        return qvtcorebase_enforcementoperations;
    }

    public void addQvtcorebase_enforcementoperation(Qvtcorebase_enforcementoperation qvtcorebase_enforcementoperation) {
        this.qvtcorebase_enforcementoperations.add(qvtcorebase_enforcementoperation);
    }
    public qvtcorebase_EnforcementOperation getQvtcorebase_enforcementoperation() {
        return qvtcorebase_enforcementoperation;
    }

    public void setQvtcorebase_enforcementoperation(qvtcorebase_EnforcementOperation qvtcorebase_enforcementoperation) {
        this.qvtcorebase_enforcementoperation = qvtcorebase_enforcementoperation;
    }
    public qvtcorebase_Area getQvtcorebase_area() {
        return qvtcorebase_area;
    }

    public void setQvtcorebase_area(qvtcorebase_Area qvtcorebase_area) {
        this.qvtcorebase_area = qvtcorebase_area;
    }
    public List<qvtcorebase_Assignment> getQvtcorebase_assignments() {
        return qvtcorebase_assignments;
    }

    public void addQvtcorebase_assignment(Qvtcorebase_assignment qvtcorebase_assignment) {
        this.qvtcorebase_assignments.add(qvtcorebase_assignment);
    }
    public qvtcorebase_Assignment getQvtcorebase_assignment() {
        return qvtcorebase_assignment;
    }

    public void setQvtcorebase_assignment(qvtcorebase_Assignment qvtcorebase_assignment) {
        this.qvtcorebase_assignment = qvtcorebase_assignment;
    }

}