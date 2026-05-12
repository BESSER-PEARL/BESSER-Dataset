





import java.util.List;
import java.util.ArrayList;

public class build_properties_Match  {

    private String replacement;
    private String pattern;
    private boolean quotePattern;



    public build_properties_Match(
        String replacement,        String pattern,        boolean quotePattern    ) {
        this.replacement = replacement;
        this.pattern = pattern;
        this.quotePattern = quotePattern;
    }


    public String getReplacement() {
        return replacement;
    }

    public void setReplacement(String replacement) {
        this.replacement = replacement;
    }
    public String getPattern() {
        return pattern;
    }

    public void setPattern(String pattern) {
        this.pattern = pattern;
    }
    public boolean getQuotepattern() {
        return quotePattern;
    }

    public void setQuotepattern(boolean quotePattern) {
        this.quotePattern = quotePattern;
    }


}