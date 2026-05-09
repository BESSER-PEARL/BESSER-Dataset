





import java.util.List;
import java.util.ArrayList;

public class pycom_Import  {

    private String name;
    private String path;





    private pycom_System pycom_system;




    private pycom_Library pycom_library;


    public pycom_Import(
        String name,        String path    ) {
        this.name = name;
        this.path = path;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }

    public pycom_System getPycom_system() {
        return pycom_system;
    }

    public void setPycom_system(pycom_System pycom_system) {
        this.pycom_system = pycom_system;
    }
    public pycom_Library getPycom_library() {
        return pycom_library;
    }

    public void setPycom_library(pycom_Library pycom_library) {
        this.pycom_library = pycom_library;
    }

}