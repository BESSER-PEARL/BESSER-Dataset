





import java.util.List;
import java.util.ArrayList;

public class smm_SmmElement  {

    private String shortDescription;
    private String description;
    private String name;





    private smm_SmmRelationship smm_smmrelationship;




    private List<smm_Annotation> smm_annotations;




    private List<smm_SmmRelationship> smm_smmrelationships;




    private List<smm_SmmRelationship> smm_smmrelationships;




    private smm_SmmRelationship smm_smmrelationship;




    private List<smm_Attribute> smm_attributes;


    public smm_SmmElement(
        String shortDescription,        String description,        String name    ) {
        this.shortDescription = shortDescription;
        this.description = description;
        this.name = name;
        this.smm_annotations = new ArrayList<>();
        this.smm_smmrelationships = new ArrayList<>();
        this.smm_smmrelationships = new ArrayList<>();
        this.smm_attributes = new ArrayList<>();
    }

    public smm_SmmElement(
        String shortDescription,        String description,        String name        ArrayList<smm_Annotation> smm_annotations,        ArrayList<smm_SmmRelationship> smm_smmrelationships,        ArrayList<smm_SmmRelationship> smm_smmrelationships,        ArrayList<smm_Attribute> smm_attributes    ) {
        this.shortDescription = shortDescription;
        this.description = description;
        this.name = name;
        this.smm_annotations = smm_annotations;
        this.smm_smmrelationships = smm_smmrelationships;
        this.smm_smmrelationships = smm_smmrelationships;
        this.smm_attributes = smm_attributes;
    }

    public String getShortdescription() {
        return shortDescription;
    }

    public void setShortdescription(String shortDescription) {
        this.shortDescription = shortDescription;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public smm_SmmRelationship getSmm_smmrelationship() {
        return smm_smmrelationship;
    }

    public void setSmm_smmrelationship(smm_SmmRelationship smm_smmrelationship) {
        this.smm_smmrelationship = smm_smmrelationship;
    }
    public List<smm_Annotation> getSmm_annotations() {
        return smm_annotations;
    }

    public void addSmm_annotation(Smm_annotation smm_annotation) {
        this.smm_annotations.add(smm_annotation);
    }
    public List<smm_SmmRelationship> getSmm_smmrelationships() {
        return smm_smmrelationships;
    }

    public void addSmm_smmrelationship(Smm_smmrelationship smm_smmrelationship) {
        this.smm_smmrelationships.add(smm_smmrelationship);
    }
    public List<smm_SmmRelationship> getSmm_smmrelationships() {
        return smm_smmrelationships;
    }

    public void addSmm_smmrelationship(Smm_smmrelationship smm_smmrelationship) {
        this.smm_smmrelationships.add(smm_smmrelationship);
    }
    public smm_SmmRelationship getSmm_smmrelationship() {
        return smm_smmrelationship;
    }

    public void setSmm_smmrelationship(smm_SmmRelationship smm_smmrelationship) {
        this.smm_smmrelationship = smm_smmrelationship;
    }
    public List<smm_Attribute> getSmm_attributes() {
        return smm_attributes;
    }

    public void addSmm_attribute(Smm_attribute smm_attribute) {
        this.smm_attributes.add(smm_attribute);
    }

}