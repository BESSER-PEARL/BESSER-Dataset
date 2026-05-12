





import java.util.List;
import java.util.ArrayList;

public class query_XMLValueFunctionValidateAccordingToIdentifier extends XMLValueFunctionValidateAccordingTo {

    private String registeredXMLSchemaName;
    private String schemaName;



    public query_XMLValueFunctionValidateAccordingToIdentifier(
        String registeredXMLSchemaName,        String schemaName    ) {
        super(
        );
        this.registeredXMLSchemaName = registeredXMLSchemaName;
        this.schemaName = schemaName;
    }


    public String getRegisteredxmlschemaname() {
        return registeredXMLSchemaName;
    }

    public void setRegisteredxmlschemaname(String registeredXMLSchemaName) {
        this.registeredXMLSchemaName = registeredXMLSchemaName;
    }
    public String getSchemaname() {
        return schemaName;
    }

    public void setSchemaname(String schemaName) {
        this.schemaName = schemaName;
    }


}