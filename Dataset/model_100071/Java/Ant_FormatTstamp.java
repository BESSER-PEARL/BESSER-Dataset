





import java.util.List;
import java.util.ArrayList;

public class Ant_FormatTstamp  {

    private String pattern;
    private String property;
    private String unit;
    private String locale;
    private String offset;





    private Ant_Tstamp ant_tstamp;


    public Ant_FormatTstamp(
        String pattern,        String property,        String unit,        String locale,        String offset    ) {
        this.pattern = pattern;
        this.property = property;
        this.unit = unit;
        this.locale = locale;
        this.offset = offset;
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
    public String getLocale() {
        return locale;
    }

    public void setLocale(String locale) {
        this.locale = locale;
    }
    public String getOffset() {
        return offset;
    }

    public void setOffset(String offset) {
        this.offset = offset;
    }

    public Ant_Tstamp getAnt_tstamp() {
        return ant_tstamp;
    }

    public void setAnt_tstamp(Ant_Tstamp ant_tstamp) {
        this.ant_tstamp = ant_tstamp;
    }

}