





import java.util.List;
import java.util.ArrayList;

public class archimateC3_BusinessProcess extends BusinessBehaviorElement {

    private int importance;
    private String processFullName;
    private boolean missionary;
    private String processID;
    private String processType;
    private String processDesign;



    public archimateC3_BusinessProcess(
        int importance,        String processFullName,        boolean missionary,        String processID,        String processType,        String processDesign    ) {
        super(
        );
        this.importance = importance;
        this.processFullName = processFullName;
        this.missionary = missionary;
        this.processID = processID;
        this.processType = processType;
        this.processDesign = processDesign;
    }


    public int getImportance() {
        return importance;
    }

    public void setImportance(int importance) {
        this.importance = importance;
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
    public String getProcessdesign() {
        return processDesign;
    }

    public void setProcessdesign(String processDesign) {
        this.processDesign = processDesign;
    }


}