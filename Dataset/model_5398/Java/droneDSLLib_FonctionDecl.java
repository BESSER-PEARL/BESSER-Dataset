





import java.util.List;
import java.util.ArrayList;

public class droneDSLLib_FonctionDecl  {

    private String name;





    private droneDSLLib_Model dronedsllib_model;


    public droneDSLLib_FonctionDecl(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public droneDSLLib_Model getDronedsllib_model() {
        return dronedsllib_model;
    }

    public void setDronedsllib_model(droneDSLLib_Model dronedsllib_model) {
        this.dronedsllib_model = dronedsllib_model;
    }

}