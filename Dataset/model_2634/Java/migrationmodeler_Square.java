





import java.util.List;
import java.util.ArrayList;

public class migrationmodeler_Square extends NodeStyle {

    private String height;
    private String width;





    private migrationmodeler_Color migrationmodeler_color;


    public migrationmodeler_Square(
        String height,        String width    ) {
        super(
        );
        this.height = height;
        this.width = width;
    }


    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }

    public migrationmodeler_Color getMigrationmodeler_color() {
        return migrationmodeler_color;
    }

    public void setMigrationmodeler_color(migrationmodeler_Color migrationmodeler_color) {
        this.migrationmodeler_color = migrationmodeler_color;
    }

}