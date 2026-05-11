





import java.util.List;
import java.util.ArrayList;

public class raas_small_test_FourthLevelClassK  {

    private String raasRef;
    private int optionalAttrInt;
    private int singleAttrInt;
    private int multi2lowerAttrInt;



    public raas_small_test_FourthLevelClassK(
        String raasRef,        int optionalAttrInt,        int singleAttrInt,        int multi2lowerAttrInt    ) {
        this.raasRef = raasRef;
        this.optionalAttrInt = optionalAttrInt;
        this.singleAttrInt = singleAttrInt;
        this.multi2lowerAttrInt = multi2lowerAttrInt;
    }


    public String getRaasref() {
        return raasRef;
    }

    public void setRaasref(String raasRef) {
        this.raasRef = raasRef;
    }
    public int getOptionalattrint() {
        return optionalAttrInt;
    }

    public void setOptionalattrint(int optionalAttrInt) {
        this.optionalAttrInt = optionalAttrInt;
    }
    public int getSingleattrint() {
        return singleAttrInt;
    }

    public void setSingleattrint(int singleAttrInt) {
        this.singleAttrInt = singleAttrInt;
    }
    public int getMulti2lowerattrint() {
        return multi2lowerAttrInt;
    }

    public void setMulti2lowerattrint(int multi2lowerAttrInt) {
        this.multi2lowerAttrInt = multi2lowerAttrInt;
    }


}