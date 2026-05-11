





import java.util.List;
import java.util.ArrayList;

public class model_xsd_XSDNumericFacet extends XSDFundamentalFacet {

    private boolean value;



    public model_xsd_XSDNumericFacet(
        boolean value    ) {
        super(
        );
        this.value = value;
    }


    public boolean getValue() {
        return value;
    }

    public void setValue(boolean value) {
        this.value = value;
    }


}