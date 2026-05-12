





import java.util.List;
import java.util.ArrayList;

public class build_properties_Split extends IFunction {

    private String style;
    private String pattern;
    private int limit;



    public build_properties_Split(
        String style,        String pattern,        int limit    ) {
        super(
        );
        this.style = style;
        this.pattern = pattern;
        this.limit = limit;
    }


    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getPattern() {
        return pattern;
    }

    public void setPattern(String pattern) {
        this.pattern = pattern;
    }
    public int getLimit() {
        return limit;
    }

    public void setLimit(int limit) {
        this.limit = limit;
    }


}