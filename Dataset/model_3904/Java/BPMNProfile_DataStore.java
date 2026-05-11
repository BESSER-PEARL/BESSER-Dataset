





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_DataStore extends RootElement {

    private String capacity;
    private String isUnlimited;



    public BPMNProfile_DataStore(
        String capacity,        String isUnlimited    ) {
        super(
        );
        this.capacity = capacity;
        this.isUnlimited = isUnlimited;
    }


    public String getCapacity() {
        return capacity;
    }

    public void setCapacity(String capacity) {
        this.capacity = capacity;
    }
    public String getIsunlimited() {
        return isUnlimited;
    }

    public void setIsunlimited(String isUnlimited) {
        this.isUnlimited = isUnlimited;
    }


}