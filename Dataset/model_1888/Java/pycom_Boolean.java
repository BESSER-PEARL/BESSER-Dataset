





import java.util.List;
import java.util.ArrayList;

public class pycom_Boolean  {

    private String value;





    private pycom_LogicExp pycom_logicexp;


    public pycom_Boolean(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public pycom_LogicExp getPycom_logicexp() {
        return pycom_logicexp;
    }

    public void setPycom_logicexp(pycom_LogicExp pycom_logicexp) {
        this.pycom_logicexp = pycom_logicexp;
    }

}