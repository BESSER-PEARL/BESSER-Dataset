





import java.util.List;
import java.util.ArrayList;

public class build_command_StringAdvice extends IAdvise {

    private String value;



    public build_command_StringAdvice(
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