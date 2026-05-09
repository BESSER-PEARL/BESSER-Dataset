





import java.util.List;
import java.util.ArrayList;

public class UML2_Classifier extends RedefinableElement, Namespace, Type {

    private boolean isAbstract;





    private UML2_Class uml2_class;




    private UML2_CreateObjectAction uml2_createobjectaction;




    private UML2_Action uml2_action;




    private List<UML2_CollaborationOccurrence> uml2_collaborationoccurrences;




    private List<UML2_UseCase> uml2_usecases;




    private UML2_ReclassifyObjectAction uml2_reclassifyobjectaction;




    private UML2_ExceptionHandler uml2_exceptionhandler;




    private UML2_ReadExtentAction uml2_readextentaction;




    private List<UML2_Classifier> uml2_classifiers;




    private UML2_Classifier uml2_classifier;




    private UML2_CollaborationOccurrence uml2_collaborationoccurrence;




    private UML2_RedefinableElement uml2_redefinableelement;




    private UML2_Substitution uml2_substitution;




    private UML2_ReadIsClassifiedObjectAction uml2_readisclassifiedobjectaction;




    private List<UML2_Substitution> uml2_substitutions;




    private List<UML2_UseCase> uml2_usecases;




    private List<UML2_NamedElement> uml2_namedelements;




    private UML2_InformationFlow uml2_informationflow;




    private UML2_Substitution uml2_substitution;




    private UML2_Realization uml2_realization;




    private UML2_Interface uml2_interface;




    private UML2_ReclassifyObjectAction uml2_reclassifyobjectaction;




    private UML2_UseCase uml2_usecase;




    private UML2_InformationItem uml2_informationitem;


    public UML2_Classifier(
        boolean isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.uml2_collaborationoccurrences = new ArrayList<>();
        this.uml2_usecases = new ArrayList<>();
        this.uml2_classifiers = new ArrayList<>();
        this.uml2_substitutions = new ArrayList<>();
        this.uml2_usecases = new ArrayList<>();
        this.uml2_namedelements = new ArrayList<>();
    }

    public UML2_Classifier(
        boolean isAbstract        ArrayList<UML2_CollaborationOccurrence> uml2_collaborationoccurrences,        ArrayList<UML2_UseCase> uml2_usecases,        ArrayList<UML2_Classifier> uml2_classifiers,        ArrayList<UML2_Substitution> uml2_substitutions,        ArrayList<UML2_UseCase> uml2_usecases,        ArrayList<UML2_NamedElement> uml2_namedelements    ) {
        this.isAbstract = isAbstract;
        this.uml2_collaborationoccurrences = uml2_collaborationoccurrences;
        this.uml2_usecases = uml2_usecases;
        this.uml2_classifiers = uml2_classifiers;
        this.uml2_substitutions = uml2_substitutions;
        this.uml2_usecases = uml2_usecases;
        this.uml2_namedelements = uml2_namedelements;
    }

    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public UML2_Class getUml2_class() {
        return uml2_class;
    }

    public void setUml2_class(UML2_Class uml2_class) {
        this.uml2_class = uml2_class;
    }
    public UML2_CreateObjectAction getUml2_createobjectaction() {
        return uml2_createobjectaction;
    }

    public void setUml2_createobjectaction(UML2_CreateObjectAction uml2_createobjectaction) {
        this.uml2_createobjectaction = uml2_createobjectaction;
    }
    public UML2_Action getUml2_action() {
        return uml2_action;
    }

    public void setUml2_action(UML2_Action uml2_action) {
        this.uml2_action = uml2_action;
    }
    public List<UML2_CollaborationOccurrence> getUml2_collaborationoccurrences() {
        return uml2_collaborationoccurrences;
    }

    public void addUml2_collaborationoccurrence(Uml2_collaborationoccurrence uml2_collaborationoccurrence) {
        this.uml2_collaborationoccurrences.add(uml2_collaborationoccurrence);
    }
    public List<UML2_UseCase> getUml2_usecases() {
        return uml2_usecases;
    }

    public void addUml2_usecase(Uml2_usecase uml2_usecase) {
        this.uml2_usecases.add(uml2_usecase);
    }
    public UML2_ReclassifyObjectAction getUml2_reclassifyobjectaction() {
        return uml2_reclassifyobjectaction;
    }

    public void setUml2_reclassifyobjectaction(UML2_ReclassifyObjectAction uml2_reclassifyobjectaction) {
        this.uml2_reclassifyobjectaction = uml2_reclassifyobjectaction;
    }
    public UML2_ExceptionHandler getUml2_exceptionhandler() {
        return uml2_exceptionhandler;
    }

