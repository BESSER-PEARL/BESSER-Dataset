





import java.util.List;
import java.util.ArrayList;

public class connection_SAPFunctionUnit extends AbstractMetadataObject {

    private String OutputType;
    private boolean asXmlSchema;
    private String OutputTableName;



    public connection_SAPFunctionUnit(
        String OutputType,        boolean asXmlSchema,        String OutputTableName    ) {
        super(
        );
        this.OutputType = OutputType;
        this.asXmlSchema = asXmlSchema;
        this.OutputTableName = OutputTableName;
    }


    public String getOutputtype() {
        return OutputType;
    }

    public void setOutputtype(String OutputType) {
        this.OutputType = OutputType;
    }
    public boolean getAsxmlschema() {
        return asXmlSchema;
    }

    public void setAsxmlschema(boolean asXmlSchema) {
        this.asXmlSchema = asXmlSchema;
    }
    public String getOutputtablename() {
        return OutputTableName;
    }

    public void setOutputtablename(String OutputTableName) {
        this.OutputTableName = OutputTableName;
    }


}