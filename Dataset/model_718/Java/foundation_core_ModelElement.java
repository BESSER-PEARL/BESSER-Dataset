





import java.util.List;
import java.util.ArrayList;

public class foundation_core_ModelElement extends Element {

    private String visibility;
    private String isSpecification;
    private String name;





    private List<TaggedValue> taggedvalues;




    private List<TemplateParameter> templateparameters;




    private List<Stereotype> stereotypes;




    private List<StateMachine> statemachines;




    private List<TaggedValue> taggedvalues;




    private List<ElementResidence> elementresidences;


    public foundation_core_ModelElement(
        String visibility,        String isSpecification,        String name    ) {
        super(
        );
        this.visibility = visibility;
        this.isSpecification = isSpecification;
        this.name = name;
        this.taggedvalues = new ArrayList<>();
        this.templateparameters = new ArrayList<>();
        this.stereotypes = new ArrayList<>();
        this.statemachines = new ArrayList<>();
        this.taggedvalues = new ArrayList<>();
        this.elementresidences = new ArrayList<>();
    }

    public foundation_core_ModelElement(
        String visibility,        String isSpecification,        String name        ArrayList<TaggedValue> taggedvalues,        ArrayList<TemplateParameter> templateparameters,        ArrayList<Stereotype> stereotypes,        ArrayList<StateMachine> statemachines,        ArrayList<TaggedValue> taggedvalues,        ArrayList<ElementResidence> elementresidences    ) {
        this.visibility = visibility;
        this.isSpecification = isSpecification;
        this.name = name;
        this.taggedvalues = taggedvalues;
        this.templateparameters = templateparameters;
        this.stereotypes = stereotypes;
        this.statemachines = statemachines;
        this.taggedvalues = taggedvalues;
        this.elementresidences = elementresidences;
    }

    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public String getIsspecification() {
        return isSpecification;
    }

    public void setIsspecification(String isSpecification) {
        this.isSpecification = isSpecification;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<TaggedValue> getTaggedvalues() {
        return taggedvalues;
    }

    public void addTaggedvalue(Taggedvalue taggedvalue) {
        this.taggedvalues.add(taggedvalue);
    }
    public List<TemplateParameter> getTemplateparameters() {
        return templateparameters;
    }

    public void addTemplateparameter(Templateparameter templateparameter) {
        this.templateparameters.add(templateparameter);
    }
    public List<Stereotype> getStereotypes() {
        return stereotypes;
    }

    public void addStereotype(Stereotype stereotype) {
        this.stereotypes.add(stereotype);
    }
    public List<StateMachine> getStatemachines() {
        return statemachines;
    }

    public void addStatemachine(Statemachine statemachine) {
        this.statemachines.add(statemachine);
    }
    public List<TaggedValue> getTaggedvalues() {
        return taggedvalues;
    }

    public void addTaggedvalue(Taggedvalue taggedvalue) {
        this.taggedvalues.add(taggedvalue);
    }
    public List<ElementResidence> getElementresidences() {
        return elementresidences;
    }

    public void addElementresidence(Elementresidence elementresidence) {
        this.elementresidences.add(elementresidence);
    }

}