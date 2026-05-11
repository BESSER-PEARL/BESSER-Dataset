





import java.util.List;
import java.util.ArrayList;

public class jcl_parameters_JobClass extends Parameter {

    private int value;



    public jcl_parameters_JobClass(
        int value    ) {
        super(
        );
        this.value = value;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }


}