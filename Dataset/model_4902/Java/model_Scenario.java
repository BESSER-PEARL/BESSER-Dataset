





import java.util.List;
import java.util.ArrayList;

public class model_Scenario  {

    private String scenarioFilePath;



    public model_Scenario(
        String scenarioFilePath    ) {
        this.scenarioFilePath = scenarioFilePath;
    }


    public String getScenariofilepath() {
        return scenarioFilePath;
    }

    public void setScenariofilepath(String scenarioFilePath) {
        this.scenarioFilePath = scenarioFilePath;
    }


}