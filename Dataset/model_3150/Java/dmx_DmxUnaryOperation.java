





import java.util.List;
import java.util.ArrayList;

public class dmx_DmxUnaryOperation extends DExpression {

    private String operator;





    private dmx_DExpression dmx_dexpression;


    public dmx_DmxUnaryOperation(
        String operator    ) {
        super(
        );
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public dmx_DExpression getDmx_dexpression() {
        return dmx_dexpression;
    }

    public void setDmx_dexpression(dmx_DExpression dmx_dexpression) {
        this.dmx_dexpression = dmx_dexpression;
    }

}