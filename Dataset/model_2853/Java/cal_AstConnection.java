





import java.util.List;
import java.util.ArrayList;

public class cal_AstConnection  {

    private String outPort;
    private String inPort;



    public cal_AstConnection(
        String outPort,        String inPort    ) {
        this.outPort = outPort;
        this.inPort = inPort;
    }


    public String getOutport() {
        return outPort;
    }

    public void setOutport(String outPort) {
        this.outPort = outPort;
    }
    public String getInport() {
        return inPort;
    }

    public void setInport(String inPort) {
        this.inPort = inPort;
    }


}