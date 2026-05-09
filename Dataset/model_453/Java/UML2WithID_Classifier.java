





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Classifier extends RedefinableElement, Namespace, Type {

    private boolean isAbstract;





    private UML2WithID_CollaborationOccurrence uml2withid_collaborationoccurrence;




    private List<UML2WithID_CollaborationOccurrence> uml2withid_collaborationoccurrences;




    private List<UML2WithID_NamedElement> uml2withid_namedelements;




    private UML2WithID_Classifier uml2withid_classifier;




    private UML2WithID_RedefinableElement uml2withid_redefinableelement;




    private UML2WithID_ExceptionHandler uml2withid_exceptionhandler;




    private List<UML2WithID_Classifier> uml2withid_classifiers;


    public UML2WithID_Classifier(
        boolean isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.uml2withid_collaborationoccurrences = new ArrayList<>();
        this.uml2withid_namedelements = new ArrayList<>();
        this.uml2withid_classifiers = new ArrayList<>();
    }

    public UML2WithID_Classifier(
        boolean isAbstract        ArrayList<UML2WithID_CollaborationOccurrence> uml2withid_collaborationoccurrences,        ArrayList<UML2WithID_NamedElement> uml2withid_namedelements,        ArrayList<UML2WithID_Classifier> uml2withid_classifiers    ) {
        this.isAbstract = isAbstract;
        this.uml2withid_collaborationoccurrences = uml2withid_collaborationoccurrences;
        this.uml2withid_namedelements = uml2withid_namedelements;
        this.uml2withid_classifiers = uml2withid_classifiers;
    }

    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public UML2WithID_CollaborationOccurrence getUml2withid_collaborationoccurrence() {
        return uml2withid_collaborationoccurrence;
    }

    public void setUml2withid_collaborationoccurrence(UML2WithID_CollaborationOccurrence uml2withid_collaborationoccurrence) {
        this.uml2withid_collaborationoccurrence = uml2withid_collaborationoccurrence;
    }
    public List<UML2WithID_CollaborationOccurrence> getUml2withid_collaborationoccurrences() {
        return uml2withid_collaborationoccurrences;
    }

    public void addUml2withid_collaborationoccurrence(Uml2withid_collaborationoccurrence uml2withid_collaborationoccurrence) {
        this.uml2withid_collaborationoccurrences.add(uml2withid_collaborationoccurrence);
    }
    public List<UML2WithID_NamedElement> getUml2withid_namedelements() {
        return uml2withid_namedelements;
    }

    public void addUml2withid_namedelement(Uml2withid_namedelement uml2withid_namedelement) {
        this.uml2withid_namedelements.add(uml2withid_namedelement);
    }
    public UML2WithID_Classifier getUml2withid_classifier() {
        return uml2withid_classifier;
    }

    public void setUml2withid_classifier(UML2WithID_Classifier uml2withid_classifier) {
        this.uml2withid_classifier = uml2withid_classifier;
    }
    public UML2WithID_RedefinableElement getUml2withid_redefinableelement() {
        return uml2withid_redefinableelement;
    }

    public void setUml2withid_redefinableelement(UML2WithID_RedefinableElement uml2withid_redefinableelement) {
        this.uml2withid_redefinableelement = uml2withid_redefinableelement;
    }
    public UML2WithID_ExceptionHandler getUml2withid_exceptionhandler() {
        return uml2withid_exceptionhandler;
    }

    public void setUml2withid_exceptionhandler(UML2WithID_ExceptionHandler uml2withid_exceptionhandler) {
        this.uml2withid_exceptionhandler = uml2withid_exceptionhandler;
    }
    public List<UML2WithID_Classifier> getUml2withid_classifiers() {
        return uml2withid_classifiers;
    }

    public void addUml2withid_classifier(Uml2withid_classifier uml2withid_classifier) {
        this.uml2withid_classifiers.add(uml2withid_classifier);
    }

}