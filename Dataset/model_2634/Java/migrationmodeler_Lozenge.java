





import java.util.List;
import java.util.ArrayList;

public class migrationmodeler_Lozenge extends NodeStyle {

    private String width;
    private String height;





    private migrationmodeler_Color migrationmodeler_color;


    public migrationmodeler_Lozenge(
        String width,        String height    ) {
        super(
        );
        this.width = width;
        this.height = height;
    }


    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }

    public migrationmodeler_Color getMigrationmodeler_color() {
        return migrationmodeler_color;
    }

    public void setMigrationmodeler_color(migrationmodeler_Color migrationmodeler_color) {
        this.migrationmodeler_color = migrationmodeler_color;
    }

}