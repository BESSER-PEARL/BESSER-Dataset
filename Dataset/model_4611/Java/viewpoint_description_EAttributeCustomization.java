





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_EAttributeCustomization extends EStructuralFeatureCustomization {

    private String attributeName;
    private String value;



    public viewpoint_description_EAttributeCustomization(
        String attributeName,        String value    ) {
        super(
        );
        this.attributeName = attributeName;
        this.value = value;
    }


    public String getAttributename() {
        return attributeName;
    }

    public void setAttributename(String attributeName) {
        this.attributeName = attributeName;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}