





import java.util.List;
import java.util.ArrayList;

public class behaviouralProgramMM_Literal extends Expression {

    private String Value;



    public behaviouralProgramMM_Literal(
        String Value    ) {
        super(
        );
        this.Value = Value;
    }


    public String getValue() {
        return Value;
    }

    public void setValue(String Value) {
        this.Value = Value;
    }


}