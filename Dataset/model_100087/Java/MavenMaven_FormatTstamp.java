





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_FormatTstamp  {

    private String locale;
    private String offset;
    private String pattern;
    private String unit;
    private String property;



    public MavenMaven_FormatTstamp(
        String locale,        String offset,        String pattern,        String unit,        String property    ) {
        this.locale = locale;
        this.offset = offset;
        this.pattern = pattern;
        this.unit = unit;
        this.property = property;
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
    public String getProperty() {
        return property;
    }

    public void setProperty(String property) {
        this.property = property;
    }


}