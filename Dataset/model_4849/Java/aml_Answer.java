





import java.util.List;
import java.util.ArrayList;

public class aml_Answer  {

    private String questionId;
    private String group;
    private String rationale;





    private aml_Argument aml_argument;




    private List<aml_Witness> aml_witnesss;




    private List<aml_DiscoveryMethod> aml_discoverymethods;




    private List<aml_Annotation> aml_annotations;




    private List<aml_Belief> aml_beliefs;




    private List<aml_AggregationRule> aml_aggregationrules;


    public aml_Answer(
        String questionId,        String group,        String rationale    ) {
        this.questionId = questionId;
        this.group = group;
        this.rationale = rationale;
        this.aml_witnesss = new ArrayList<>();
        this.aml_discoverymethods = new ArrayList<>();
        this.aml_annotations = new ArrayList<>();
        this.aml_beliefs = new ArrayList<>();
        this.aml_aggregationrules = new ArrayList<>();
    }

    public aml_Answer(
        String questionId,        String group,        String rationale        ArrayList<aml_Witness> aml_witnesss,        ArrayList<aml_DiscoveryMethod> aml_discoverymethods,        ArrayList<aml_Annotation> aml_annotations,        ArrayList<aml_Belief> aml_beliefs,        ArrayList<aml_AggregationRule> aml_aggregationrules    ) {
        this.questionId = questionId;
        this.group = group;
        this.rationale = rationale;
        this.aml_witnesss = aml_witnesss;
        this.aml_discoverymethods = aml_discoverymethods;
        this.aml_annotations = aml_annotations;
        this.aml_beliefs = aml_beliefs;
        this.aml_aggregationrules = aml_aggregationrules;
    }

    public String getQuestionid() {
        return questionId;
    }

    public void setQuestionid(String questionId) {
        this.questionId = questionId;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getRationale() {
        return rationale;
    }

    public void setRationale(String rationale) {
        this.rationale = rationale;
    }

    public aml_Argument getAml_argument() {
        return aml_argument;
    }

    public void setAml_argument(aml_Argument aml_argument) {
        this.aml_argument = aml_argument;
    }
    public List<aml_Witness> getAml_witnesss() {
        return aml_witnesss;
    }

    public void addAml_witness(Aml_witness aml_witness) {
        this.aml_witnesss.add(aml_witness);
    }
    public List<aml_DiscoveryMethod> getAml_discoverymethods() {
        return aml_discoverymethods;
    }

    public void addAml_discoverymethod(Aml_discoverymethod aml_discoverymethod) {
        this.aml_discoverymethods.add(aml_discoverymethod);
    }
    public List<aml_Annotation> getAml_annotations() {
        return aml_annotations;
    }

    public void addAml_annotation(Aml_annotation aml_annotation) {
        this.aml_annotations.add(aml_annotation);
    }
    public List<aml_Belief> getAml_beliefs() {
        return aml_beliefs;
    }

    public void addAml_belief(Aml_belief aml_belief) {
        this.aml_beliefs.add(aml_belief);
    }
    public List<aml_AggregationRule> getAml_aggregationrules() {
        return aml_aggregationrules;
    }

    public void addAml_aggregationrule(Aml_aggregationrule aml_aggregationrule) {
        this.aml_aggregationrules.add(aml_aggregationrule);
    }

}