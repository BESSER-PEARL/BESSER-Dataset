





import java.util.List;
import java.util.ArrayList;

public class mid_EMFInfo  {

    private String relatedClassName;
    private String className;
    private String featureName;
    private boolean attribute;





    private mid_ModelElement mid_modelelement;


    public mid_EMFInfo(
        String relatedClassName,        String className,        String featureName,        boolean attribute    ) {
        this.relatedClassName = relatedClassName;
        this.className = className;
        this.featureName = featureName;
        this.attribute = attribute;
    }


    public String getRelatedclassname() {
        return relatedClassName;
    }

    public void setRelatedclassname(String relatedClassName) {
        this.relatedClassName = relatedClassName;
    }
    public String getClassname() {
        return className;
    }

    public void setClassname(String className) {
        this.className = className;
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

    public mid_ModelElement getMid_modelelement() {
        return mid_modelelement;
    }

    public void setMid_modelelement(mid_ModelElement mid_modelelement) {
        this.mid_modelelement = mid_modelelement;
    }

}