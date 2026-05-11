





import java.util.List;
import java.util.ArrayList;

public class qm_ToolBasedInstrument extends Instrument {

    private String metric;





    private qm_Tool qm_tool;


    public qm_ToolBasedInstrument(
        String metric    ) {
        super(
        );
        this.metric = metric;
    }


    public String getMetric() {
        return metric;
    }

    public void setMetric(String metric) {
        this.metric = metric;
    }

    public qm_Tool getQm_tool() {
        return qm_tool;
    }

    public void setQm_tool(qm_Tool qm_tool) {
        this.qm_tool = qm_tool;
    }

}