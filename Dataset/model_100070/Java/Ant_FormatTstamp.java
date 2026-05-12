





import java.util.List;
import java.util.ArrayList;

public class Ant_FormatTstamp  {

    private String offset;
    private String locale;
    private String pattern;
    private String property;
    private String unit;



    public Ant_FormatTstamp(
        String offset,        String locale,        String pattern,        String property,        String unit    ) {
        this.offset = offset;
        this.locale = locale;
        this.pattern = pattern;
        this.property = property;
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


}