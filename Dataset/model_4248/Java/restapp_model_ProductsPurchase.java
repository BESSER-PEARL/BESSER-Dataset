





import java.util.List;
import java.util.ArrayList;

public class restapp_model_ProductsPurchase  {

    private int unityDiscount;
    private int quantity;
    private float unityValueWithDiscount;
    private float unityValue;



    public restapp_model_ProductsPurchase(
        int unityDiscount,        int quantity,        float unityValueWithDiscount,        float unityValue    ) {
        this.unityDiscount = unityDiscount;
        this.quantity = quantity;
        this.unityValueWithDiscount = unityValueWithDiscount;
        this.unityValue = unityValue;
    }


    public int getUnitydiscount() {
        return unityDiscount;
    }

    public void setUnitydiscount(int unityDiscount) {
        this.unityDiscount = unityDiscount;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public float getUnityvaluewithdiscount() {
        return unityValueWithDiscount;
    }

    public void setUnityvaluewithdiscount(float unityValueWithDiscount) {
        this.unityValueWithDiscount = unityValueWithDiscount;
    }
    public float getUnityvalue() {
        return unityValue;
    }

    public void setUnityvalue(float unityValue) {
        this.unityValue = unityValue;
    }


}