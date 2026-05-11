





import java.util.List;
import java.util.ArrayList;

public class migrationmodeler_Point  {

    private int y;
    private int x;





    private migrationmodeler_EdgeRepresentation migrationmodeler_edgerepresentation;


    public migrationmodeler_Point(
        int y,        int x    ) {
        this.y = y;
        this.x = x;
    }


    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }
    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }

    public migrationmodeler_EdgeRepresentation getMigrationmodeler_edgerepresentation() {
        return migrationmodeler_edgerepresentation;
    }

    public void setMigrationmodeler_edgerepresentation(migrationmodeler_EdgeRepresentation migrationmodeler_edgerepresentation) {
        this.migrationmodeler_edgerepresentation = migrationmodeler_edgerepresentation;
    }

}