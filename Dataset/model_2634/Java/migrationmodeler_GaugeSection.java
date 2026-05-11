





import java.util.List;
import java.util.ArrayList;

public class migrationmodeler_GaugeSection  {

    private String label;
    private String min;
    private String value;
    private String max;





    private migrationmodeler_GaugeCompositeStyle migrationmodeler_gaugecompositestyle;




    private migrationmodeler_Color migrationmodeler_color;




    private migrationmodeler_Color migrationmodeler_color;


    public migrationmodeler_GaugeSection(
        String label,        String min,        String value,        String max    ) {
        this.label = label;
        this.min = min;
        this.value = value;
        this.max = max;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getMin() {
        return min;
    }

    public void setMin(String min) {
        this.min = min;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getMax() {
        return max;
    }

    public void setMax(String max) {
        this.max = max;
    }

    public migrationmodeler_GaugeCompositeStyle getMigrationmodeler_gaugecompositestyle() {
        return migrationmodeler_gaugecompositestyle;
    }

    public void setMigrationmodeler_gaugecompositestyle(migrationmodeler_GaugeCompositeStyle migrationmodeler_gaugecompositestyle) {
        this.migrationmodeler_gaugecompositestyle = migrationmodeler_gaugecompositestyle;
    }
    public migrationmodeler_Color getMigrationmodeler_color() {
        return migrationmodeler_color;
    }

    public void setMigrationmodeler_color(migrationmodeler_Color migrationmodeler_color) {
        this.migrationmodeler_color = migrationmodeler_color;
    }
    public migrationmodeler_Color getMigrationmodeler_color() {
        return migrationmodeler_color;
    }

    public void setMigrationmodeler_color(migrationmodeler_Color migrationmodeler_color) {
        this.migrationmodeler_color = migrationmodeler_color;
    }

}