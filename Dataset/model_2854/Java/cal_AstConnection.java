





import java.util.List;
import java.util.ArrayList;

public class cal_AstConnection  {

    private String inPort;
    private String outPort;





    private cal_AstStructure cal_aststructure;


    public cal_AstConnection(
        String inPort,        String outPort    ) {
        this.inPort = inPort;
        this.outPort = outPort;
    }


    public String getInport() {
        return inPort;
    }

    public void setInport(String inPort) {
        this.inPort = inPort;
    }
    public String getOutport() {
        return outPort;
    }

    public void setOutport(String outPort) {
        this.outPort = outPort;
    }

    public cal_AstStructure getCal_aststructure() {
        return cal_aststructure;
    }

    public void setCal_aststructure(cal_AstStructure cal_aststructure) {
        this.cal_aststructure = cal_aststructure;
    }

}