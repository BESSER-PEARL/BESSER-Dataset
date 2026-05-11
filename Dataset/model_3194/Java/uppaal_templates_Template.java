





import java.util.List;
import java.util.ArrayList;

public class uppaal_templates_Template extends AbstractTemplate {






    private List<Location> locations;




    private Location location;


    public uppaal_templates_Template(
    ) {
        super(
        );
        this.locations = new ArrayList<>();
    }

    public uppaal_templates_Template(
        ArrayList<Location> locations    ) {
        this.locations = locations;
    }


    public List<Location> getLocations() {
        return locations;
    }

    public void addLocation(Location location) {
        this.locations.add(location);
    }
    public Location getLocation() {
        return location;
    }

    public void setLocation(Location location) {
        this.location = location;
    }

}