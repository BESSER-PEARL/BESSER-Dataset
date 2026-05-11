





import java.util.List;
import java.util.ArrayList;

public class migrationmodeler_Layout  {

    private int width;
    private int x;
    private int y;
    private int height;





    private migrationmodeler_AbstractRepresentation migrationmodeler_abstractrepresentation;


    public migrationmodeler_Layout(
        int width,        int x,        int y,        int height    ) {
        this.width = width;
        this.x = x;
        this.y = y;
        this.height = height;
    }


    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }
    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }
    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }

    public migrationmodeler_AbstractRepresentation getMigrationmodeler_abstractrepresentation() {
        return migrationmodeler_abstractrepresentation;
    }

    public void setMigrationmodeler_abstractrepresentation(migrationmodeler_AbstractRepresentation migrationmodeler_abstractrepresentation) {
        this.migrationmodeler_abstractrepresentation = migrationmodeler_abstractrepresentation;
    }

}