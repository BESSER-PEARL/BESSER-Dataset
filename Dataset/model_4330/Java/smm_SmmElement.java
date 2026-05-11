





import java.util.List;
import java.util.ArrayList;

public class smm_SmmElement  {

    private String name;
    private String shortDescription;
    private String description;





    private smm_Observation smm_observation;




    private List<smm_Annotation> smm_annotations;




    private List<smm_Attribute> smm_attributes;




    private List<smm_Observation> smm_observations;


    public smm_SmmElement(
        String name,        String shortDescription,        String description    ) {
        this.name = name;
        this.shortDescription = shortDescription;
        this.description = description;
        this.smm_annotations = new ArrayList<>();
        this.smm_attributes = new ArrayList<>();
        this.smm_observations = new ArrayList<>();
    }

    public smm_SmmElement(
        String name,        String shortDescription,        String description        ArrayList<smm_Annotation> smm_annotations,        ArrayList<smm_Attribute> smm_attributes,        ArrayList<smm_Observation> smm_observations    ) {
        this.name = name;
        this.shortDescription = shortDescription;
        this.description = description;
        this.smm_annotations = smm_annotations;
        this.smm_attributes = smm_attributes;
        this.smm_observations = smm_observations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public List<smm_Attribute> getSmm_attributes() {
        return smm_attributes;
    }

    public void addSmm_attribute(Smm_attribute smm_attribute) {
        this.smm_attributes.add(smm_attribute);
    }
    public List<smm_Observation> getSmm_observations() {
        return smm_observations;
    }

    public void addSmm_observation(Smm_observation smm_observation) {
        this.smm_observations.add(smm_observation);
    }

}