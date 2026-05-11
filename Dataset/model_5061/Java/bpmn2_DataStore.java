





import java.util.List;
import java.util.ArrayList;

public class bpmn2_DataStore extends RootElement, ItemAwareElement {

    private boolean isUnlimited;
    private String name;
    private int capacity;



    public bpmn2_DataStore(
        boolean isUnlimited,        String name,        int capacity    ) {
        super(
        );
        this.isUnlimited = isUnlimited;
        this.name = name;
        this.capacity = capacity;
    }


    public boolean getIsunlimited() {
        return isUnlimited;
    }

    public void setIsunlimited(boolean isUnlimited) {
        this.isUnlimited = isUnlimited;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }


}