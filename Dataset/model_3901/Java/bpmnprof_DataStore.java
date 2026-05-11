





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_DataStore extends RootElement {

    private String capacity;
    private String isUnlimited;





    private bpmnprof_DataStoreReference bpmnprof_datastorereference;




    private bpmnprof_Class bpmnprof_class;


    public bpmnprof_DataStore(
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

    public bpmnprof_DataStoreReference getBpmnprof_datastorereference() {
        return bpmnprof_datastorereference;
    }

    public void setBpmnprof_datastorereference(bpmnprof_DataStoreReference bpmnprof_datastorereference) {
        this.bpmnprof_datastorereference = bpmnprof_datastorereference;
    }
    public bpmnprof_Class getBpmnprof_class() {
        return bpmnprof_class;
    }

    public void setBpmnprof_class(bpmnprof_Class bpmnprof_class) {
        this.bpmnprof_class = bpmnprof_class;
    }

}