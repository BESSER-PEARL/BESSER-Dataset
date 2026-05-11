





import java.util.List;
import java.util.ArrayList;

public class events_Multiplicity extends AbstractMultiplicity {

    private int value;



    public events_Multiplicity(
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