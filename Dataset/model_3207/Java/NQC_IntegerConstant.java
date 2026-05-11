





import java.util.List;
import java.util.ArrayList;

public class NQC_IntegerConstant extends ConstantExpression {

    private int Value;





    private NQC_Variable nqc_variable;


    public NQC_IntegerConstant(
        int Value    ) {
        super(
        );
        this.Value = Value;
    }


    public int getValue() {
        return Value;
    }

    public void setValue(int Value) {
        this.Value = Value;
    }

    public NQC_Variable getNqc_variable() {
        return nqc_variable;
    }

    public void setNqc_variable(NQC_Variable nqc_variable) {
        this.nqc_variable = nqc_variable;
    }

}