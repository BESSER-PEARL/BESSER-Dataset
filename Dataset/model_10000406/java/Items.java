





import java.util.List;
import java.util.ArrayList;

public class Items  {

    private String ArrayList_appliance_;
    private String ArrayList_furniture_;
    private int typeOfItems;
    private String ArrayList_food_;



    public Items(
        String ArrayList_appliance_,        String ArrayList_furniture_,        int typeOfItems,        String ArrayList_food_    ) {
        this.ArrayList_appliance_ = ArrayList_appliance_;
        this.ArrayList_furniture_ = ArrayList_furniture_;
        this.typeOfItems = typeOfItems;
        this.ArrayList_food_ = ArrayList_food_;
    }


    public String getArraylist_appliance_() {
        return ArrayList_appliance_;
    }

    public void setArraylist_appliance_(String ArrayList_appliance_) {
        this.ArrayList_appliance_ = ArrayList_appliance_;
    }
    public String getArraylist_furniture_() {
        return ArrayList_furniture_;
    }

    public void setArraylist_furniture_(String ArrayList_furniture_) {
        this.ArrayList_furniture_ = ArrayList_furniture_;
    }
    public int getTypeofitems() {
        return typeOfItems;
    }

    public void setTypeofitems(int typeOfItems) {
        this.typeOfItems = typeOfItems;
    }
    public String getArraylist_food_() {
        return ArrayList_food_;
    }

    public void setArraylist_food_(String ArrayList_food_) {
        this.ArrayList_food_ = ArrayList_food_;
    }


}