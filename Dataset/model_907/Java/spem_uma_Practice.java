





import java.util.List;
import java.util.ArrayList;

public class spem_uma_Practice extends Guidance {

    private String additionalInfo;
    private String problem;
    private String goal;
    private String levelOfAdoption;
    private String application;
    private String background;



    public spem_uma_Practice(
        String additionalInfo,        String problem,        String goal,        String levelOfAdoption,        String application,        String background    ) {
        super(
        );
        this.additionalInfo = additionalInfo;
        this.problem = problem;
        this.goal = goal;
        this.levelOfAdoption = levelOfAdoption;
        this.application = application;
        this.background = background;
    }


    public String getAdditionalinfo() {
        return additionalInfo;
    }

    public void setAdditionalinfo(String additionalInfo) {
        this.additionalInfo = additionalInfo;
    }
    public String getProblem() {
        return problem;
    }

    public void setProblem(String problem) {
        this.problem = problem;
    }
    public String getGoal() {
        return goal;
    }

    public void setGoal(String goal) {
        this.goal = goal;
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
    public String getBackground() {
        return background;
    }

    public void setBackground(String background) {
        this.background = background;
    }


}