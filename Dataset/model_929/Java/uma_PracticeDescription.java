





import java.util.List;
import java.util.ArrayList;

public class uma_PracticeDescription extends ContentDescription {

    private String additionalInfo;
    private String problem;
    private String application;
    private String goals;
    private String background;
    private String levelsOfAdoption;



    public uma_PracticeDescription(
        String additionalInfo,        String problem,        String application,        String goals,        String background,        String levelsOfAdoption    ) {
        super(
        );
        this.additionalInfo = additionalInfo;
        this.problem = problem;
        this.application = application;
        this.goals = goals;
        this.background = background;
        this.levelsOfAdoption = levelsOfAdoption;
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
    public String getApplication() {
        return application;
    }

    public void setApplication(String application) {
        this.application = application;
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


}