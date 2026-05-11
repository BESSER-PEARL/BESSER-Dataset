





import java.util.List;
import java.util.ArrayList;

public class r1_FunctionDef extends ExpressionDef {






    private List<r1_OperandDef> r1_operanddefs;


    public r1_FunctionDef(
    ) {
        super(
        );
        this.r1_operanddefs = new ArrayList<>();
    }

    public r1_FunctionDef(
        ArrayList<r1_OperandDef> r1_operanddefs    ) {
        this.r1_operanddefs = r1_operanddefs;
    }


    public List<r1_OperandDef> getR1_operanddefs() {
        return r1_operanddefs;
    }

    public void addR1_operanddef(R1_operanddef r1_operanddef) {
        this.r1_operanddefs.add(r1_operanddef);
    }

}