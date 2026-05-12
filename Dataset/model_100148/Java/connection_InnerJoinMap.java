





import java.util.List;
import java.util.ArrayList;

public class connection_InnerJoinMap  {

    private String key;
    private String value;





    private connection_ValidationRulesConnection connection_validationrulesconnection;


    public connection_InnerJoinMap(
        String key,        String value    ) {
        this.key = key;
        this.value = value;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public connection_ValidationRulesConnection getConnection_validationrulesconnection() {
        return connection_validationrulesconnection;
    }

    public void setConnection_validationrulesconnection(connection_ValidationRulesConnection connection_validationrulesconnection) {
        this.connection_validationrulesconnection = connection_validationrulesconnection;
    }

}