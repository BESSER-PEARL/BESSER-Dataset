





import java.util.List;
import java.util.ArrayList;

public class feature_HyStringAttribute extends HyFeatureAttribute {

    private String default;



    public feature_HyStringAttribute(
        String default    ) {
        super(
        );
        this.default = default;
    }


    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }


}