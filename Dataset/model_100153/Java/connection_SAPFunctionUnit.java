





import java.util.List;
import java.util.ArrayList;

public class connection_SAPFunctionUnit extends AbstractMetadataObject {

    private String OutputTableName;
    private String OutputType;



    public connection_SAPFunctionUnit(
        String OutputTableName,        String OutputType    ) {
        super(
        );
        this.OutputTableName = OutputTableName;
        this.OutputType = OutputType;
    }


    public String getOutputtablename() {
        return OutputTableName;
    }

    public void setOutputtablename(String OutputTableName) {
        this.OutputTableName = OutputTableName;
    }
    public String getOutputtype() {
        return OutputType;
    }

    public void setOutputtype(String OutputType) {
        this.OutputType = OutputType;
    }


}