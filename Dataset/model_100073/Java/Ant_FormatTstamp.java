





import java.util.List;
import java.util.ArrayList;

public class Ant_FormatTstamp  {

    private String unit;
    private String pattern;
    private String offset;
    private String locale;
    private String property;



    public Ant_FormatTstamp(
        String unit,        String pattern,        String offset,        String locale,        String property    ) {
        this.unit = unit;
        this.pattern = pattern;
        this.offset = offset;
        this.locale = locale;
        this.property = property;
    }


    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }
    public String getPattern() {
        return pattern;
    }

    public void setPattern(String pattern) {
        this.pattern = pattern;
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
    public String getProperty() {
        return property;
    }

    public void setProperty(String property) {
        this.property = property;
    }


}