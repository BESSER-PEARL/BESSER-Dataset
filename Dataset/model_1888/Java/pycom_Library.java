





import java.util.List;
import java.util.ArrayList;

public class pycom_Library  {

    private String name;





    private pycom_System pycom_system;


    public pycom_Library(
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

}