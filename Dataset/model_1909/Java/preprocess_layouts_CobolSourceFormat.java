





import java.util.List;
import java.util.ArrayList;

public class preprocess_layouts_CobolSourceFormat  {

    private boolean commentEntryMultiLine;
    private String pattern;
    private String regex;
    private String type;



    public preprocess_layouts_CobolSourceFormat(
        boolean commentEntryMultiLine,        String pattern,        String regex,        String type    ) {
        this.commentEntryMultiLine = commentEntryMultiLine;
        this.pattern = pattern;
        this.regex = regex;
        this.type = type;
    }


    public boolean getCommententrymultiline() {
        return commentEntryMultiLine;
    }

    public void setCommententrymultiline(boolean commentEntryMultiLine) {
        this.commentEntryMultiLine = commentEntryMultiLine;
    }
    public String getPattern() {
        return pattern;
    }

    public void setPattern(String pattern) {
        this.pattern = pattern;
    }
    public String getRegex() {
        return regex;
    }

    public void setRegex(String regex) {
        this.regex = regex;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}