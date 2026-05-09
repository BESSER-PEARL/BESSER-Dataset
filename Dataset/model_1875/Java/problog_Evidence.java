





import java.util.List;
import java.util.ArrayList;

public class problog_Evidence extends ProbLogStatement {

    private String value;



    public problog_Evidence(
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