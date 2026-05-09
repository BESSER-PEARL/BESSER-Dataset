





import java.util.List;
import java.util.ArrayList;

public class pycom_LogicExp  {






    private pycom_Condition pycom_condition;




    private pycom_ComparisonExp pycom_comparisonexp;


    public pycom_LogicExp(
    ) {
    }



    public pycom_Condition getPycom_condition() {
        return pycom_condition;
    }

    public void setPycom_condition(pycom_Condition pycom_condition) {
        this.pycom_condition = pycom_condition;
    }
    public pycom_ComparisonExp getPycom_comparisonexp() {
        return pycom_comparisonexp;
    }

    public void setPycom_comparisonexp(pycom_ComparisonExp pycom_comparisonexp) {
        this.pycom_comparisonexp = pycom_comparisonexp;
    }

}