





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_FormatTstamp  {

    private String pattern;
    private String property;
    private String unit;
    private String offset;
    private String locale;





    private MavenMaven_Tstamp mavenmaven_tstamp;


    public MavenMaven_FormatTstamp(
        String pattern,        String property,        String unit,        String offset,        String locale    ) {
        this.pattern = pattern;
        this.property = property;
        this.unit = unit;
        this.offset = offset;
        this.locale = locale;
    }


    public String getPattern() {
        return pattern;
    }

    public void setPattern(String pattern) {
        this.pattern = pattern;
    }
    public String getProperty() {
        return property;
    }

    public void setProperty(String property) {
        this.property = property;
    }
    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }
    public String getOffset() {
        return offset;
    }

    public void setOffset(String offset) {
        this.offset = offset;
    }
    public String getLocale() {
        return locale;
    }

    public void setLocale(String locale) {
        this.locale = locale;
    }

    public MavenMaven_Tstamp getMavenmaven_tstamp() {
        return mavenmaven_tstamp;
    }

    public void setMavenmaven_tstamp(MavenMaven_Tstamp mavenmaven_tstamp) {
        this.mavenmaven_tstamp = mavenmaven_tstamp;
    }

}