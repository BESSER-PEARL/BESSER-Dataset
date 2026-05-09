





import java.util.List;
import java.util.ArrayList;

public class oclstates_SimpleState extends State {

    private int value;



    public oclstates_SimpleState(
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