





import java.util.List;
import java.util.ArrayList;

public class smm_SmmElement  {

    private String description;
    private String shortDescription;
    private String name;





    private List<smm_Attribute> smm_attributes;




    private smm_Observation smm_observation;




    private List<smm_Annotation> smm_annotations;


    public smm_SmmElement(
        String description,        String shortDescription,        String name    ) {
        this.description = description;
        this.shortDescription = shortDescription;
        this.name = name;
        this.smm_attributes = new ArrayList<>();
        this.smm_annotations = new ArrayList<>();
    }

    public smm_SmmElement(
        String description,        String shortDescription,        String name        ArrayList<smm_Attribute> smm_attributes,        ArrayList<smm_Annotation> smm_annotations    ) {
        this.description = description;
        this.shortDescription = shortDescription;
        this.name = name;
        this.smm_attributes = smm_attributes;
        this.smm_annotations = smm_annotations;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getShortdescription() {
        return shortDescription;
    }

    public void setShortdescription(String shortDescription) {
        this.shortDescription = shortDescription;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<smm_Attribute> getSmm_attributes() {
        return smm_attributes;
    }

    public void addSmm_attribute(Smm_attribute smm_attribute) {
        this.smm_attributes.add(smm_attribute);
    }
    public smm_Observation getSmm_observation() {
        return smm_observation;
    }

    public void setSmm_observation(smm_Observation smm_observation) {
        this.smm_observation = smm_observation;
    }
    public List<smm_Annotation> getSmm_annotations() {
        return smm_annotations;
    }

    public void addSmm_annotation(Smm_annotation smm_annotation) {
        this.smm_annotations.add(smm_annotation);
    }

}