





import java.util.List;
import java.util.ArrayList;

public class analysis_bottlenecks_DoubleToBottlenecksReportMap  {

    private String key;





    private BottlenecksReport bottlenecksreport;


    public analysis_bottlenecks_DoubleToBottlenecksReportMap(
        String key    ) {
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public BottlenecksReport getBottlenecksreport() {
        return bottlenecksreport;
    }

    public void setBottlenecksreport(BottlenecksReport bottlenecksreport) {
        this.bottlenecksreport = bottlenecksreport;
    }

}