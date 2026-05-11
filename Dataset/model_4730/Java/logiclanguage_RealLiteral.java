





import java.util.List;
import java.util.ArrayList;

public class logiclanguage_RealLiteral extends AtomicTerm {

    private String value;



    public logiclanguage_RealLiteral(
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