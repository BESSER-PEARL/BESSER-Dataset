





import java.util.List;
import java.util.ArrayList;

public class prolog_Comment extends Clause {

    private String value;



    public prolog_Comment(
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