





import java.util.List;
import java.util.ArrayList;

public class feature_HyBooleanAttribute extends HyFeatureAttribute {

    private boolean default;



    public feature_HyBooleanAttribute(
        boolean default    ) {
        super(
        );
        this.default = default;
    }


    public boolean getDefault() {
        return default;
    }

    public void setDefault(boolean default) {
        this.default = default;
    }


}