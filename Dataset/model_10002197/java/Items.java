





import java.util.List;
import java.util.ArrayList;

public class Items  {

    private int typeOfItems;
    private String ArrayList_ComputerParts_;
    private String ArrayList_devices_;
    private String ArrayList_accessories_;



    public Items(
        int typeOfItems,        String ArrayList_ComputerParts_,        String ArrayList_devices_,        String ArrayList_accessories_    ) {
        this.typeOfItems = typeOfItems;
        this.ArrayList_ComputerParts_ = ArrayList_ComputerParts_;
        this.ArrayList_devices_ = ArrayList_devices_;
        this.ArrayList_accessories_ = ArrayList_accessories_;
    }


    public int getTypeofitems() {
        return typeOfItems;
    }

    public void setTypeofitems(int typeOfItems) {
        this.typeOfItems = typeOfItems;
    }
    public String getArraylist_computerparts_() {
        return ArrayList_ComputerParts_;
    }

    public void setArraylist_computerparts_(String ArrayList_ComputerParts_) {
        this.ArrayList_ComputerParts_ = ArrayList_ComputerParts_;
    }
    public String getArraylist_devices_() {
        return ArrayList_devices_;
    }

    public void setArraylist_devices_(String ArrayList_devices_) {
        this.ArrayList_devices_ = ArrayList_devices_;
    }
    public String getArraylist_accessories_() {
        return ArrayList_accessories_;
    }

    public void setArraylist_accessories_(String ArrayList_accessories_) {
        this.ArrayList_accessories_ = ArrayList_accessories_;
    }


}