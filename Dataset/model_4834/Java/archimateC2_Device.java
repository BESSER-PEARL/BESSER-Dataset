





import java.util.List;
import java.util.ArrayList;

public class archimateC2_Device extends Node {






    private archimateC2_Network archimatec2_network;




    private archimateC2_Network archimatec2_network;




    private List<archimateC2_SystemSoftware> archimatec2_systemsoftwares;




    private archimateC2_SystemSoftware archimatec2_systemsoftware;


    public archimateC2_Device(
    ) {
        super(
        );
        this.archimatec2_systemsoftwares = new ArrayList<>();
    }

    public archimateC2_Device(
        ArrayList<archimateC2_SystemSoftware> archimatec2_systemsoftwares    ) {
        this.archimatec2_systemsoftwares = archimatec2_systemsoftwares;
    }


    public archimateC2_Network getArchimatec2_network() {
        return archimatec2_network;
    }

    public void setArchimatec2_network(archimateC2_Network archimatec2_network) {
        this.archimatec2_network = archimatec2_network;
    }
    public archimateC2_Network getArchimatec2_network() {
        return archimatec2_network;
    }

    public void setArchimatec2_network(archimateC2_Network archimatec2_network) {
        this.archimatec2_network = archimatec2_network;
    }
    public List<archimateC2_SystemSoftware> getArchimatec2_systemsoftwares() {
        return archimatec2_systemsoftwares;
    }

    public void addArchimatec2_systemsoftware(Archimatec2_systemsoftware archimatec2_systemsoftware) {
        this.archimatec2_systemsoftwares.add(archimatec2_systemsoftware);
    }
    public archimateC2_SystemSoftware getArchimatec2_systemsoftware() {
        return archimatec2_systemsoftware;
    }

    public void setArchimatec2_systemsoftware(archimateC2_SystemSoftware archimatec2_systemsoftware) {
        this.archimatec2_systemsoftware = archimatec2_systemsoftware;
    }

}