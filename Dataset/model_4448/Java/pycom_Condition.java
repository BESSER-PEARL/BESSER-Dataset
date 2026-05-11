





import java.util.List;
import java.util.ArrayList;

public class pycom_Condition  {

    private String operator;





    private pycom_ConditionalAction pycom_conditionalaction;




    private pycom_Condition pycom_condition;


    public pycom_Condition(
        String operator    ) {
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public pycom_ConditionalAction getPycom_conditionalaction() {
        return pycom_conditionalaction;
    }

    public void setPycom_conditionalaction(pycom_ConditionalAction pycom_conditionalaction) {
        this.pycom_conditionalaction = pycom_conditionalaction;
    }
    public pycom_Condition getPycom_condition() {
        return pycom_condition;
    }

    public void setPycom_condition(pycom_Condition pycom_condition) {
        this.pycom_condition = pycom_condition;
    }

}