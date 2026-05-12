





import java.util.List;
import java.util.ArrayList;

public class Ant_FormatTstamp  {

    private String property;
    private String offset;
    private String unit;
    private String pattern;
    private String locale;



    public Ant_FormatTstamp(
        String property,        String offset,        String unit,        String pattern,        String locale    ) {
        this.property = property;
        this.offset = offset;
        this.unit = unit;
        this.pattern = pattern;
        this.locale = locale;
    }


    public String getProperty() {
        return property;
    }

    public void setProperty(String property) {
        this.property = property;
    }
    public String getOffset() {
        return offset;
    }

    public void setOffset(String offset) {
        this.offset = offset;
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
    public String getLocale() {
        return locale;
    }

    public void setLocale(String locale) {
        this.locale = locale;
    }


}