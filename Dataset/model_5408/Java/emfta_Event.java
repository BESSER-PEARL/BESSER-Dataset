





import java.util.List;
import java.util.ArrayList;

public class emfta_Event  {

    private int referenceCount;
    private String relatedObject;
    private String description;
    private String type;
    private float probability;
    private String name;





    private emfta_FTAModel emfta_ftamodel;




    private emfta_FTAModel emfta_ftamodel;


    public emfta_Event(
        int referenceCount,        String relatedObject,        String description,        String type,        float probability,        String name    ) {
        this.referenceCount = referenceCount;
        this.relatedObject = relatedObject;
        this.description = description;
        this.type = type;
        this.probability = probability;
        this.name = name;
    }


    public int getReferencecount() {
        return referenceCount;
    }

    public void setReferencecount(int referenceCount) {
        this.referenceCount = referenceCount;
    }
    public String getRelatedobject() {
        return relatedObject;
    }

    public void setRelatedobject(String relatedObject) {
        this.relatedObject = relatedObject;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public float getProbability() {
        return probability;
    }

    public void setProbability(float probability) {
        this.probability = probability;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public emfta_FTAModel getEmfta_ftamodel() {
        return emfta_ftamodel;
    }

    public void setEmfta_ftamodel(emfta_FTAModel emfta_ftamodel) {
        this.emfta_ftamodel = emfta_ftamodel;
    }
    public emfta_FTAModel getEmfta_ftamodel() {
        return emfta_ftamodel;
    }

    public void setEmfta_ftamodel(emfta_FTAModel emfta_ftamodel) {
        this.emfta_ftamodel = emfta_ftamodel;
    }

}