





import java.util.List;
import java.util.ArrayList;

public class bpmn2_DataStore extends RootElement, ItemAwareElement {

    private int capacity;
    private String name;
    private boolean isUnlimited;



    public bpmn2_DataStore(
        int capacity,        String name,        boolean isUnlimited    ) {
        super(
        );
        this.capacity = capacity;
        this.name = name;
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
    public boolean getIsunlimited() {
        return isUnlimited;
    }

    public void setIsunlimited(boolean isUnlimited) {
        this.isUnlimited = isUnlimited;
    }


}