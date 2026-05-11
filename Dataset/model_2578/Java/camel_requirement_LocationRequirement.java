





import java.util.List;
import java.util.ArrayList;

public class camel_requirement_LocationRequirement extends HardRequirement {






    private List<Location> locations;


    public camel_requirement_LocationRequirement(
    ) {
        super(
        );
        this.locations = new ArrayList<>();
    }

    public camel_requirement_LocationRequirement(
        ArrayList<Location> locations    ) {
        this.locations = locations;
    }


    public List<Location> getLocations() {
        return locations;
    }

    public void addLocation(Location location) {
        this.locations.add(location);
    }

}