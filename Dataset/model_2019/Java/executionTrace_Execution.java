





import java.util.List;
import java.util.ArrayList;

public class executionTrace_Execution  {

    private String executionStartedTimeStamp;
    private String executionFinishedTimeStamp;
    private String executionTimeMsec;
    private String executionTime;





    private executionTrace_Execution executiontrace_execution;




    private executionTrace_ExecutionTrace executiontrace_executiontrace;




    private List<executionTrace_Execution> executiontrace_executions;


    public executionTrace_Execution(
        String executionStartedTimeStamp,        String executionFinishedTimeStamp,        String executionTimeMsec,        String executionTime    ) {
        this.executionStartedTimeStamp = executionStartedTimeStamp;
        this.executionFinishedTimeStamp = executionFinishedTimeStamp;
        this.executionTimeMsec = executionTimeMsec;
        this.executionTime = executionTime;
        this.executiontrace_executions = new ArrayList<>();
    }

    public executionTrace_Execution(
        String executionStartedTimeStamp,        String executionFinishedTimeStamp,        String executionTimeMsec,        String executionTime        ArrayList<executionTrace_Execution> executiontrace_executions    ) {
        this.executionStartedTimeStamp = executionStartedTimeStamp;
        this.executionFinishedTimeStamp = executionFinishedTimeStamp;
        this.executionTimeMsec = executionTimeMsec;
        this.executionTime = executionTime;
        this.executiontrace_executions = executiontrace_executions;
    }

    public String getExecutionstartedtimestamp() {
        return executionStartedTimeStamp;
    }

    public void setExecutionstartedtimestamp(String executionStartedTimeStamp) {
        this.executionStartedTimeStamp = executionStartedTimeStamp;
    }
    public String getExecutionfinishedtimestamp() {
        return executionFinishedTimeStamp;
    }

    public void setExecutionfinishedtimestamp(String executionFinishedTimeStamp) {
        this.executionFinishedTimeStamp = executionFinishedTimeStamp;
    }
    public String getExecutiontimemsec() {
        return executionTimeMsec;
    }

    public void setExecutiontimemsec(String executionTimeMsec) {
        this.executionTimeMsec = executionTimeMsec;
    }
    public String getExecutiontime() {
        return executionTime;
    }

    public void setExecutiontime(String executionTime) {
        this.executionTime = executionTime;
    }

    public executionTrace_Execution getExecutiontrace_execution() {
        return executiontrace_execution;
    }

    public void setExecutiontrace_execution(executionTrace_Execution executiontrace_execution) {
        this.executiontrace_execution = executiontrace_execution;
    }
    public executionTrace_ExecutionTrace getExecutiontrace_executiontrace() {
        return executiontrace_executiontrace;
    }

    public void setExecutiontrace_executiontrace(executionTrace_ExecutionTrace executiontrace_executiontrace) {
        this.executiontrace_executiontrace = executiontrace_executiontrace;
    }
    public List<executionTrace_Execution> getExecutiontrace_executions() {
        return executiontrace_executions;
    }

    public void addExecutiontrace_execution(Executiontrace_execution executiontrace_execution) {
        this.executiontrace_executions.add(executiontrace_execution);
    }

}