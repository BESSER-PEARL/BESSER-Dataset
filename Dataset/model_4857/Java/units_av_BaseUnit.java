





import java.util.List;
import java.util.ArrayList;

public class units_av_BaseUnit  {

    private String name;





    private units_av_UnitLiteral units_av_unitliteral;




    private units_av_UnitRepository units_av_unitrepository;


    public units_av_BaseUnit(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public units_av_UnitLiteral getUnits_av_unitliteral() {
        return units_av_unitliteral;
    }

    public void setUnits_av_unitliteral(units_av_UnitLiteral units_av_unitliteral) {
        this.units_av_unitliteral = units_av_unitliteral;
    }
    public units_av_UnitRepository getUnits_av_unitrepository() {
        return units_av_unitrepository;
    }

    public void setUnits_av_unitrepository(units_av_UnitRepository units_av_unitrepository) {
        this.units_av_unitrepository = units_av_unitrepository;
    }

}