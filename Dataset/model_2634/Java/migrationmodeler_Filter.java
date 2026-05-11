





import java.util.List;
import java.util.ArrayList;

public class migrationmodeler_Filter  {

    private String id;
    private boolean activated;





    private migrationmodeler_Diagram migrationmodeler_diagram;


    public migrationmodeler_Filter(
        String id,        boolean activated    ) {
        this.id = id;
        this.activated = activated;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public boolean getActivated() {
        return activated;
    }

    public void setActivated(boolean activated) {
        this.activated = activated;
    }

    public migrationmodeler_Diagram getMigrationmodeler_diagram() {
        return migrationmodeler_diagram;
    }

    public void setMigrationmodeler_diagram(migrationmodeler_Diagram migrationmodeler_diagram) {
        this.migrationmodeler_diagram = migrationmodeler_diagram;
    }

}