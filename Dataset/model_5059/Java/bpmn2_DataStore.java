





import java.util.List;
import java.util.ArrayList;

public class bpmn2_DataStore extends RootElement, ItemAwareElement {

    private boolean isUnlimited;
    private int capacity;
    private String name;



    public bpmn2_DataStore(
        boolean isUnlimited,        int capacity,        String name    ) {
        super(
        );
        this.isUnlimited = isUnlimited;
        this.capacity = capacity;
        this.name = name;
    }


    public boolean getIsunlimited() {
        return isUnlimited;
    }

    public void setIsunlimited(boolean isUnlimited) {
        this.isUnlimited = isUnlimited;
    }
    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}