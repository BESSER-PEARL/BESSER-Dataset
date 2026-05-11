





import java.util.List;
import java.util.ArrayList;

public class migrationmodeler_Color  {

    private int blue;
    private int green;
    private int red;





    private migrationmodeler_EdgeStyle migrationmodeler_edgestyle;


    public migrationmodeler_Color(
        int blue,        int green,        int red    ) {
        this.blue = blue;
        this.green = green;
        this.red = red;
    }


    public int getBlue() {
        return blue;
    }

    public void setBlue(int blue) {
        this.blue = blue;
    }
    public int getGreen() {
        return green;
    }

    public void setGreen(int green) {
        this.green = green;
    }
    public int getRed() {
        return red;
    }

    public void setRed(int red) {
        this.red = red;
    }

    public migrationmodeler_EdgeStyle getMigrationmodeler_edgestyle() {
        return migrationmodeler_edgestyle;
    }

    public void setMigrationmodeler_edgestyle(migrationmodeler_EdgeStyle migrationmodeler_edgestyle) {
        this.migrationmodeler_edgestyle = migrationmodeler_edgestyle;
    }

}