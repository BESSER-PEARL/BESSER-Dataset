





import java.util.List;
import java.util.ArrayList;

public class raas_small_test_TopClassB  {

    private int multi2lowerAttrInt;
    private String raasRef;
    private int singleAttrInt;
    private int optionalAttrInt;





    private List<raas_small_test_#5656663> raas_small_test_#5656663s;


    public raas_small_test_TopClassB(
        int multi2lowerAttrInt,        String raasRef,        int singleAttrInt,        int optionalAttrInt    ) {
        this.multi2lowerAttrInt = multi2lowerAttrInt;
        this.raasRef = raasRef;
        this.singleAttrInt = singleAttrInt;
        this.optionalAttrInt = optionalAttrInt;
        this.raas_small_test_#5656663s = new ArrayList<>();
    }

    public raas_small_test_TopClassB(
        int multi2lowerAttrInt,        String raasRef,        int singleAttrInt,        int optionalAttrInt        ArrayList<raas_small_test_#5656663> raas_small_test_#5656663s    ) {
        this.multi2lowerAttrInt = multi2lowerAttrInt;
        this.raasRef = raasRef;
        this.singleAttrInt = singleAttrInt;
        this.optionalAttrInt = optionalAttrInt;
        this.raas_small_test_#5656663s = raas_small_test_#5656663s;
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

    public List<raas_small_test_#5656663> getRaas_small_test_#5656663s() {
        return raas_small_test_#5656663s;
    }

    public void addRaas_small_test_#5656663(Raas_small_test_#5656663 raas_small_test_#5656663) {
        this.raas_small_test_#5656663s.add(raas_small_test_#5656663);
    }

}