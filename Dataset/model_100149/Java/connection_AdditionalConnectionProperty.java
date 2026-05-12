





import java.util.List;
import java.util.ArrayList;

public class connection_AdditionalConnectionProperty  {

    private String Value;
    private String propertyName;





    private connection_SAPConnection connection_sapconnection;


    public connection_AdditionalConnectionProperty(
        String Value,        String propertyName    ) {
        this.Value = Value;
        this.propertyName = propertyName;
    }


    public String getValue() {
        return Value;
    }

    public void setValue(String Value) {
        this.Value = Value;
    }
    public String getPropertyname() {
        return propertyName;
    }

    public void setPropertyname(String propertyName) {
        this.propertyName = propertyName;
    }

    public connection_SAPConnection getConnection_sapconnection() {
        return connection_sapconnection;
    }

    public void setConnection_sapconnection(connection_SAPConnection connection_sapconnection) {
        this.connection_sapconnection = connection_sapconnection;
    }

}