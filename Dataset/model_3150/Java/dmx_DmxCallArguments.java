





import java.util.List;
import java.util.ArrayList;

public class dmx_DmxCallArguments  {






    private List<dmx_DExpression> dmx_dexpressions;




    private dmx_DmxMemberNavigation dmx_dmxmembernavigation;




    private dmx_DmxFunctionCall dmx_dmxfunctioncall;


    public dmx_DmxCallArguments(
    ) {
        this.dmx_dexpressions = new ArrayList<>();
    }

    public dmx_DmxCallArguments(
        ArrayList<dmx_DExpression> dmx_dexpressions    ) {
        this.dmx_dexpressions = dmx_dexpressions;
    }


    public List<dmx_DExpression> getDmx_dexpressions() {
        return dmx_dexpressions;
    }

    public void addDmx_dexpression(Dmx_dexpression dmx_dexpression) {
        this.dmx_dexpressions.add(dmx_dexpression);
    }
    public dmx_DmxMemberNavigation getDmx_dmxmembernavigation() {
        return dmx_dmxmembernavigation;
    }

    public void setDmx_dmxmembernavigation(dmx_DmxMemberNavigation dmx_dmxmembernavigation) {
        this.dmx_dmxmembernavigation = dmx_dmxmembernavigation;
    }
    public dmx_DmxFunctionCall getDmx_dmxfunctioncall() {
        return dmx_dmxfunctioncall;
    }

    public void setDmx_dmxfunctioncall(dmx_DmxFunctionCall dmx_dmxfunctioncall) {
        this.dmx_dmxfunctioncall = dmx_dmxfunctioncall;
    }

}