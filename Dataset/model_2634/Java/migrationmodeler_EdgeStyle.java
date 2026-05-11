





import java.util.List;
import java.util.ArrayList;

public class migrationmodeler_EdgeStyle  {

    private String routingStyle;





    private migrationmodeler_EdgeRepresentation migrationmodeler_edgerepresentation;


    public migrationmodeler_EdgeStyle(
        String routingStyle    ) {
        this.routingStyle = routingStyle;
    }


    public String getRoutingstyle() {
        return routingStyle;
    }

    public void setRoutingstyle(String routingStyle) {
        this.routingStyle = routingStyle;
    }

    public migrationmodeler_EdgeRepresentation getMigrationmodeler_edgerepresentation() {
        return migrationmodeler_edgerepresentation;
    }

    public void setMigrationmodeler_edgerepresentation(migrationmodeler_EdgeRepresentation migrationmodeler_edgerepresentation) {
        this.migrationmodeler_edgerepresentation = migrationmodeler_edgerepresentation;
    }

}