





import java.util.List;
import java.util.ArrayList;

public class junitresult_Testrun extends AbstractAggregatedTest {

    private int started;
    private String project;
    private int ignored;



    public junitresult_Testrun(
        int started,        String project,        int ignored    ) {
        super(
        );
        this.started = started;
        this.project = project;
        this.ignored = ignored;
    }


    public int getStarted() {
        return started;
    }

    public void setStarted(int started) {
        this.started = started;
    }
    public String getProject() {
        return project;
    }

    public void setProject(String project) {
        this.project = project;
    }
    public int getIgnored() {
        return ignored;
    }

    public void setIgnored(int ignored) {
        this.ignored = ignored;
    }


}