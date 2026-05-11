





import java.util.List;
import java.util.ArrayList;

public class junitresult_Testrun extends AbstractAggregatedTest {

    private int ignored;
    private String project;
    private int started;



    public junitresult_Testrun(
        int ignored,        String project,        int started    ) {
        super(
        );
        this.ignored = ignored;
        this.project = project;
        this.started = started;
    }


    public int getIgnored() {
        return ignored;
    }

    public void setIgnored(int ignored) {
        this.ignored = ignored;
    }
    public String getProject() {
        return project;
    }

    public void setProject(String project) {
        this.project = project;
    }
    public int getStarted() {
        return started;
    }

    public void setStarted(int started) {
        this.started = started;
    }


}