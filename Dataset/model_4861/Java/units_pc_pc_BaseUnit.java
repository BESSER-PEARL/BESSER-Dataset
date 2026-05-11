





import java.util.List;
import java.util.ArrayList;

public class units_pc_pc_BaseUnit  {

    private String name;





    private units_pc_pc_UnitLiteral units_pc_pc_unitliteral;


    public units_pc_pc_BaseUnit(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public units_pc_pc_UnitLiteral getUnits_pc_pc_unitliteral() {
        return units_pc_pc_unitliteral;
    }

    public void setUnits_pc_pc_unitliteral(units_pc_pc_UnitLiteral units_pc_pc_unitliteral) {
        this.units_pc_pc_unitliteral = units_pc_pc_unitliteral;
    }

}