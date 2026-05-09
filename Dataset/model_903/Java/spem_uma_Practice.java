





import java.util.List;
import java.util.ArrayList;

public class spem_uma_Practice extends Guidance {

    private String application;
    private String levelOfAdoption;
    private String additionalInfo;
    private String goal;
    private String background;
    private String problem;



    public spem_uma_Practice(
        String application,        String levelOfAdoption,        String additionalInfo,        String goal,        String background,        String problem    ) {
        super(
        );
        this.application = application;
        this.levelOfAdoption = levelOfAdoption;
        this.additionalInfo = additionalInfo;
        this.goal = goal;
        this.background = background;
        this.problem = problem;
    }


    public String getApplication() {
        return application;
    }

    public void setApplication(String application) {
        this.application = application;
    }
    public String getLevelofadoption() {
        return levelOfAdoption;
    }

    public void setLevelofadoption(String levelOfAdoption) {
        this.levelOfAdoption = levelOfAdoption;
    }
    public String getAdditionalinfo() {
        return additionalInfo;
    }

    public void setAdditionalinfo(String additionalInfo) {
        this.additionalInfo = additionalInfo;
    }
    public String getGoal() {
        return goal;
    }

    public void setGoal(String goal) {
        this.goal = goal;
    }
    public String getBackground() {
        return background;
    }

    public void setBackground(String background) {
        this.background = background;
    }
    public String getProblem() {
        return problem;
    }

    public void setProblem(String problem) {
        this.problem = problem;
    }


}