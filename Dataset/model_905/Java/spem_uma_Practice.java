





import java.util.List;
import java.util.ArrayList;

public class spem_uma_Practice extends Guidance {

    private String background;
    private String additionalInfo;
    private String levelOfAdoption;
    private String application;
    private String goal;
    private String problem;



    public spem_uma_Practice(
        String background,        String additionalInfo,        String levelOfAdoption,        String application,        String goal,        String problem    ) {
        super(
        );
        this.background = background;
        this.additionalInfo = additionalInfo;
        this.levelOfAdoption = levelOfAdoption;
        this.application = application;
        this.goal = goal;
        this.problem = problem;
    }


    public String getBackground() {
        return background;
    }

    public void setBackground(String background) {
        this.background = background;
    }
    public String getAdditionalinfo() {
        return additionalInfo;
    }

    public void setAdditionalinfo(String additionalInfo) {
        this.additionalInfo = additionalInfo;
    }
    public String getLevelofadoption() {
        return levelOfAdoption;
    }

    public void setLevelofadoption(String levelOfAdoption) {
        this.levelOfAdoption = levelOfAdoption;
    }
    public String getApplication() {
        return application;
    }

    public void setApplication(String application) {
        this.application = application;
    }
    public String getGoal() {
        return goal;
    }

    public void setGoal(String goal) {
        this.goal = goal;
    }
    public String getProblem() {
        return problem;
    }

    public void setProblem(String problem) {
        this.problem = problem;
    }


}