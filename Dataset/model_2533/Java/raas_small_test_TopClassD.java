





import java.util.List;
import java.util.ArrayList;

public class raas_small_test_TopClassD  {

    private String raasRef;
    private int singleAttrInt;
    private int optionalAttrInt;
    private String optionalTimeZone;
    private int multi2lowerAttrInt;



    public raas_small_test_TopClassD(
        String raasRef,        int singleAttrInt,        int optionalAttrInt,        String optionalTimeZone,        int multi2lowerAttrInt    ) {
        this.raasRef = raasRef;
        this.singleAttrInt = singleAttrInt;
        this.optionalAttrInt = optionalAttrInt;
        this.optionalTimeZone = optionalTimeZone;
        this.multi2lowerAttrInt = multi2lowerAttrInt;
    }


    public String getRaasref() {
        return raasRef;
    }

    public void setRaasref(String raasRef) {
        this.raasRef = raasRef;
    }
    public int getSingleattrint() {
        return singleAttrInt;
    }

    public void setSingleattrint(int singleAttrInt) {
        this.singleAttrInt = singleAttrInt;
    }
    public int getOptionalattrint() {
        return optionalAttrInt;
    }

    public void setOptionalattrint(int optionalAttrInt) {
        this.optionalAttrInt = optionalAttrInt;
    }
    public String getOptionaltimezone() {
        return optionalTimeZone;
    }

    public void setOptionaltimezone(String optionalTimeZone) {
        this.optionalTimeZone = optionalTimeZone;
    }
    public int getMulti2lowerattrint() {
        return multi2lowerAttrInt;
    }

    public void setMulti2lowerattrint(int multi2lowerAttrInt) {
        this.multi2lowerAttrInt = multi2lowerAttrInt;
    }


}