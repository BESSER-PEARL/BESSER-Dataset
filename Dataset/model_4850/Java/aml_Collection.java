





import java.util.List;
import java.util.ArrayList;

public class aml_Collection  {

    private String objectType;
    private String id;
    private String group;
    private String label1;
    private String label;





    private List<aml_Annotation> aml_annotations;




    private aml_AmlDocument aml_amldocument;


    public aml_Collection(
        String objectType,        String id,        String group,        String label1,        String label    ) {
        this.objectType = objectType;
        this.id = id;
        this.group = group;
        this.label1 = label1;
        this.label = label;
        this.aml_annotations = new ArrayList<>();
    }

    public aml_Collection(
        String objectType,        String id,        String group,        String label1,        String label        ArrayList<aml_Annotation> aml_annotations    ) {
        this.objectType = objectType;
        this.id = id;
        this.group = group;
        this.label1 = label1;
        this.label = label;
        this.aml_annotations = aml_annotations;
    }

    public String getObjecttype() {
        return objectType;
    }

    public void setObjecttype(String objectType) {
        this.objectType = objectType;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getLabel1() {
        return label1;
    }

    public void setLabel1(String label1) {
        this.label1 = label1;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public List<aml_Annotation> getAml_annotations() {
        return aml_annotations;
    }

    public void addAml_annotation(Aml_annotation aml_annotation) {
        this.aml_annotations.add(aml_annotation);
    }
    public aml_AmlDocument getAml_amldocument() {
        return aml_amldocument;
    }

    public void setAml_amldocument(aml_AmlDocument aml_amldocument) {
        this.aml_amldocument = aml_amldocument;
    }

}