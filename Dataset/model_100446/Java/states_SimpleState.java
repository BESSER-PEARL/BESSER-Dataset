





import java.util.List;
import java.util.ArrayList;

public class states_SimpleState extends State {

    private int value;



    public states_SimpleState(
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