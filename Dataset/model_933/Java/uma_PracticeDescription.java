





import java.util.List;
import java.util.ArrayList;

public class uma_PracticeDescription extends ContentDescription {

    private String background;
    private String additionalInfo;
    private String levelsOfAdoption;
    private String goals;
    private String application;
    private String problem;



    public uma_PracticeDescription(
        String background,        String additionalInfo,        String levelsOfAdoption,        String goals,        String application,        String problem    ) {
        super(
        );
        this.background = background;
        this.additionalInfo = additionalInfo;
        this.levelsOfAdoption = levelsOfAdoption;
        this.goals = goals;
        this.application = application;
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
    public String getLevelsofadoption() {
        return levelsOfAdoption;
    }

    public void setLevelsofadoption(String levelsOfAdoption) {
        this.levelsOfAdoption = levelsOfAdoption;
    }
    public String getGoals() {
        return goals;
    }

    public void setGoals(String goals) {
        this.goals = goals;
    }
    public String getApplication() {
        return application;
    }

    public void setApplication(String application) {
        this.application = application;
    }
    public String getProblem() {
        return problem;
    }

    public void setProblem(String problem) {
        this.problem = problem;
    }


}