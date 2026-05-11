





import java.util.List;
import java.util.ArrayList;

public class iOTConnector_FilterType  {

    private String value;





    private iOTConnector_FilterAction iotconnector_filteraction;


    public iOTConnector_FilterType(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public iOTConnector_FilterAction getIotconnector_filteraction() {
        return iotconnector_filteraction;
    }

    public void setIotconnector_filteraction(iOTConnector_FilterAction iotconnector_filteraction) {
        this.iotconnector_filteraction = iotconnector_filteraction;
    }

}