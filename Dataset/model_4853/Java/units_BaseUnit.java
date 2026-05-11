





import java.util.List;
import java.util.ArrayList;

public class units_BaseUnit  {

    private String name;





    private units_UnitLiteral units_unitliteral;


    public units_BaseUnit(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public units_UnitLiteral getUnits_unitliteral() {
        return units_unitliteral;
    }

    public void setUnits_unitliteral(units_UnitLiteral units_unitliteral) {
        this.units_unitliteral = units_unitliteral;
    }

}