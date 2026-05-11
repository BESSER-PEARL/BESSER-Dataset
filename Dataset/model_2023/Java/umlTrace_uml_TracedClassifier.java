





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedClassifier extends uml_TracedType, uml_TracedRedefinableElement, uml_TracedTemplateableElement, uml_TracedNamespace {






    private List<uml_TracedProperty> uml_tracedpropertys;




    private List<uml_TracedClassifier> uml_tracedclassifiers;




    private List<uml_TracedClassifier> uml_tracedclassifiers;




    private List<uml_TracedUseCase> uml_tracedusecases;




    private List<uml_TracedUseCase> uml_tracedusecases;




    private List<uml_TracedSubstitution> uml_tracedsubstitutions;




    private List<uml_TracedGeneralization> uml_tracedgeneralizations;




    private List<uml_TracedNamedElement> uml_tracednamedelements;




    private List<uml_TracedCollaborationUse> uml_tracedcollaborationuses;




    private uml_TracedCollaborationUse uml_tracedcollaborationuse;




    private List<uml_TracedGeneralizationSet> uml_tracedgeneralizationsets;


    public umlTrace_uml_TracedClassifier(
    ) {
        super(
        );
        this.uml_tracedpropertys = new ArrayList<>();
        this.uml_tracedclassifiers = new ArrayList<>();
        this.uml_tracedclassifiers = new ArrayList<>();
        this.uml_tracedusecases = new ArrayList<>();
        this.uml_tracedusecases = new ArrayList<>();
        this.uml_tracedsubstitutions = new ArrayList<>();
        this.uml_tracedgeneralizations = new ArrayList<>();
        this.uml_tracednamedelements = new ArrayList<>();
        this.uml_tracedcollaborationuses = new ArrayList<>();
        this.uml_tracedgeneralizationsets = new ArrayList<>();
    }

    public umlTrace_uml_TracedClassifier(
        ArrayList<uml_TracedProperty> uml_tracedpropertys,        ArrayList<uml_TracedClassifier> uml_tracedclassifiers,        ArrayList<uml_TracedClassifier> uml_tracedclassifiers,        ArrayList<uml_TracedUseCase> uml_tracedusecases,        ArrayList<uml_TracedUseCase> uml_tracedusecases,        ArrayList<uml_TracedSubstitution> uml_tracedsubstitutions,        ArrayList<uml_TracedGeneralization> uml_tracedgeneralizations,        ArrayList<uml_TracedNamedElement> uml_tracednamedelements,        ArrayList<uml_TracedCollaborationUse> uml_tracedcollaborationuses,        ArrayList<uml_TracedGeneralizationSet> uml_tracedgeneralizationsets    ) {
        this.uml_tracedpropertys = uml_tracedpropertys;
        this.uml_tracedclassifiers = uml_tracedclassifiers;
        this.uml_tracedclassifiers = uml_tracedclassifiers;
        this.uml_tracedusecases = uml_tracedusecases;
        this.uml_tracedusecases = uml_tracedusecases;
        this.uml_tracedsubstitutions = uml_tracedsubstitutions;
        this.uml_tracedgeneralizations = uml_tracedgeneralizations;
        this.uml_tracednamedelements = uml_tracednamedelements;
        this.uml_tracedcollaborationuses = uml_tracedcollaborationuses;
        this.uml_tracedgeneralizationsets = uml_tracedgeneralizationsets;
    }


    public List<uml_TracedProperty> getUml_tracedpropertys() {
        return uml_tracedpropertys;
    }

    public void addUml_tracedproperty(Uml_tracedproperty uml_tracedproperty) {
        this.uml_tracedpropertys.add(uml_tracedproperty);
    }
    public List<uml_TracedClassifier> getUml_tracedclassifiers() {
        return uml_tracedclassifiers;
    }

    public void addUml_tracedclassifier(Uml_tracedclassifier uml_tracedclassifier) {
        this.uml_tracedclassifiers.add(uml_tracedclassifier);
    }
    public List<uml_TracedClassifier> getUml_tracedclassifiers() {
        return uml_tracedclassifiers;
    }

    public void addUml_tracedclassifier(Uml_tracedclassifier uml_tracedclassifier) {
        this.uml_tracedclassifiers.add(uml_tracedclassifier);
    }
    public List<uml_TracedUseCase> getUml_tracedusecases() {
        return uml_tracedusecases;
    }

    public void addUml_tracedusecase(Uml_tracedusecase uml_tracedusecase) {
        this.uml_tracedusecases.add(uml_tracedusecase);
    }
    public List<uml_TracedUseCase> getUml_tracedusecases() {
        return uml_tracedusecases;
    }

    public void addUml_tracedusecase(Uml_tracedusecase uml_tracedusecase) {
        this.uml_tracedusecases.add(uml_tracedusecase);
    }
    public List<uml_TracedSubstitution> getUml_tracedsubstitutions() {
        return uml_tracedsubstitutions;
    }

    public void addUml_tracedsubstitution(Uml_tracedsubstitution uml_tracedsubstitution) {
        this.uml_tracedsubstitutions.add(uml_tracedsubstitution);
    }
    public List<uml_TracedGeneralization> getUml_tracedgeneralizations() {
        return uml_tracedgeneralizations;
    }

    public void addUml_tracedgeneralization(Uml_tracedgeneralization uml_tracedgeneralization) {
        this.uml_tracedgeneralizations.add(uml_tracedgeneralization);
    }
    public List<uml_TracedNamedElement> getUml_tracednamedelements() {
        return uml_tracednamedelements;
    }

    public void addUml_tracednamedelement(Uml_tracednamedelement uml_tracednamedelement) {
        this.uml_tracednamedelements.add(uml_tracednamedelement);
    }
    public List<uml_TracedCollaborationUse> getUml_tracedcollaborationuses() {
        return uml_tracedcollaborationuses;
    }

    public void addUml_tracedcollaborationuse(Uml_tracedcollaborationuse uml_tracedcollaborationuse) {
        this.uml_tracedcollaborationuses.add(uml_tracedcollaborationuse);
    }
    public uml_TracedCollaborationUse getUml_tracedcollaborationuse() {
        return uml_tracedcollaborationuse;
    }

    public void setUml_tracedcollaborationuse(uml_TracedCollaborationUse uml_tracedcollaborationuse) {
        this.uml_tracedcollaborationuse = uml_tracedcollaborationuse;
    }
    public List<uml_TracedGeneralizationSet> getUml_tracedgeneralizationsets() {
        return uml_tracedgeneralizationsets;
    }

    public void addUml_tracedgeneralizationset(Uml_tracedgeneralizationset uml_tracedgeneralizationset) {
        this.uml_tracedgeneralizationsets.add(uml_tracedgeneralizationset);
    }

}