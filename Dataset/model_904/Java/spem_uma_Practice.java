





import java.util.List;
import java.util.ArrayList;

public class spem_uma_Practice extends Guidance {

    private String background;
    private String problem;
    private String additionalInfo;
    private String levelOfAdoption;
    private String goal;
    private String application;



    public spem_uma_Practice(
        String background,        String problem,        String additionalInfo,        String levelOfAdoption,        String goal,        String application    ) {
        super(
        );
        this.background = background;
        this.problem = problem;
        this.additionalInfo = additionalInfo;
        this.levelOfAdoption = levelOfAdoption;
        this.goal = goal;
        this.application = application;
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
    public String getGoal() {
        return goal;
    }

    public void setGoal(String goal) {
        this.goal = goal;
    }
    public String getApplication() {
        return application;
    }

    public void setApplication(String application) {
        this.application = application;
    }


}