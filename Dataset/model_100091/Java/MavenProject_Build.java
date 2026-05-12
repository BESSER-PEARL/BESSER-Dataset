





import java.util.List;
import java.util.ArrayList;

public class MavenProject_Build  {

    private String unitTestSourceDirectory;
    private String defaultGoal;
    private String sourceDirectory;



    public MavenProject_Build(
        String unitTestSourceDirectory,        String defaultGoal,        String sourceDirectory    ) {
        this.unitTestSourceDirectory = unitTestSourceDirectory;
        this.defaultGoal = defaultGoal;
        this.sourceDirectory = sourceDirectory;
    }


    public String getUnittestsourcedirectory() {
        return unitTestSourceDirectory;
    }

    public void setUnittestsourcedirectory(String unitTestSourceDirectory) {
        this.unitTestSourceDirectory = unitTestSourceDirectory;
    }
    public String getDefaultgoal() {
        return defaultGoal;
    }

    public void setDefaultgoal(String defaultGoal) {
        this.defaultGoal = defaultGoal;
    }
    public String getSourcedirectory() {
        return sourceDirectory;
    }

    public void setSourcedirectory(String sourceDirectory) {
        this.sourceDirectory = sourceDirectory;
    }


}