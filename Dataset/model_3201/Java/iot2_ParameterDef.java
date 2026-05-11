





import java.util.List;
import java.util.ArrayList;

public class iot2_ParameterDef extends Typed {

    private String identifier;
    private String direction;





    private iot2_OperationDef iot2_operationdef;


    public iot2_ParameterDef(
        String identifier,        String direction    ) {
        super(
        );
        this.identifier = identifier;
        this.direction = direction;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }

    public iot2_OperationDef getIot2_operationdef() {
        return iot2_operationdef;
    }

    public void setIot2_operationdef(iot2_OperationDef iot2_operationdef) {
        this.iot2_operationdef = iot2_operationdef;
    }

}