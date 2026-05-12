





import java.util.List;
import java.util.ArrayList;

public class AsmL_MapTerm extends Term {

    private String separator;



    public AsmL_MapTerm(
        String separator    ) {
        super(
        );
        this.separator = separator;
    }


    public String getSeparator() {
        return separator;
    }

    public void setSeparator(String separator) {
        this.separator = separator;
    }


}