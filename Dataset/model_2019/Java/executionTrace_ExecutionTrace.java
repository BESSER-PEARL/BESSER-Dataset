





import java.util.List;
import java.util.ArrayList;

public class executionTrace_ExecutionTrace  {

    private String totalExecutionTimeMsec;
    private String totalExecutionTime;
    private String description;



    public executionTrace_ExecutionTrace(
        String totalExecutionTimeMsec,        String totalExecutionTime,        String description    ) {
        this.totalExecutionTimeMsec = totalExecutionTimeMsec;
        this.totalExecutionTime = totalExecutionTime;
        this.description = description;
    }


    public String getTotalexecutiontimemsec() {
        return totalExecutionTimeMsec;
    }

    public void setTotalexecutiontimemsec(String totalExecutionTimeMsec) {
        this.totalExecutionTimeMsec = totalExecutionTimeMsec;
    }
    public String getTotalexecutiontime() {
        return totalExecutionTime;
    }

    public void setTotalexecutiontime(String totalExecutionTime) {
        this.totalExecutionTime = totalExecutionTime;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}