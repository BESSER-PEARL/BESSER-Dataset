





import java.util.List;
import java.util.ArrayList;

public class model_xsd_XSDMinLengthFacet extends XSDFixedFacet {

    private int value;



    public model_xsd_XSDMinLengthFacet(
        int value    ) {
        super(
        );
        this.value = value;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }


}