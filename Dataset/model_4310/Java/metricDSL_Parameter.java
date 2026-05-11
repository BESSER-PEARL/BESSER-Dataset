





import java.util.List;
import java.util.ArrayList;

public class metricDSL_Parameter extends Number {

    private float defaultValue;
    private String shortname;
    private String description;



    public metricDSL_Parameter(
        float defaultValue,        String shortname,        String description    ) {
        super(
        );
        this.defaultValue = defaultValue;
        this.shortname = shortname;
        this.description = description;
    }


    public float getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(float defaultValue) {
        this.defaultValue = defaultValue;
    }
    public String getShortname() {
        return shortname;
    }

    public void setShortname(String shortname) {
        this.shortname = shortname;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}