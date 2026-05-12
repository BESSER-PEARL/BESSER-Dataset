





import java.util.List;
import java.util.ArrayList;

public class Ant_FormatTstamp  {

    private String locale;
    private String property;
    private String pattern;
    private String unit;
    private String offset;



    public Ant_FormatTstamp(
        String locale,        String property,        String pattern,        String unit,        String offset    ) {
        this.locale = locale;
        this.property = property;
        this.pattern = pattern;
        this.unit = unit;
        this.offset = offset;
    }


    public String getLocale() {
        return locale;
    }

    public void setLocale(String locale) {
        this.locale = locale;
    }
    public String getProperty() {
        return property;
    }

    public void setProperty(String property) {
        this.property = property;
    }
    public String getPattern() {
        return pattern;
    }

    public void setPattern(String pattern) {
        this.pattern = pattern;
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


}