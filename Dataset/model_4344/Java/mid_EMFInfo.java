





import java.util.List;
import java.util.ArrayList;

public class mid_EMFInfo  {

    private String relatedClassName;
    private String featureName;
    private boolean attribute;
    private String className;





    private mid_ModelElement mid_modelelement;


    public mid_EMFInfo(
        String relatedClassName,        String featureName,        boolean attribute,        String className    ) {
        this.relatedClassName = relatedClassName;
        this.featureName = featureName;
        this.attribute = attribute;
        this.className = className;
    }


    public String getRelatedclassname() {
        return relatedClassName;
    }

    public void setRelatedclassname(String relatedClassName) {
        this.relatedClassName = relatedClassName;
    }
    public String getFeaturename() {
        return featureName;
    }

    public void setFeaturename(String featureName) {
        this.featureName = featureName;
    }
    public boolean getAttribute() {
        return attribute;
    }

    public void setAttribute(boolean attribute) {
        this.attribute = attribute;
    }
    public String getClassname() {
        return className;
    }

    public void setClassname(String className) {
        this.className = className;
    }

    public mid_ModelElement getMid_modelelement() {
        return mid_modelelement;
    }

    public void setMid_modelelement(mid_ModelElement mid_modelelement) {
        this.mid_modelelement = mid_modelelement;
    }

}