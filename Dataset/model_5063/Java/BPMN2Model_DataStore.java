





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_DataStore extends ItemAwareElement, RootElement {

    private String name;
    private int capacity;
    private boolean isUnlimited;



    public BPMN2Model_DataStore(
        String name,        int capacity,        boolean isUnlimited    ) {
        super(
        );
        this.name = name;
        this.capacity = capacity;
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
    public boolean getIsunlimited() {
        return isUnlimited;
    }

    public void setIsunlimited(boolean isUnlimited) {
        this.isUnlimited = isUnlimited;
    }


}