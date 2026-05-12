





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_FormatTstamp  {

    private String property;
    private String pattern;
    private String locale;
    private String offset;
    private String unit;



    public MavenMaven_FormatTstamp(
        String property,        String pattern,        String locale,        String offset,        String unit    ) {
        this.property = property;
        this.pattern = pattern;
        this.locale = locale;
        this.offset = offset;
        this.unit = unit;
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
    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }


}