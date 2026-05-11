





import java.util.List;
import java.util.ArrayList;

public class archimateC3_BusinessProcess extends BusinessBehaviorElement {

    private String processFullName;
    private boolean missionary;
    private String processDesign;
    private int importance;
    private String processID;
    private String processType;



    public archimateC3_BusinessProcess(
        String processFullName,        boolean missionary,        String processDesign,        int importance,        String processID,        String processType    ) {
        super(
        );
        this.processFullName = processFullName;
        this.missionary = missionary;
        this.processDesign = processDesign;
        this.importance = importance;
        this.processID = processID;
        this.processType = processType;
    }


    public String getProcessfullname() {
        return processFullName;
    }

    public void setProcessfullname(String processFullName) {
        this.processFullName = processFullName;
    }
    public boolean getMissionary() {
        return missionary;
    }

    public void setMissionary(boolean missionary) {
        this.missionary = missionary;
    }
    public String getProcessdesign() {
        return processDesign;
    }

    public void setProcessdesign(String processDesign) {
        this.processDesign = processDesign;
    }
    public int getImportance() {
        return importance;
    }

    public void setImportance(int importance) {
        this.importance = importance;
    }
    public String getProcessid() {
        return processID;
    }

    public void setProcessid(String processID) {
        this.processID = processID;
    }
    public String getProcesstype() {
        return processType;
    }

    public void setProcesstype(String processType) {
        this.processType = processType;
    }


}