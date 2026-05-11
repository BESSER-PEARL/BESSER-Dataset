





import java.util.List;
import java.util.ArrayList;

public class bpmn2_DataStore extends RootElement, ItemAwareElement {

    private boolean isUnlimited;
    private int capacity;





    private bpmn2_DocumentRoot bpmn2_documentroot;


    public bpmn2_DataStore(
        boolean isUnlimited,        int capacity    ) {
        super(
        );
        this.isUnlimited = isUnlimited;
        this.capacity = capacity;
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

    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }

}