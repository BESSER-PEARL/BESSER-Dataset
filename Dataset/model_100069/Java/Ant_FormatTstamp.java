





import java.util.List;
import java.util.ArrayList;

public class Ant_FormatTstamp  {

    private String locale;
    private String pattern;
    private String offset;
    private String property;
    private String unit;



    public Ant_FormatTstamp(
        String locale,        String pattern,        String offset,        String property,        String unit    ) {
        this.locale = locale;
        this.pattern = pattern;
        this.offset = offset;
        this.property = property;
        this.unit = unit;
    }


    public String getLocale() {
        return locale;
    }

    public void setLocale(String locale) {
        this.locale = locale;
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


}