





import java.util.List;
import java.util.ArrayList;

public class conf101_Admin extends NamedElement {






    private conf101_System conf101_system;




    private List<conf101_Location> conf101_locations;


    public conf101_Admin(
    ) {
        super(
        );
        this.conf101_locations = new ArrayList<>();
    }

    public conf101_Admin(
        ArrayList<conf101_Location> conf101_locations    ) {
        this.conf101_locations = conf101_locations;
    }


    public conf101_System getConf101_system() {
        return conf101_system;
    }

    public void setConf101_system(conf101_System conf101_system) {
        this.conf101_system = conf101_system;
    }
    public List<conf101_Location> getConf101_locations() {
        return conf101_locations;
    }

    public void addConf101_location(Conf101_location conf101_location) {
        this.conf101_locations.add(conf101_location);
    }

}