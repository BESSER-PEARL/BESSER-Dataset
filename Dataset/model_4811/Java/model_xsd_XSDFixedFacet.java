





import java.util.List;
import java.util.ArrayList;

public class model_xsd_XSDFixedFacet extends XSDConstrainingFacet {

    private boolean fixed;



    public model_xsd_XSDFixedFacet(
        boolean fixed    ) {
        super(
        );
        this.fixed = fixed;
    }


    public boolean getFixed() {
        return fixed;
    }

    public void setFixed(boolean fixed) {
        this.fixed = fixed;
    }


}