





import java.util.List;
import java.util.ArrayList;

public class iOTConnector_BitwiseOperator  {

    private String value;





    private iOTConnector_FilterExp iotconnector_filterexp;


    public iOTConnector_BitwiseOperator(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public iOTConnector_FilterExp getIotconnector_filterexp() {
        return iotconnector_filterexp;
    }

    public void setIotconnector_filterexp(iOTConnector_FilterExp iotconnector_filterexp) {
        this.iotconnector_filterexp = iotconnector_filterexp;
    }

}