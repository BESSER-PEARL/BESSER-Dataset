





import java.util.List;
import java.util.ArrayList;

public class model_xsd_XSDMaxFacet extends XSDFixedFacet {

    private String value;
    private boolean exclusive;
    private boolean inclusive;



    public model_xsd_XSDMaxFacet(
        String value,        boolean exclusive,        boolean inclusive    ) {
        super(
        );
        this.value = value;
        this.exclusive = exclusive;
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
    public boolean getInclusive() {
        return inclusive;
    }

    public void setInclusive(boolean inclusive) {
        this.inclusive = inclusive;
    }


}