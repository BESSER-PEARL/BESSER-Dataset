





import java.util.List;
import java.util.ArrayList;

public class prolog_AtomicQuotedString extends Term {

    private String value;



    public prolog_AtomicQuotedString(
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