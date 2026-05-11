





import java.util.List;
import java.util.ArrayList;

public class SmartHome_RuleComposant  {

    private String operator;





    private SmartHome_IotComponent smarthome_iotcomponent;




    private SmartHome_Rule smarthome_rule;




    private SmartHome_Rule smarthome_rule;


    public SmartHome_RuleComposant(
        String operator    ) {
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public SmartHome_IotComponent getSmarthome_iotcomponent() {
        return smarthome_iotcomponent;
    }

    public void setSmarthome_iotcomponent(SmartHome_IotComponent smarthome_iotcomponent) {
        this.smarthome_iotcomponent = smarthome_iotcomponent;
    }
    public SmartHome_Rule getSmarthome_rule() {
        return smarthome_rule;
    }

    public void setSmarthome_rule(SmartHome_Rule smarthome_rule) {
        this.smarthome_rule = smarthome_rule;
    }
    public SmartHome_Rule getSmarthome_rule() {
        return smarthome_rule;
    }

    public void setSmarthome_rule(SmartHome_Rule smarthome_rule) {
        this.smarthome_rule = smarthome_rule;
    }

}