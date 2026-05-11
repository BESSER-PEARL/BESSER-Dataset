





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_EAttributeCustomization extends EStructuralFeatureCustomization {

    private String value;
    private String attributeName;



    public viewpoint_description_EAttributeCustomization(
        String value,        String attributeName    ) {
        super(
        );
        this.value = value;
        this.attributeName = attributeName;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getAttributename() {
        return attributeName;
    }

    public void setAttributename(String attributeName) {
        this.attributeName = attributeName;
    }


}