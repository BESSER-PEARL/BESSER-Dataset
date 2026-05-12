





import java.util.List;
import java.util.ArrayList;

public class sql_common_Comment extends Separator {

    private String value;



    public sql_common_Comment(
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