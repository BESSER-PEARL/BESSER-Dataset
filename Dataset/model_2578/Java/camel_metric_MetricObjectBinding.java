





import java.util.List;
import java.util.ArrayList;

public class camel_metric_MetricObjectBinding  {

    private String name;





    private ExecutionContext executioncontext;


    public camel_metric_MetricObjectBinding(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ExecutionContext getExecutioncontext() {
        return executioncontext;
    }

    public void setExecutioncontext(ExecutionContext executioncontext) {
        this.executioncontext = executioncontext;
    }

}