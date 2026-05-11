





import java.util.List;
import java.util.ArrayList;

public class idl_Preproc_Pragma_Conn_Type extends Preproc_Pragma {

    private String valueConnType;
    private String valuePort;



    public idl_Preproc_Pragma_Conn_Type(
        String valueConnType,        String valuePort    ) {
        super(
        );
        this.valueConnType = valueConnType;
        this.valuePort = valuePort;
    }


    public String getValueconntype() {
        return valueConnType;
    }

    public void setValueconntype(String valueConnType) {
        this.valueConnType = valueConnType;
    }
    public String getValueport() {
        return valuePort;
    }

    public void setValueport(String valuePort) {
        this.valuePort = valuePort;
    }


}