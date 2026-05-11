





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_DataStore extends RootElement {

    private String isUnlimited;
    private String capacity;



    public BPMNProfile_DataStore(
        String isUnlimited,        String capacity    ) {
        super(
        );
        this.isUnlimited = isUnlimited;
        this.capacity = capacity;
    }


    public String getIsunlimited() {
        return isUnlimited;
    }

    public void setIsunlimited(String isUnlimited) {
        this.isUnlimited = isUnlimited;
    }
    public String getCapacity() {
        return capacity;
    }

    public void setCapacity(String capacity) {
        this.capacity = capacity;
    }


}