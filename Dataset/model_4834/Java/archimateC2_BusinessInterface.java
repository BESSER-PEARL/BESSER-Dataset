





import java.util.List;
import java.util.ArrayList;

public class archimateC2_BusinessInterface extends ActiveStructure {






    private List<archimateC2_BusinessService> archimatec2_businessservices;




    private archimateC2_BusinessService archimatec2_businessservice;


    public archimateC2_BusinessInterface(
    ) {
        super(
        );
        this.archimatec2_businessservices = new ArrayList<>();
    }

    public archimateC2_BusinessInterface(
        ArrayList<archimateC2_BusinessService> archimatec2_businessservices    ) {
        this.archimatec2_businessservices = archimatec2_businessservices;
    }


    public List<archimateC2_BusinessService> getArchimatec2_businessservices() {
        return archimatec2_businessservices;
    }

    public void addArchimatec2_businessservice(Archimatec2_businessservice archimatec2_businessservice) {
        this.archimatec2_businessservices.add(archimatec2_businessservice);
    }
    public archimateC2_BusinessService getArchimatec2_businessservice() {
        return archimatec2_businessservice;
    }

    public void setArchimatec2_businessservice(archimateC2_BusinessService archimatec2_businessservice) {
        this.archimatec2_businessservice = archimatec2_businessservice;
    }

}