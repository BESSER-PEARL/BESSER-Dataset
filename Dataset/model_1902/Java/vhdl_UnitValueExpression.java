





import java.util.List;
import java.util.ArrayList;

public class vhdl_UnitValueExpression extends ValueExpression {

    private String unit;



    public vhdl_UnitValueExpression(
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


}