





import java.util.List;
import java.util.ArrayList;

public class trace_Properties extends EModelElement {

    private String index;
    private String absoluteDeadline;
    private String remainingTime;
    private String executionTime;
    private String range;
    private String blockingTime;
    private String responseTime;





    private trace_Slice trace_slice;


    public trace_Properties(
        String index,        String absoluteDeadline,        String remainingTime,        String executionTime,        String range,        String blockingTime,        String responseTime    ) {
        super(
        );
        this.index = index;
        this.absoluteDeadline = absoluteDeadline;
        this.remainingTime = remainingTime;
        this.executionTime = executionTime;
        this.range = range;
        this.blockingTime = blockingTime;
        this.responseTime = responseTime;
    }


    public String getIndex() {
        return index;
    }

    public void setIndex(String index) {
        this.index = index;
    }
    public String getAbsolutedeadline() {
        return absoluteDeadline;
    }

    public void setAbsolutedeadline(String absoluteDeadline) {
        this.absoluteDeadline = absoluteDeadline;
    }
    public String getRemainingtime() {
        return remainingTime;
    }

    public void setRemainingtime(String remainingTime) {
        this.remainingTime = remainingTime;
    }
    public String getExecutiontime() {
        return executionTime;
    }

    public void setExecutiontime(String executionTime) {
        this.executionTime = executionTime;
    }
    public String getRange() {
        return range;
    }

    public void setRange(String range) {
        this.range = range;
    }
    public String getBlockingtime() {
        return blockingTime;
    }

    public void setBlockingtime(String blockingTime) {
        this.blockingTime = blockingTime;
    }
    public String getResponsetime() {
        return responseTime;
    }

    public void setResponsetime(String responseTime) {
        this.responseTime = responseTime;
    }

    public trace_Slice getTrace_slice() {
        return trace_slice;
    }

    public void setTrace_slice(trace_Slice trace_slice) {
        this.trace_slice = trace_slice;
    }

}