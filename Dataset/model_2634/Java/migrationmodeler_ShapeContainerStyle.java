





import java.util.List;
import java.util.ArrayList;

public class migrationmodeler_ShapeContainerStyle extends ContainerStyle {

    private String shape;





    private migrationmodeler_Color migrationmodeler_color;


    public migrationmodeler_ShapeContainerStyle(
        String shape    ) {
        super(
        );
        this.shape = shape;
    }


    public String getShape() {
        return shape;
    }

    public void setShape(String shape) {
        this.shape = shape;
    }

    public migrationmodeler_Color getMigrationmodeler_color() {
        return migrationmodeler_color;
    }

    public void setMigrationmodeler_color(migrationmodeler_Color migrationmodeler_color) {
        this.migrationmodeler_color = migrationmodeler_color;
    }

}