    public void setUml2_exceptionhandler(UML2_ExceptionHandler uml2_exceptionhandler) {
        this.uml2_exceptionhandler = uml2_exceptionhandler;
    }
    public UML2_ReadExtentAction getUml2_readextentaction() {
        return uml2_readextentaction;
    }

    public void setUml2_readextentaction(UML2_ReadExtentAction uml2_readextentaction) {
        this.uml2_readextentaction = uml2_readextentaction;
    }
    public List<UML2_Classifier> getUml2_classifiers() {
        return uml2_classifiers;
    }

    public void addUml2_classifier(Uml2_classifier uml2_classifier) {
        this.uml2_classifiers.add(uml2_classifier);
    }
    public UML2_Classifier getUml2_classifier() {
        return uml2_classifier;
    }

    public void setUml2_classifier(UML2_Classifier uml2_classifier) {
        this.uml2_classifier = uml2_classifier;
    }
    public UML2_CollaborationOccurrence getUml2_collaborationoccurrence() {
        return uml2_collaborationoccurrence;
    }

    public void setUml2_collaborationoccurrence(UML2_CollaborationOccurrence uml2_collaborationoccurrence) {
        this.uml2_collaborationoccurrence = uml2_collaborationoccurrence;
    }
    public UML2_RedefinableElement getUml2_redefinableelement() {
        return uml2_redefinableelement;
    }

    public void setUml2_redefinableelement(UML2_RedefinableElement uml2_redefinableelement) {
        this.uml2_redefinableelement = uml2_redefinableelement;
    }
    public UML2_Substitution getUml2_substitution() {
        return uml2_substitution;
    }

    public void setUml2_substitution(UML2_Substitution uml2_substitution) {
        this.uml2_substitution = uml2_substitution;
    }
    public UML2_ReadIsClassifiedObjectAction getUml2_readisclassifiedobjectaction() {
        return uml2_readisclassifiedobjectaction;
    }

    public void setUml2_readisclassifiedobjectaction(UML2_ReadIsClassifiedObjectAction uml2_readisclassifiedobjectaction) {
        this.uml2_readisclassifiedobjectaction = uml2_readisclassifiedobjectaction;
    }
    public List<UML2_Substitution> getUml2_substitutions() {
        return uml2_substitutions;
    }

    public void addUml2_substitution(Uml2_substitution uml2_substitution) {
        this.uml2_substitutions.add(uml2_substitution);
    }
    public List<UML2_UseCase> getUml2_usecases() {
        return uml2_usecases;
    }

    public void addUml2_usecase(Uml2_usecase uml2_usecase) {
        this.uml2_usecases.add(uml2_usecase);
    }
    public List<UML2_NamedElement> getUml2_namedelements() {
        return uml2_namedelements;
    }

    public void addUml2_namedelement(Uml2_namedelement uml2_namedelement) {
        this.uml2_namedelements.add(uml2_namedelement);
    }
    public UML2_InformationFlow getUml2_informationflow() {
        return uml2_informationflow;
    }

    public void setUml2_informationflow(UML2_InformationFlow uml2_informationflow) {
        this.uml2_informationflow = uml2_informationflow;
    }
    public UML2_Substitution getUml2_substitution() {
        return uml2_substitution;
    }

    public void setUml2_substitution(UML2_Substitution uml2_substitution) {
        this.uml2_substitution = uml2_substitution;
    }
    public UML2_Realization getUml2_realization() {
        return uml2_realization;
    }

    public void setUml2_realization(UML2_Realization uml2_realization) {
        this.uml2_realization = uml2_realization;
    }
    public UML2_Interface getUml2_interface() {
        return uml2_interface;
    }

    public void setUml2_interface(UML2_Interface uml2_interface) {
        this.uml2_interface = uml2_interface;
    }
    public UML2_ReclassifyObjectAction getUml2_reclassifyobjectaction() {
        return uml2_reclassifyobjectaction;
    }

    public void setUml2_reclassifyobjectaction(UML2_ReclassifyObjectAction uml2_reclassifyobjectaction) {
        this.uml2_reclassifyobjectaction = uml2_reclassifyobjectaction;
    }
    public UML2_UseCase getUml2_usecase() {
        return uml2_usecase;
    }

    public void setUml2_usecase(UML2_UseCase uml2_usecase) {
        this.uml2_usecase = uml2_usecase;
    }
    public UML2_InformationItem getUml2_informationitem() {
        return uml2_informationitem;
    }

    public void setUml2_informationitem(UML2_InformationItem uml2_informationitem) {
        this.uml2_informationitem = uml2_informationitem;
    }

}