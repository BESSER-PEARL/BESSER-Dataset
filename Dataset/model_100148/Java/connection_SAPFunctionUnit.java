





import java.util.List;
import java.util.ArrayList;

public class connection_SAPFunctionUnit extends AbstractMetadataObject {

    private String OutputType;
    private String OutputTableName;



    public connection_SAPFunctionUnit(
        String OutputType,        String OutputTableName    ) {
        super(
        );
        this.OutputType = OutputType;
        this.OutputTableName = OutputTableName;
    }


    public String getOutputtype() {
        return OutputType;
    }

    public void setOutputtype(String OutputType) {
        this.OutputType = OutputType;
    }
    public String getOutputtablename() {
        return OutputTableName;
    }

    public void setOutputtablename(String OutputTableName) {
        this.OutputTableName = OutputTableName;
    }


}