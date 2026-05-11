





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedInformationFlow extends uml_TracedPackageableElement, uml_TracedDirectedRelationship {






    private List<uml_TracedNamedElement> uml_tracednamedelements;




    private List<uml_TracedNamedElement> uml_tracednamedelements;




    private List<uml_TracedConnector> uml_tracedconnectors;




    private List<uml_TracedMessage> uml_tracedmessages;




    private List<uml_TracedClassifier> uml_tracedclassifiers;




    private List<uml_TracedActivityEdge> uml_tracedactivityedges;


    public umlTrace_uml_TracedInformationFlow(
    ) {
        super(
        );
        this.uml_tracednamedelements = new ArrayList<>();
        this.uml_tracednamedelements = new ArrayList<>();
        this.uml_tracedconnectors = new ArrayList<>();
        this.uml_tracedmessages = new ArrayList<>();
        this.uml_tracedclassifiers = new ArrayList<>();
        this.uml_tracedactivityedges = new ArrayList<>();
    }

    public umlTrace_uml_TracedInformationFlow(
        ArrayList<uml_TracedNamedElement> uml_tracednamedelements,        ArrayList<uml_TracedNamedElement> uml_tracednamedelements,        ArrayList<uml_TracedConnector> uml_tracedconnectors,        ArrayList<uml_TracedMessage> uml_tracedmessages,        ArrayList<uml_TracedClassifier> uml_tracedclassifiers,        ArrayList<uml_TracedActivityEdge> uml_tracedactivityedges    ) {
        this.uml_tracednamedelements = uml_tracednamedelements;
        this.uml_tracednamedelements = uml_tracednamedelements;
        this.uml_tracedconnectors = uml_tracedconnectors;
        this.uml_tracedmessages = uml_tracedmessages;
        this.uml_tracedclassifiers = uml_tracedclassifiers;
        this.uml_tracedactivityedges = uml_tracedactivityedges;
    }


    public List<uml_TracedNamedElement> getUml_tracednamedelements() {
        return uml_tracednamedelements;
    }

    public void addUml_tracednamedelement(Uml_tracednamedelement uml_tracednamedelement) {
        this.uml_tracednamedelements.add(uml_tracednamedelement);
    }
    public List<uml_TracedNamedElement> getUml_tracednamedelements() {
        return uml_tracednamedelements;
    }

    public void addUml_tracednamedelement(Uml_tracednamedelement uml_tracednamedelement) {
        this.uml_tracednamedelements.add(uml_tracednamedelement);
    }
    public List<uml_TracedConnector> getUml_tracedconnectors() {
        return uml_tracedconnectors;
    }

    public void addUml_tracedconnector(Uml_tracedconnector uml_tracedconnector) {
        this.uml_tracedconnectors.add(uml_tracedconnector);
    }
    public List<uml_TracedMessage> getUml_tracedmessages() {
        return uml_tracedmessages;
    }

    public void addUml_tracedmessage(Uml_tracedmessage uml_tracedmessage) {
        this.uml_tracedmessages.add(uml_tracedmessage);
    }
    public List<uml_TracedClassifier> getUml_tracedclassifiers() {
        return uml_tracedclassifiers;
    }

    public void addUml_tracedclassifier(Uml_tracedclassifier uml_tracedclassifier) {
        this.uml_tracedclassifiers.add(uml_tracedclassifier);
    }
    public List<uml_TracedActivityEdge> getUml_tracedactivityedges() {
        return uml_tracedactivityedges;
    }

    public void addUml_tracedactivityedge(Uml_tracedactivityedge uml_tracedactivityedge) {
        this.uml_tracedactivityedges.add(uml_tracedactivityedge);
    }

}