





import java.util.List;
import java.util.ArrayList;

public class r1_OperandDef extends Element {

    private String operandType;
    private String name;



    public r1_OperandDef(
        String operandType,        String name    ) {
        super(
        );
        this.operandType = operandType;
        this.name = name;
    }


    public String getOperandtype() {
        return operandType;
    }

    public void setOperandtype(String operandType) {
        this.operandType = operandType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}