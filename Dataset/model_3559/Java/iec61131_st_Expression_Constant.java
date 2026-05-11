





import java.util.List;
import java.util.ArrayList;

public class iec61131_st_Expression_Constant extends Primary_Expression {






    private Constant constant;


    public iec61131_st_Expression_Constant(
    ) {
        super(
        );
    }



    public Constant getConstant() {
        return constant;
    }

    public void setConstant(Constant constant) {
        this.constant = constant;
    }

}