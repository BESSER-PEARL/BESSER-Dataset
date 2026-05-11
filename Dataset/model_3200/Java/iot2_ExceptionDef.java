





import java.util.List;
import java.util.ArrayList;

public class iot2_ExceptionDef extends Contained {

    private String typeCode;





    private iot2_OperationDef iot2_operationdef;


    public iot2_ExceptionDef(
        String typeCode    ) {
        super(
        );
        this.typeCode = typeCode;
    }


    public String getTypecode() {
        return typeCode;
    }

    public void setTypecode(String typeCode) {
        this.typeCode = typeCode;
    }

    public iot2_OperationDef getIot2_operationdef() {
        return iot2_operationdef;
    }

    public void setIot2_operationdef(iot2_OperationDef iot2_operationdef) {
        this.iot2_operationdef = iot2_operationdef;
    }

}