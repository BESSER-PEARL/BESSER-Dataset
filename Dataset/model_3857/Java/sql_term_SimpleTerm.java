





import java.util.List;
import java.util.ArrayList;

public class sql_term_SimpleTerm extends Term {

    private String value;



    public sql_term_SimpleTerm(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}