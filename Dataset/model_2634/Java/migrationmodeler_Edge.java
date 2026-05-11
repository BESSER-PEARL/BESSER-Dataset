





import java.util.List;
import java.util.ArrayList;

public class migrationmodeler_Edge extends GraphicalElement {






    private List<migrationmodeler_EdgeRepresentation> migrationmodeler_edgerepresentations;




    private migrationmodeler_Diagram migrationmodeler_diagram;


    public migrationmodeler_Edge(
    ) {
        super(
        );
        this.migrationmodeler_edgerepresentations = new ArrayList<>();
    }

    public migrationmodeler_Edge(
        ArrayList<migrationmodeler_EdgeRepresentation> migrationmodeler_edgerepresentations    ) {
        this.migrationmodeler_edgerepresentations = migrationmodeler_edgerepresentations;
    }


    public List<migrationmodeler_EdgeRepresentation> getMigrationmodeler_edgerepresentations() {
        return migrationmodeler_edgerepresentations;
    }

    public void addMigrationmodeler_edgerepresentation(Migrationmodeler_edgerepresentation migrationmodeler_edgerepresentation) {
        this.migrationmodeler_edgerepresentations.add(migrationmodeler_edgerepresentation);
    }
    public migrationmodeler_Diagram getMigrationmodeler_diagram() {
        return migrationmodeler_diagram;
    }

    public void setMigrationmodeler_diagram(migrationmodeler_Diagram migrationmodeler_diagram) {
        this.migrationmodeler_diagram = migrationmodeler_diagram;
    }

}