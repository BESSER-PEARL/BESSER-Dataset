





import java.util.List;
import java.util.ArrayList;

public class raas_small_test_ThirdLevelClassJ  {

    private int singleAttrInt;
    private int optionalAttrInt;
    private int multi2lowerAttrInt;
    private String raasRef;



    public raas_small_test_ThirdLevelClassJ(
        int singleAttrInt,        int optionalAttrInt,        int multi2lowerAttrInt,        String raasRef    ) {
        this.singleAttrInt = singleAttrInt;
        this.optionalAttrInt = optionalAttrInt;
        this.multi2lowerAttrInt = multi2lowerAttrInt;
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
    public int getMulti2lowerattrint() {
        return multi2lowerAttrInt;
    }

    public void setMulti2lowerattrint(int multi2lowerAttrInt) {
        this.multi2lowerAttrInt = multi2lowerAttrInt;
    }
    public String getRaasref() {
        return raasRef;
    }

    public void setRaasref(String raasRef) {
        this.raasRef = raasRef;
    }


}