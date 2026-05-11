





import java.util.List;
import java.util.ArrayList;

public class pycom_Board  {

    private String name;





    private pycom_System pycom_system;




    private pycom_Function pycom_function;


    public pycom_Board(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public pycom_System getPycom_system() {
        return pycom_system;
    }

    public void setPycom_system(pycom_System pycom_system) {
        this.pycom_system = pycom_system;
    }
    public pycom_Function getPycom_function() {
        return pycom_function;
    }

    public void setPycom_function(pycom_Function pycom_function) {
        this.pycom_function = pycom_function;
    }

}