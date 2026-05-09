





import java.util.List;
import java.util.ArrayList;

public class ccsl_filters_RegexMatch extends AtomicFilter {

    private String regex;



    public ccsl_filters_RegexMatch(
        String regex    ) {
        super(
        );
        this.regex = regex;
    }


    public String getRegex() {
        return regex;
    }

    public void setRegex(String regex) {
        this.regex = regex;
    }


}