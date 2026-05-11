





import java.util.List;
import java.util.ArrayList;

public class aml_Question  {

    private String group;
    private String description;
    private String id;
    private String amplification;
    private String label;





    private aml_Collection aml_collection;




    private List<aml_DiscoveryMethod> aml_discoverymethods;




    private List<aml_EObject> aml_eobjects;




    private List<aml_AggregationRule> aml_aggregationrules;




    private List<aml_Annotation> aml_annotations;




    private aml_Template aml_template;




    private List<aml_Choice> aml_choices;


    public aml_Question(
        String group,        String description,        String id,        String amplification,        String label    ) {
        this.group = group;
        this.description = description;
        this.id = id;
        this.amplification = amplification;
        this.label = label;
        this.aml_discoverymethods = new ArrayList<>();
        this.aml_eobjects = new ArrayList<>();
        this.aml_aggregationrules = new ArrayList<>();
        this.aml_annotations = new ArrayList<>();
        this.aml_choices = new ArrayList<>();
    }

    public aml_Question(
        String group,        String description,        String id,        String amplification,        String label        ArrayList<aml_DiscoveryMethod> aml_discoverymethods,        ArrayList<aml_EObject> aml_eobjects,        ArrayList<aml_AggregationRule> aml_aggregationrules,        ArrayList<aml_Annotation> aml_annotations,        ArrayList<aml_Choice> aml_choices    ) {
        this.group = group;
        this.description = description;
        this.id = id;
        this.amplification = amplification;
        this.label = label;
        this.aml_discoverymethods = aml_discoverymethods;
        this.aml_eobjects = aml_eobjects;
        this.aml_aggregationrules = aml_aggregationrules;
        this.aml_annotations = aml_annotations;
        this.aml_choices = aml_choices;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getAmplification() {
        return amplification;
    }

    public void setAmplification(String amplification) {
        this.amplification = amplification;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public aml_Collection getAml_collection() {
        return aml_collection;
    }

    public void setAml_collection(aml_Collection aml_collection) {
        this.aml_collection = aml_collection;
    }
    public List<aml_DiscoveryMethod> getAml_discoverymethods() {
        return aml_discoverymethods;
    }

    public void addAml_discoverymethod(Aml_discoverymethod aml_discoverymethod) {
        this.aml_discoverymethods.add(aml_discoverymethod);
    }
    public List<aml_EObject> getAml_eobjects() {
        return aml_eobjects;
    }

    public void addAml_eobject(Aml_eobject aml_eobject) {
        this.aml_eobjects.add(aml_eobject);
    }
    public List<aml_AggregationRule> getAml_aggregationrules() {
        return aml_aggregationrules;
    }

    public void addAml_aggregationrule(Aml_aggregationrule aml_aggregationrule) {
        this.aml_aggregationrules.add(aml_aggregationrule);
    }
    public List<aml_Annotation> getAml_annotations() {
        return aml_annotations;
    }

    public void addAml_annotation(Aml_annotation aml_annotation) {
        this.aml_annotations.add(aml_annotation);
    }
    public aml_Template getAml_template() {
        return aml_template;
    }

    public void setAml_template(aml_Template aml_template) {
        this.aml_template = aml_template;
    }
    public List<aml_Choice> getAml_choices() {
        return aml_choices;
    }

    public void addAml_choice(Aml_choice aml_choice) {
        this.aml_choices.add(aml_choice);
    }

}