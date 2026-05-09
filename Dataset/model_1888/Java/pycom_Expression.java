





import java.util.List;
import java.util.ArrayList;

public class pycom_Expression  {

    private int outputValue;





    private pycom_ComparisonExp pycom_comparisonexp;




    private pycom_ComparisonExp pycom_comparisonexp;




    private pycom_Function pycom_function;


    public pycom_Expression(
        int outputValue    ) {
        this.outputValue = outputValue;
    }


    public int getOutputvalue() {
        return outputValue;
    }

    public void setOutputvalue(int outputValue) {
        this.outputValue = outputValue;
    }

    public pycom_ComparisonExp getPycom_comparisonexp() {
        return pycom_comparisonexp;
    }

    public void setPycom_comparisonexp(pycom_ComparisonExp pycom_comparisonexp) {
        this.pycom_comparisonexp = pycom_comparisonexp;
    }
    public pycom_ComparisonExp getPycom_comparisonexp() {
        return pycom_comparisonexp;
    }

    public void setPycom_comparisonexp(pycom_ComparisonExp pycom_comparisonexp) {
        this.pycom_comparisonexp = pycom_comparisonexp;
    }
    public pycom_Function getPycom_function() {
        return pycom_function;
    }

    public void setPycom_function(pycom_Function pycom_function) {
        this.pycom_function = pycom_function;
    }

}