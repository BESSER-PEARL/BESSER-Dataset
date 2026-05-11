





import java.util.List;
import java.util.ArrayList;

public class smarthome_EvaluatingNode  {






    private smarthome_SmartHome smarthome_smarthome;




    private List<smarthome_FilterConnection> smarthome_filterconnections;




    private List<smarthome_CommandConnection> smarthome_commandconnections;


    public smarthome_EvaluatingNode(
    ) {
        this.smarthome_filterconnections = new ArrayList<>();
        this.smarthome_commandconnections = new ArrayList<>();
    }

    public smarthome_EvaluatingNode(
        ArrayList<smarthome_FilterConnection> smarthome_filterconnections,        ArrayList<smarthome_CommandConnection> smarthome_commandconnections    ) {
        this.smarthome_filterconnections = smarthome_filterconnections;
        this.smarthome_commandconnections = smarthome_commandconnections;
    }


    public smarthome_SmartHome getSmarthome_smarthome() {
        return smarthome_smarthome;
    }

    public void setSmarthome_smarthome(smarthome_SmartHome smarthome_smarthome) {
        this.smarthome_smarthome = smarthome_smarthome;
    }
    public List<smarthome_FilterConnection> getSmarthome_filterconnections() {
        return smarthome_filterconnections;
    }

    public void addSmarthome_filterconnection(Smarthome_filterconnection smarthome_filterconnection) {
        this.smarthome_filterconnections.add(smarthome_filterconnection);
    }
    public List<smarthome_CommandConnection> getSmarthome_commandconnections() {
        return smarthome_commandconnections;
    }

    public void addSmarthome_commandconnection(Smarthome_commandconnection smarthome_commandconnection) {
        this.smarthome_commandconnections.add(smarthome_commandconnection);
    }

}