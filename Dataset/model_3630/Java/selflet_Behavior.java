





import java.util.List;
import java.util.ArrayList;

public class selflet_Behavior  {

    private String elementaryBehaviorCost;
    private String name;
    private String fileName;
    private String elementaryBehaviorCPUTime;
    private String isDefaultBehavior;



    public selflet_Behavior(
        String elementaryBehaviorCost,        String name,        String fileName,        String elementaryBehaviorCPUTime,        String isDefaultBehavior    ) {
        this.elementaryBehaviorCost = elementaryBehaviorCost;
        this.name = name;
        this.fileName = fileName;
        this.elementaryBehaviorCPUTime = elementaryBehaviorCPUTime;
        this.isDefaultBehavior = isDefaultBehavior;
    }


    public String getElementarybehaviorcost() {
        return elementaryBehaviorCost;
    }

    public void setElementarybehaviorcost(String elementaryBehaviorCost) {
        this.elementaryBehaviorCost = elementaryBehaviorCost;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getFilename() {
        return fileName;
    }

    public void setFilename(String fileName) {
        this.fileName = fileName;
    }
    public String getElementarybehaviorcputime() {
        return elementaryBehaviorCPUTime;
    }

    public void setElementarybehaviorcputime(String elementaryBehaviorCPUTime) {
        this.elementaryBehaviorCPUTime = elementaryBehaviorCPUTime;
    }
    public String getIsdefaultbehavior() {
        return isDefaultBehavior;
    }

    public void setIsdefaultbehavior(String isDefaultBehavior) {
        this.isDefaultBehavior = isDefaultBehavior;
    }


}