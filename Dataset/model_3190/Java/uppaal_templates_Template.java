





import java.util.List;
import java.util.ArrayList;

public class uppaal_templates_Template extends AbstractTemplate {






    private List<Location> locations;




    private List<Edge> edges;




    private LocalDeclarations localdeclarations;




    private Location location;


    public uppaal_templates_Template(
    ) {
        super(
        );
        this.locations = new ArrayList<>();
        this.edges = new ArrayList<>();
    }

    public uppaal_templates_Template(
        ArrayList<Location> locations,        ArrayList<Edge> edges    ) {
        this.locations = locations;
        this.edges = edges;
    }


    public List<Location> getLocations() {
        return locations;
    }

    public void addLocation(Location location) {
        this.locations.add(location);
    }
    public List<Edge> getEdges() {
        return edges;
    }

    public void addEdge(Edge edge) {
        this.edges.add(edge);
    }
    public LocalDeclarations getLocaldeclarations() {
        return localdeclarations;
    }

    public void setLocaldeclarations(LocalDeclarations localdeclarations) {
        this.localdeclarations = localdeclarations;
    }
    public Location getLocation() {
        return location;
    }

    public void setLocation(Location location) {
        this.location = location;
    }

}