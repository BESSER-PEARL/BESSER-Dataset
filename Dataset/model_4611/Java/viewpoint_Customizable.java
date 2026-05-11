





import java.util.List;
import java.util.ArrayList;

public class viewpoint_Customizable extends IdentifiedElement {

    private String customFeatures;



    public viewpoint_Customizable(
        String customFeatures    ) {
        super(
        );
        this.customFeatures = customFeatures;
    }


    public String getCustomfeatures() {
        return customFeatures;
    }

    public void setCustomfeatures(String customFeatures) {
        this.customFeatures = customFeatures;
    }


}