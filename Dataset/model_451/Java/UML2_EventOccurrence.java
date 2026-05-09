





import java.util.List;
import java.util.ArrayList;

public class UML2_EventOccurrence extends InteractionFragment, MessageEnd {






    private UML2_GeneralOrdering uml2_generalordering;




    private List<UML2_GeneralOrdering> uml2_generalorderings;




    private UML2_GeneralOrdering uml2_generalordering;




    private List<UML2_ExecutionOccurrence> uml2_executionoccurrences;




    private List<UML2_GeneralOrdering> uml2_generalorderings;




    private UML2_ExecutionOccurrence uml2_executionoccurrence;




    private UML2_ExecutionOccurrence uml2_executionoccurrence;




    private List<UML2_ExecutionOccurrence> uml2_executionoccurrences;


    public UML2_EventOccurrence(
    ) {
        super(
        );
        this.uml2_generalorderings = new ArrayList<>();
        this.uml2_executionoccurrences = new ArrayList<>();
        this.uml2_generalorderings = new ArrayList<>();
        this.uml2_executionoccurrences = new ArrayList<>();
    }

    public UML2_EventOccurrence(
        ArrayList<UML2_GeneralOrdering> uml2_generalorderings,        ArrayList<UML2_ExecutionOccurrence> uml2_executionoccurrences,        ArrayList<UML2_GeneralOrdering> uml2_generalorderings,        ArrayList<UML2_ExecutionOccurrence> uml2_executionoccurrences    ) {
        this.uml2_generalorderings = uml2_generalorderings;
        this.uml2_executionoccurrences = uml2_executionoccurrences;
        this.uml2_generalorderings = uml2_generalorderings;
        this.uml2_executionoccurrences = uml2_executionoccurrences;
    }


    public UML2_GeneralOrdering getUml2_generalordering() {
        return uml2_generalordering;
    }

    public void setUml2_generalordering(UML2_GeneralOrdering uml2_generalordering) {
        this.uml2_generalordering = uml2_generalordering;
    }
    public List<UML2_GeneralOrdering> getUml2_generalorderings() {
        return uml2_generalorderings;
    }

    public void addUml2_generalordering(Uml2_generalordering uml2_generalordering) {
        this.uml2_generalorderings.add(uml2_generalordering);
    }
    public UML2_GeneralOrdering getUml2_generalordering() {
        return uml2_generalordering;
    }

    public void setUml2_generalordering(UML2_GeneralOrdering uml2_generalordering) {
        this.uml2_generalordering = uml2_generalordering;
    }
    public List<UML2_ExecutionOccurrence> getUml2_executionoccurrences() {
        return uml2_executionoccurrences;
    }

    public void addUml2_executionoccurrence(Uml2_executionoccurrence uml2_executionoccurrence) {
        this.uml2_executionoccurrences.add(uml2_executionoccurrence);
    }
    public List<UML2_GeneralOrdering> getUml2_generalorderings() {
        return uml2_generalorderings;
    }

    public void addUml2_generalordering(Uml2_generalordering uml2_generalordering) {
        this.uml2_generalorderings.add(uml2_generalordering);
    }
    public UML2_ExecutionOccurrence getUml2_executionoccurrence() {
        return uml2_executionoccurrence;
    }

    public void setUml2_executionoccurrence(UML2_ExecutionOccurrence uml2_executionoccurrence) {
        this.uml2_executionoccurrence = uml2_executionoccurrence;
    }
    public UML2_ExecutionOccurrence getUml2_executionoccurrence() {
        return uml2_executionoccurrence;
    }

    public void setUml2_executionoccurrence(UML2_ExecutionOccurrence uml2_executionoccurrence) {
        this.uml2_executionoccurrence = uml2_executionoccurrence;
    }
    public List<UML2_ExecutionOccurrence> getUml2_executionoccurrences() {
        return uml2_executionoccurrences;
    }

    public void addUml2_executionoccurrence(Uml2_executionoccurrence uml2_executionoccurrence) {
        this.uml2_executionoccurrences.add(uml2_executionoccurrence);
    }

}