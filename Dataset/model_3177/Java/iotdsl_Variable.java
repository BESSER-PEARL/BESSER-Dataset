





import java.util.List;
import java.util.ArrayList;

public class iotdsl_Variable extends Action {

    private String name;



    public iotdsl_Variable(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}