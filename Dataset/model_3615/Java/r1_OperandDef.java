





import java.util.List;
import java.util.ArrayList;

public class r1_OperandDef extends Element {

    private String name;
    private String operandType;





    private r1_TypeSpecifier r1_typespecifier;


    public r1_OperandDef(
        String name,        String operandType    ) {
        super(
        );
        this.name = name;
        this.operandType = operandType;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getOperandtype() {
        return operandType;
    }

    public void setOperandtype(String operandType) {
        this.operandType = operandType;
    }

    public r1_TypeSpecifier getR1_typespecifier() {
        return r1_typespecifier;
    }

    public void setR1_typespecifier(r1_TypeSpecifier r1_typespecifier) {
        this.r1_typespecifier = r1_typespecifier;
    }

}