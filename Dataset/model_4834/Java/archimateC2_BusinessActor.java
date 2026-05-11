





import java.util.List;
import java.util.ArrayList;

public class archimateC2_BusinessActor extends ActiveStructure {






    private List<archimateC2_ApplicationService> archimatec2_applicationservices;




    private List<archimateC2_ApplicationInterface> archimatec2_applicationinterfaces;




    private List<archimateC2_BusinessInterface> archimatec2_businessinterfaces;




    private archimateC2_Location archimatec2_location;




    private List<archimateC2_Location> archimatec2_locations;




    private archimateC2_ApplicationService archimatec2_applicationservice;




    private archimateC2_BusinessService archimatec2_businessservice;




    private List<archimateC2_BusinessService> archimatec2_businessservices;




    private archimateC2_ApplicationInterface archimatec2_applicationinterface;




    private archimateC2_BusinessInterface archimatec2_businessinterface;


    public archimateC2_BusinessActor(
    ) {
        super(
        );
        this.archimatec2_applicationservices = new ArrayList<>();
        this.archimatec2_applicationinterfaces = new ArrayList<>();
        this.archimatec2_businessinterfaces = new ArrayList<>();
        this.archimatec2_locations = new ArrayList<>();
        this.archimatec2_businessservices = new ArrayList<>();
    }

    public archimateC2_BusinessActor(
        ArrayList<archimateC2_ApplicationService> archimatec2_applicationservices,        ArrayList<archimateC2_ApplicationInterface> archimatec2_applicationinterfaces,        ArrayList<archimateC2_BusinessInterface> archimatec2_businessinterfaces,        ArrayList<archimateC2_Location> archimatec2_locations,        ArrayList<archimateC2_BusinessService> archimatec2_businessservices    ) {
        this.archimatec2_applicationservices = archimatec2_applicationservices;
        this.archimatec2_applicationinterfaces = archimatec2_applicationinterfaces;
        this.archimatec2_businessinterfaces = archimatec2_businessinterfaces;
        this.archimatec2_locations = archimatec2_locations;
        this.archimatec2_businessservices = archimatec2_businessservices;
    }


    public List<archimateC2_ApplicationService> getArchimatec2_applicationservices() {
        return archimatec2_applicationservices;
    }

    public void addArchimatec2_applicationservice(Archimatec2_applicationservice archimatec2_applicationservice) {
        this.archimatec2_applicationservices.add(archimatec2_applicationservice);
    }
    public List<archimateC2_ApplicationInterface> getArchimatec2_applicationinterfaces() {
        return archimatec2_applicationinterfaces;
    }

    public void addArchimatec2_applicationinterface(Archimatec2_applicationinterface archimatec2_applicationinterface) {
        this.archimatec2_applicationinterfaces.add(archimatec2_applicationinterface);
    }
    public List<archimateC2_BusinessInterface> getArchimatec2_businessinterfaces() {
        return archimatec2_businessinterfaces;
    }

    public void addArchimatec2_businessinterface(Archimatec2_businessinterface archimatec2_businessinterface) {
        this.archimatec2_businessinterfaces.add(archimatec2_businessinterface);
    }
    public archimateC2_Location getArchimatec2_location() {
        return archimatec2_location;
    }

    public void setArchimatec2_location(archimateC2_Location archimatec2_location) {
        this.archimatec2_location = archimatec2_location;
    }
    public List<archimateC2_Location> getArchimatec2_locations() {
        return archimatec2_locations;
    }

    public void addArchimatec2_location(Archimatec2_location archimatec2_location) {
        this.archimatec2_locations.add(archimatec2_location);
    }
    public archimateC2_ApplicationService getArchimatec2_applicationservice() {
        return archimatec2_applicationservice;
    }

    public void setArchimatec2_applicationservice(archimateC2_ApplicationService archimatec2_applicationservice) {
        this.archimatec2_applicationservice = archimatec2_applicationservice;
    }
    public archimateC2_BusinessService getArchimatec2_businessservice() {
        return archimatec2_businessservice;
    }

    public void setArchimatec2_businessservice(archimateC2_BusinessService archimatec2_businessservice) {
        this.archimatec2_businessservice = archimatec2_businessservice;
    }
    public List<archimateC2_BusinessService> getArchimatec2_businessservices() {
        return archimatec2_businessservices;
    }

    public void addArchimatec2_businessservice(Archimatec2_businessservice archimatec2_businessservice) {
        this.archimatec2_businessservices.add(archimatec2_businessservice);
    }
    public archimateC2_ApplicationInterface getArchimatec2_applicationinterface() {
        return archimatec2_applicationinterface;
    }

    public void setArchimatec2_applicationinterface(archimateC2_ApplicationInterface archimatec2_applicationinterface) {
        this.archimatec2_applicationinterface = archimatec2_applicationinterface;
    }
    public archimateC2_BusinessInterface getArchimatec2_businessinterface() {
        return archimatec2_businessinterface;
    }

    public void setArchimatec2_businessinterface(archimateC2_BusinessInterface archimatec2_businessinterface) {
        this.archimatec2_businessinterface = archimatec2_businessinterface;
    }

}