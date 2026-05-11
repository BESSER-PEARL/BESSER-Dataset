





import java.util.List;
import java.util.ArrayList;

public class pycom_Server  {

    private String name;





    private pycom_System pycom_system;




    private List<pycom_ConditionalAction> pycom_conditionalactions;


    public pycom_Server(
        String name    ) {
        this.name = name;
        this.pycom_conditionalactions = new ArrayList<>();
    }

    public pycom_Server(
        String name        ArrayList<pycom_ConditionalAction> pycom_conditionalactions    ) {
        this.name = name;
        this.pycom_conditionalactions = pycom_conditionalactions;
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
    public List<pycom_ConditionalAction> getPycom_conditionalactions() {
        return pycom_conditionalactions;
    }

    public void addPycom_conditionalaction(Pycom_conditionalaction pycom_conditionalaction) {
        this.pycom_conditionalactions.add(pycom_conditionalaction);
    }

}