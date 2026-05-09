





import java.util.List;
import java.util.ArrayList;

public class uma_PracticeDescription extends ContentDescription {

    private String goals;
    private String additionalInfo;
    private String problem;
    private String background;
    private String application;
    private String levelsOfAdoption;



    public uma_PracticeDescription(
        String goals,        String additionalInfo,        String problem,        String background,        String application,        String levelsOfAdoption    ) {
        super(
        );
        this.goals = goals;
        this.additionalInfo = additionalInfo;
        this.problem = problem;
        this.background = background;
        this.application = application;
        this.levelsOfAdoption = levelsOfAdoption;
    }


    public String getGoals() {
        return goals;
    }

    public void setGoals(String goals) {
        this.goals = goals;
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
    public String getBackground() {
        return background;
    }

    public void setBackground(String background) {
        this.background = background;
    }
    public String getApplication() {
        return application;
    }

    public void setApplication(String application) {
        this.application = application;
    }
    public String getLevelsofadoption() {
        return levelsOfAdoption;
    }

    public void setLevelsofadoption(String levelsOfAdoption) {
        this.levelsOfAdoption = levelsOfAdoption;
    }


}