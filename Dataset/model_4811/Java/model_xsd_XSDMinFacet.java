





import java.util.List;
import java.util.ArrayList;

public class model_xsd_XSDMinFacet extends XSDFixedFacet {

    private boolean inclusive;
    private String value;
    private boolean exclusive;



    public model_xsd_XSDMinFacet(
        boolean inclusive,        String value,        boolean exclusive    ) {
        super(
        );
        this.inclusive = inclusive;
        this.value = value;
        this.exclusive = exclusive;
    }


    public boolean getInclusive() {
        return inclusive;
    }

    public void setInclusive(boolean inclusive) {
        this.inclusive = inclusive;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public boolean getExclusive() {
        return exclusive;
    }

    public void setExclusive(boolean exclusive) {
        this.exclusive = exclusive;
    }


}