





import java.util.List;
import java.util.ArrayList;

public class UML2_Classifier extends Namespace, RedefinableElement, Type {

    private boolean isAbstract;





    private List<UML2_UseCase> uml2_usecases;




    private List<UML2_UseCase> uml2_usecases;




    private List<UML2_Classifier> uml2_classifiers;




    private List<UML2_CollaborationOccurrence> uml2_collaborationoccurrences;




    private UML2_UseCase uml2_usecase;




    private UML2_ExceptionHandler uml2_exceptionhandler;




    private List<UML2_NamedElement> uml2_namedelements;




    private UML2_RedefinableElement uml2_redefinableelement;




    private List<UML2_Classifier> uml2_classifiers;




    private UML2_Class uml2_class;




    private UML2_CollaborationOccurrence uml2_collaborationoccurrence;


    public UML2_Classifier(
        boolean isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.uml2_usecases = new ArrayList<>();
        this.uml2_usecases = new ArrayList<>();
        this.uml2_classifiers = new ArrayList<>();
        this.uml2_collaborationoccurrences = new ArrayList<>();
        this.uml2_namedelements = new ArrayList<>();
        this.uml2_classifiers = new ArrayList<>();
    }

    public UML2_Classifier(
        boolean isAbstract        ArrayList<UML2_UseCase> uml2_usecases,        ArrayList<UML2_UseCase> uml2_usecases,        ArrayList<UML2_Classifier> uml2_classifiers,        ArrayList<UML2_CollaborationOccurrence> uml2_collaborationoccurrences,        ArrayList<UML2_NamedElement> uml2_namedelements,        ArrayList<UML2_Classifier> uml2_classifiers    ) {
        this.isAbstract = isAbstract;
        this.uml2_usecases = uml2_usecases;
        this.uml2_usecases = uml2_usecases;
        this.uml2_classifiers = uml2_classifiers;
        this.uml2_collaborationoccurrences = uml2_collaborationoccurrences;
        this.uml2_namedelements = uml2_namedelements;
        this.uml2_classifiers = uml2_classifiers;
    }

    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public List<UML2_UseCase> getUml2_usecases() {
        return uml2_usecases;
    }

    public void addUml2_usecase(Uml2_usecase uml2_usecase) {
        this.uml2_usecases.add(uml2_usecase);
    }
    public List<UML2_UseCase> getUml2_usecases() {
        return uml2_usecases;
    }

    public void addUml2_usecase(Uml2_usecase uml2_usecase) {
        this.uml2_usecases.add(uml2_usecase);
    }
    public List<UML2_Classifier> getUml2_classifiers() {
        return uml2_classifiers;
    }

    public void addUml2_classifier(Uml2_classifier uml2_classifier) {
        this.uml2_classifiers.add(uml2_classifier);
    }
    public List<UML2_CollaborationOccurrence> getUml2_collaborationoccurrences() {
        return uml2_collaborationoccurrences;
    }

    public void addUml2_collaborationoccurrence(Uml2_collaborationoccurrence uml2_collaborationoccurrence) {
        this.uml2_collaborationoccurrences.add(uml2_collaborationoccurrence);
    }
    public UML2_UseCase getUml2_usecase() {
        return uml2_usecase;
    }

    public void setUml2_usecase(UML2_UseCase uml2_usecase) {
        this.uml2_usecase = uml2_usecase;
    }
    public UML2_ExceptionHandler getUml2_exceptionhandler() {
        return uml2_exceptionhandler;
    }

    public void setUml2_exceptionhandler(UML2_ExceptionHandler uml2_exceptionhandler) {
        this.uml2_exceptionhandler = uml2_exceptionhandler;
    }
    public List<UML2_NamedElement> getUml2_namedelements() {
        return uml2_namedelements;
    }

    public void addUml2_namedelement(Uml2_namedelement uml2_namedelement) {
        this.uml2_namedelements.add(uml2_namedelement);
    }
    public UML2_RedefinableElement getUml2_redefinableelement() {
        return uml2_redefinableelement;
    }

    public void setUml2_redefinableelement(UML2_RedefinableElement uml2_redefinableelement) {
        this.uml2_redefinableelement = uml2_redefinableelement;
    }
    public List<UML2_Classifier> getUml2_classifiers() {
        return uml2_classifiers;
    }

    public void addUml2_classifier(Uml2_classifier uml2_classifier) {
        this.uml2_classifiers.add(uml2_classifier);
    }
    public UML2_Class getUml2_class() {
        return uml2_class;
    }

    public void setUml2_class(UML2_Class uml2_class) {
        this.uml2_class = uml2_class;
    }
    public UML2_CollaborationOccurrence getUml2_collaborationoccurrence() {
        return uml2_collaborationoccurrence;
    }

    public void setUml2_collaborationoccurrence(UML2_CollaborationOccurrence uml2_collaborationoccurrence) {
        this.uml2_collaborationoccurrence = uml2_collaborationoccurrence;
    }

}