





import java.util.List;
import java.util.ArrayList;

public class model_xsd_XSDEnumerationFacet extends XSDRepeatableFacet {

    private String value;



    public model_xsd_XSDEnumerationFacet(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}