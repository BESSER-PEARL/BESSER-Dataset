





import java.util.List;
import java.util.ArrayList;

public class workflow_CustomTask extends SimpleTask {

    private String runner;



    public workflow_CustomTask(
        String runner    ) {
        super(
        );
        this.runner = runner;
    }


    public String getRunner() {
        return runner;
    }

    public void setRunner(String runner) {
        this.runner = runner;
    }


}