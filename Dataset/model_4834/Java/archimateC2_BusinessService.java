





import java.util.List;
import java.util.ArrayList;

public class archimateC2_BusinessService extends BehaviorElement {






    private List<archimateC2_ApplicationInterface> archimatec2_applicationinterfaces;




    private archimateC2_ApplicationInterface archimatec2_applicationinterface;


    public archimateC2_BusinessService(
    ) {
        super(
        );
        this.archimatec2_applicationinterfaces = new ArrayList<>();
    }

    public archimateC2_BusinessService(
        ArrayList<archimateC2_ApplicationInterface> archimatec2_applicationinterfaces    ) {
        this.archimatec2_applicationinterfaces = archimatec2_applicationinterfaces;
    }


    public List<archimateC2_ApplicationInterface> getArchimatec2_applicationinterfaces() {
        return archimatec2_applicationinterfaces;
    }

    public void addArchimatec2_applicationinterface(Archimatec2_applicationinterface archimatec2_applicationinterface) {
        this.archimatec2_applicationinterfaces.add(archimatec2_applicationinterface);
    }
    public archimateC2_ApplicationInterface getArchimatec2_applicationinterface() {
        return archimatec2_applicationinterface;
    }

    public void setArchimatec2_applicationinterface(archimateC2_ApplicationInterface archimatec2_applicationinterface) {
        this.archimatec2_applicationinterface = archimatec2_applicationinterface;
    }

}