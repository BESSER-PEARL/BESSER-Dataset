





import java.util.List;
import java.util.ArrayList;

public class archimateC2_BusinessRole extends ActiveStructure {

    private int rank;





    private archimateC2_ApplicationInterface archimatec2_applicationinterface;




    private List<archimateC2_BusinessService> archimatec2_businessservices;




    private List<archimateC2_BusinessBehaviorElement> archimatec2_businessbehaviorelements;




    private archimateC2_BusinessActor archimatec2_businessactor;




    private List<archimateC2_ApplicationService> archimatec2_applicationservices;




    private archimateC2_ApplicationService archimatec2_applicationservice;




    private archimateC2_BusinessService archimatec2_businessservice;




    private List<archimateC2_BusinessInterface> archimatec2_businessinterfaces;




    private List<archimateC2_BusinessInterface> archimatec2_businessinterfaces;




    private archimateC2_BusinessBehaviorElement archimatec2_businessbehaviorelement;




    private List<archimateC2_ApplicationInterface> archimatec2_applicationinterfaces;




    private archimateC2_BusinessInterface archimatec2_businessinterface;




    private archimateC2_BusinessInterface archimatec2_businessinterface;




    private List<archimateC2_BusinessActor> archimatec2_businessactors;


    public archimateC2_BusinessRole(
        int rank    ) {
        super(
        );
        this.rank = rank;
        this.archimatec2_businessservices = new ArrayList<>();
        this.archimatec2_businessbehaviorelements = new ArrayList<>();
        this.archimatec2_applicationservices = new ArrayList<>();
        this.archimatec2_businessinterfaces = new ArrayList<>();
        this.archimatec2_businessinterfaces = new ArrayList<>();
        this.archimatec2_applicationinterfaces = new ArrayList<>();
        this.archimatec2_businessactors = new ArrayList<>();
    }

    public archimateC2_BusinessRole(
        int rank        ArrayList<archimateC2_BusinessService> archimatec2_businessservices,        ArrayList<archimateC2_BusinessBehaviorElement> archimatec2_businessbehaviorelements,        ArrayList<archimateC2_ApplicationService> archimatec2_applicationservices,        ArrayList<archimateC2_BusinessInterface> archimatec2_businessinterfaces,        ArrayList<archimateC2_BusinessInterface> archimatec2_businessinterfaces,        ArrayList<archimateC2_ApplicationInterface> archimatec2_applicationinterfaces,        ArrayList<archimateC2_BusinessActor> archimatec2_businessactors    ) {
        this.rank = rank;
        this.archimatec2_businessservices = archimatec2_businessservices;
        this.archimatec2_businessbehaviorelements = archimatec2_businessbehaviorelements;
        this.archimatec2_applicationservices = archimatec2_applicationservices;
        this.archimatec2_businessinterfaces = archimatec2_businessinterfaces;
        this.archimatec2_businessinterfaces = archimatec2_businessinterfaces;
        this.archimatec2_applicationinterfaces = archimatec2_applicationinterfaces;
        this.archimatec2_businessactors = archimatec2_businessactors;
    }

    public int getRank() {
        return rank;
    }

    public void setRank(int rank) {
        this.rank = rank;
    }

    public archimateC2_ApplicationInterface getArchimatec2_applicationinterface() {
        return archimatec2_applicationinterface;
    }

    public void setArchimatec2_applicationinterface(archimateC2_ApplicationInterface archimatec2_applicationinterface) {
        this.archimatec2_applicationinterface = archimatec2_applicationinterface;
    }
    public List<archimateC2_BusinessService> getArchimatec2_businessservices() {
        return archimatec2_businessservices;
    }

    public void addArchimatec2_businessservice(Archimatec2_businessservice archimatec2_businessservice) {
        this.archimatec2_businessservices.add(archimatec2_businessservice);
    }
    public List<archimateC2_BusinessBehaviorElement> getArchimatec2_businessbehaviorelements() {
        return archimatec2_businessbehaviorelements;
    }

    public void addArchimatec2_businessbehaviorelement(Archimatec2_businessbehaviorelement archimatec2_businessbehaviorelement) {
        this.archimatec2_businessbehaviorelements.add(archimatec2_businessbehaviorelement);
    }
    public archimateC2_BusinessActor getArchimatec2_businessactor() {
        return archimatec2_businessactor;
    }

    public void setArchimatec2_businessactor(archimateC2_BusinessActor archimatec2_businessactor) {
        this.archimatec2_businessactor = archimatec2_businessactor;
    }
    public List<archimateC2_ApplicationService> getArchimatec2_applicationservices() {
        return archimatec2_applicationservices;
    }

    public void addArchimatec2_applicationservice(Archimatec2_applicationservice archimatec2_applicationservice) {
        this.archimatec2_applicationservices.add(archimatec2_applicationservice);
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
    public List<archimateC2_BusinessInterface> getArchimatec2_businessinterfaces() {
        return archimatec2_businessinterfaces;
    }

    public void addArchimatec2_businessinterface(Archimatec2_businessinterface archimatec2_businessinterface) {
        this.archimatec2_businessinterfaces.add(archimatec2_businessinterface);
    }
    public List<archimateC2_BusinessInterface> getArchimatec2_businessinterfaces() {
        return archimatec2_businessinterfaces;
    }

    public void addArchimatec2_businessinterface(Archimatec2_businessinterface archimatec2_businessinterface) {
        this.archimatec2_businessinterfaces.add(archimatec2_businessinterface);
    }
    public archimateC2_BusinessBehaviorElement getArchimatec2_businessbehaviorelement() {
        return archimatec2_businessbehaviorelement;
    }

    public void setArchimatec2_businessbehaviorelement(archimateC2_BusinessBehaviorElement archimatec2_businessbehaviorelement) {
        this.archimatec2_businessbehaviorelement = archimatec2_businessbehaviorelement;
    }
    public List<archimateC2_ApplicationInterface> getArchimatec2_applicationinterfaces() {
        return archimatec2_applicationinterfaces;
    }

    public void addArchimatec2_applicationinterface(Archimatec2_applicationinterface archimatec2_applicationinterface) {
        this.archimatec2_applicationinterfaces.add(archimatec2_applicationinterface);
    }
    public archimateC2_BusinessInterface getArchimatec2_businessinterface() {
        return archimatec2_businessinterface;
    }

    public void setArchimatec2_businessinterface(archimateC2_BusinessInterface archimatec2_businessinterface) {
        this.archimatec2_businessinterface = archimatec2_businessinterface;
    }
    public archimateC2_BusinessInterface getArchimatec2_businessinterface() {
        return archimatec2_businessinterface;
    }

    public void setArchimatec2_businessinterface(archimateC2_BusinessInterface archimatec2_businessinterface) {
        this.archimatec2_businessinterface = archimatec2_businessinterface;
    }
    public List<archimateC2_BusinessActor> getArchimatec2_businessactors() {
        return archimatec2_businessactors;
    }

    public void addArchimatec2_businessactor(Archimatec2_businessactor archimatec2_businessactor) {
        this.archimatec2_businessactors.add(archimatec2_businessactor);
    }

}