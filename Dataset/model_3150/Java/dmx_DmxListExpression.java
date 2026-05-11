





import java.util.List;
import java.util.ArrayList;

public class dmx_DmxListExpression extends DExpression {






    private List<dmx_DExpression> dmx_dexpressions;


    public dmx_DmxListExpression(
    ) {
        super(
        );
        this.dmx_dexpressions = new ArrayList<>();
    }

    public dmx_DmxListExpression(
        ArrayList<dmx_DExpression> dmx_dexpressions    ) {
        this.dmx_dexpressions = dmx_dexpressions;
    }


    public List<dmx_DExpression> getDmx_dexpressions() {
        return dmx_dexpressions;
    }

    public void addDmx_dexpression(Dmx_dexpression dmx_dexpression) {
        this.dmx_dexpressions.add(dmx_dexpression);
    }

}