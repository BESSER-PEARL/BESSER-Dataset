





import java.util.List;
import java.util.ArrayList;

public class prolog_CompoundTerm extends Clause, Term {

    private String value;



    public prolog_CompoundTerm(
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