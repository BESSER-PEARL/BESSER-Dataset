





import java.util.List;
import java.util.ArrayList;

public class uml_OccurrenceSpecification extends InteractionFragment {






    private uml_Event uml_event;




    private uml_ExecutionSpecification uml_executionspecification;




    private uml_ExecutionSpecification uml_executionspecification;




    private List<uml_GeneralOrdering> uml_generalorderings;




    private uml_GeneralOrdering uml_generalordering;




    private uml_GeneralOrdering uml_generalordering;




    private List<uml_GeneralOrdering> uml_generalorderings;


    public uml_OccurrenceSpecification(
    ) {
        super(
        );
        this.uml_generalorderings = new ArrayList<>();
        this.uml_generalorderings = new ArrayList<>();
    }

    public uml_OccurrenceSpecification(
        ArrayList<uml_GeneralOrdering> uml_generalorderings,        ArrayList<uml_GeneralOrdering> uml_generalorderings    ) {
        this.uml_generalorderings = uml_generalorderings;
        this.uml_generalorderings = uml_generalorderings;
    }


    public uml_Event getUml_event() {
        return uml_event;
    }

    public void setUml_event(uml_Event uml_event) {
        this.uml_event = uml_event;
    }
    public uml_ExecutionSpecification getUml_executionspecification() {
        return uml_executionspecification;
    }

    public void setUml_executionspecification(uml_ExecutionSpecification uml_executionspecification) {
        this.uml_executionspecification = uml_executionspecification;
    }
    public uml_ExecutionSpecification getUml_executionspecification() {
        return uml_executionspecification;
    }

    public void setUml_executionspecification(uml_ExecutionSpecification uml_executionspecification) {
        this.uml_executionspecification = uml_executionspecification;
    }
    public List<uml_GeneralOrdering> getUml_generalorderings() {
        return uml_generalorderings;
    }

    public void addUml_generalordering(Uml_generalordering uml_generalordering) {
        this.uml_generalorderings.add(uml_generalordering);
    }
    public uml_GeneralOrdering getUml_generalordering() {
        return uml_generalordering;
    }

    public void setUml_generalordering(uml_GeneralOrdering uml_generalordering) {
        this.uml_generalordering = uml_generalordering;
    }
    public uml_GeneralOrdering getUml_generalordering() {
        return uml_generalordering;
    }

    public void setUml_generalordering(uml_GeneralOrdering uml_generalordering) {
        this.uml_generalordering = uml_generalordering;
    }
    public List<uml_GeneralOrdering> getUml_generalorderings() {
        return uml_generalorderings;
    }

    public void addUml_generalordering(Uml_generalordering uml_generalordering) {
        this.uml_generalorderings.add(uml_generalordering);
    }

}