





import java.util.List;
import java.util.ArrayList;

public class archimateC2_BusinessProcess extends BusinessBehaviorElement {

    private int importance;
    private String processType;
    private String processDesign;
    private boolean missionary;
    private String processFullName;
    private String processID;



    public archimateC2_BusinessProcess(
        int importance,        String processType,        String processDesign,        boolean missionary,        String processFullName,        String processID    ) {
        super(
        );
        this.importance = importance;
        this.processType = processType;
        this.processDesign = processDesign;
        this.missionary = missionary;
        this.processFullName = processFullName;
        this.processID = processID;
    }


    public int getImportance() {
        return importance;
    }

    public void setImportance(int importance) {
        this.importance = importance;
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
    public boolean getMissionary() {
        return missionary;
    }

    public void setMissionary(boolean missionary) {
        this.missionary = missionary;
    }
    public String getProcessfullname() {
        return processFullName;
    }

    public void setProcessfullname(String processFullName) {
        this.processFullName = processFullName;
    }
    public String getProcessid() {
        return processID;
    }

    public void setProcessid(String processID) {
        this.processID = processID;
    }


}