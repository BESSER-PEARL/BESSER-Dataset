





import java.util.List;
import java.util.ArrayList;

public class pycom_FunctionName  {

    private String name;





    private pycom_Function pycom_function;


    public pycom_FunctionName(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public pycom_Function getPycom_function() {
        return pycom_function;
    }

    public void setPycom_function(pycom_Function pycom_function) {
        this.pycom_function = pycom_function;
    }

}