





import java.util.List;
import java.util.ArrayList;

public class aml_Evidence  {

    private String ordinal;
    private String id;
    private String label;





    private aml_Witness aml_witness;




    private aml_Answer aml_answer;




    private List<aml_Annotation> aml_annotations;


    public aml_Evidence(
        String ordinal,        String id,        String label    ) {
        this.ordinal = ordinal;
        this.id = id;
        this.label = label;
        this.aml_annotations = new ArrayList<>();
    }

    public aml_Evidence(
        String ordinal,        String id,        String label        ArrayList<aml_Annotation> aml_annotations    ) {
        this.ordinal = ordinal;
        this.id = id;
        this.label = label;
        this.aml_annotations = aml_annotations;
    }

    public String getOrdinal() {
        return ordinal;
    }

    public void setOrdinal(String ordinal) {
        this.ordinal = ordinal;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public aml_Witness getAml_witness() {
        return aml_witness;
    }

    public void setAml_witness(aml_Witness aml_witness) {
        this.aml_witness = aml_witness;
    }
    public aml_Answer getAml_answer() {
        return aml_answer;
    }

    public void setAml_answer(aml_Answer aml_answer) {
        this.aml_answer = aml_answer;
    }
    public List<aml_Annotation> getAml_annotations() {
        return aml_annotations;
    }

    public void addAml_annotation(Aml_annotation aml_annotation) {
        this.aml_annotations.add(aml_annotation);
    }

}