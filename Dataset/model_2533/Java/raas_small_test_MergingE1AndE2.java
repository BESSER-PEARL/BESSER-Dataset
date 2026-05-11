





import java.util.List;
import java.util.ArrayList;

public class raas_small_test_MergingE1AndE2 extends raas_small_test_DerivedUnderClassE1, raas_small_test_DerivedUnderClassE2 {

    private String optionalAttrString;



    public raas_small_test_MergingE1AndE2(
        String optionalAttrString    ) {
        super(
        );
        this.optionalAttrString = optionalAttrString;
    }


    public String getOptionalattrstring() {
        return optionalAttrString;
    }

    public void setOptionalattrstring(String optionalAttrString) {
        this.optionalAttrString = optionalAttrString;
    }


}