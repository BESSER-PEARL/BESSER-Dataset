





import java.util.List;
import java.util.ArrayList;

public class migrationmodeler_Ellipse extends NodeStyle {

    private String verticalDiameter;
    private String horizontalDiameter;





    private migrationmodeler_Color migrationmodeler_color;


    public migrationmodeler_Ellipse(
        String verticalDiameter,        String horizontalDiameter    ) {
        super(
        );
        this.verticalDiameter = verticalDiameter;
        this.horizontalDiameter = horizontalDiameter;
    }


    public String getVerticaldiameter() {
        return verticalDiameter;
    }

    public void setVerticaldiameter(String verticalDiameter) {
        this.verticalDiameter = verticalDiameter;
    }
    public String getHorizontaldiameter() {
        return horizontalDiameter;
    }

    public void setHorizontaldiameter(String horizontalDiameter) {
        this.horizontalDiameter = horizontalDiameter;
    }

    public migrationmodeler_Color getMigrationmodeler_color() {
        return migrationmodeler_color;
    }

    public void setMigrationmodeler_color(migrationmodeler_Color migrationmodeler_color) {
        this.migrationmodeler_color = migrationmodeler_color;
    }

}