





import java.util.List;
import java.util.ArrayList;

public class uma_PracticeDescription extends ContentDescription {

    private String problem;
    private String goals;
    private String background;
    private String levelsOfAdoption;
    private String additionalInfo;
    private String application;



    public uma_PracticeDescription(
        String problem,        String goals,        String background,        String levelsOfAdoption,        String additionalInfo,        String application    ) {
        super(
        );
        this.problem = problem;
        this.goals = goals;
        this.background = background;
        this.levelsOfAdoption = levelsOfAdoption;
        this.additionalInfo = additionalInfo;
        this.application = application;
    }


    public String getProblem() {
        return problem;
    }

    public void setProblem(String problem) {
        this.problem = problem;
    }
    public String getGoals() {
        return goals;
    }

    public void setGoals(String goals) {
        this.goals = goals;
    }
    public String getBackground() {
        return background;
    }

    public void setBackground(String background) {
        this.background = background;
    }
    public String getLevelsofadoption() {
        return levelsOfAdoption;
    }

    public void setLevelsofadoption(String levelsOfAdoption) {
        this.levelsOfAdoption = levelsOfAdoption;
    }
    public String getAdditionalinfo() {
        return additionalInfo;
    }

    public void setAdditionalinfo(String additionalInfo) {
        this.additionalInfo = additionalInfo;
    }
    public String getApplication() {
        return application;
    }

    public void setApplication(String application) {
        this.application = application;
    }


}