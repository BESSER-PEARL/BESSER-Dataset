





import java.util.List;
import java.util.ArrayList;

public class sADL_UnitExpression extends Expression {

    private String unit;





    private sADL_Expression sadl_expression;


    public sADL_UnitExpression(
        String unit    ) {
        super(
        );
        this.unit = unit;
    }


    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }

    public sADL_Expression getSadl_expression() {
        return sadl_expression;
    }

    public void setSadl_expression(sADL_Expression sadl_expression) {
        this.sadl_expression = sadl_expression;
    }

}