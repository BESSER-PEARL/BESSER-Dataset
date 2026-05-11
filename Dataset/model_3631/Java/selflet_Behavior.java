





import java.util.List;
import java.util.ArrayList;

public class selflet_Behavior  {

    private String isDefaultBehavior;
    private String fileName;
    private String name;
    private String elementaryBehaviorCost;
    private String elementaryBehaviorCPUTime;



    public selflet_Behavior(
        String isDefaultBehavior,        String fileName,        String name,        String elementaryBehaviorCost,        String elementaryBehaviorCPUTime    ) {
        this.isDefaultBehavior = isDefaultBehavior;
        this.fileName = fileName;
        this.name = name;
        this.elementaryBehaviorCost = elementaryBehaviorCost;
        this.elementaryBehaviorCPUTime = elementaryBehaviorCPUTime;
    }


    public String getIsdefaultbehavior() {
        return isDefaultBehavior;
    }

    public void setIsdefaultbehavior(String isDefaultBehavior) {
        this.isDefaultBehavior = isDefaultBehavior;
    }
    public String getFilename() {
        return fileName;
    }

    public void setFilename(String fileName) {
        this.fileName = fileName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getElementarybehaviorcost() {
        return elementaryBehaviorCost;
    }

    public void setElementarybehaviorcost(String elementaryBehaviorCost) {
        this.elementaryBehaviorCost = elementaryBehaviorCost;
    }
    public String getElementarybehaviorcputime() {
        return elementaryBehaviorCPUTime;
    }

    public void setElementarybehaviorcputime(String elementaryBehaviorCPUTime) {
        this.elementaryBehaviorCPUTime = elementaryBehaviorCPUTime;
    }


}