





import java.util.List;
import java.util.ArrayList;

public class uma_PracticeDescription extends ContentDescription {

    private String goals;
    private String levelsOfAdoption;
    private String problem;
    private String additionalInfo;
    private String application;
    private String background;



    public uma_PracticeDescription(
        String goals,        String levelsOfAdoption,        String problem,        String additionalInfo,        String application,        String background    ) {
        super(
        );
        this.goals = goals;
        this.levelsOfAdoption = levelsOfAdoption;
        this.problem = problem;
        this.additionalInfo = additionalInfo;
        this.application = application;
        this.background = background;
    }


    public String getGoals() {
        return goals;
    }

    public void setGoals(String goals) {
        this.goals = goals;
    }
    public String getLevelsofadoption() {
        return levelsOfAdoption;
    }

    public void setLevelsofadoption(String levelsOfAdoption) {
        this.levelsOfAdoption = levelsOfAdoption;
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