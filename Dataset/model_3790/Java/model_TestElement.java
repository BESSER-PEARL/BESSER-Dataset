





import java.util.List;
import java.util.ArrayList;

public class model_TestElement  {

    private String elementUnderTest;
    private String target;
    private String description;
    private String progressState;
    private String name;
    private String endTimestamp;
    private String startTimestamp;
    private String testState;



    public model_TestElement(
        String elementUnderTest,        String target,        String description,        String progressState,        String name,        String endTimestamp,        String startTimestamp,        String testState    ) {
        this.elementUnderTest = elementUnderTest;
        this.target = target;
        this.description = description;
        this.progressState = progressState;
        this.name = name;
        this.endTimestamp = endTimestamp;
        this.startTimestamp = startTimestamp;
        this.testState = testState;
    }


    public String getElementundertest() {
        return elementUnderTest;
    }

    public void setElementundertest(String elementUnderTest) {
        this.elementUnderTest = elementUnderTest;
    }
    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getProgressstate() {
        return progressState;
    }

    public void setProgressstate(String progressState) {
        this.progressState = progressState;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getEndtimestamp() {
        return endTimestamp;
    }

    public void setEndtimestamp(String endTimestamp) {
        this.endTimestamp = endTimestamp;
    }
    public String getStarttimestamp() {
        return startTimestamp;
    }

    public void setStarttimestamp(String startTimestamp) {
        this.startTimestamp = startTimestamp;
    }
    public String getTeststate() {
        return testState;
    }

    public void setTeststate(String testState) {
        this.testState = testState;
    }


}