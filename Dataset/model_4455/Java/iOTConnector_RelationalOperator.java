





import java.util.List;
import java.util.ArrayList;

public class iOTConnector_RelationalOperator  {

    private String value;





    private iOTConnector_SampleAction iotconnector_sampleaction;


    public iOTConnector_RelationalOperator(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public iOTConnector_SampleAction getIotconnector_sampleaction() {
        return iotconnector_sampleaction;
    }

    public void setIotconnector_sampleaction(iOTConnector_SampleAction iotconnector_sampleaction) {
        this.iotconnector_sampleaction = iotconnector_sampleaction;
    }

}