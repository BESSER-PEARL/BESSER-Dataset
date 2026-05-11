





import java.util.List;
import java.util.ArrayList;

public class vcml_DateType extends CharacteristicType {

    private boolean intervalValuesAllowed;



    public vcml_DateType(
        boolean intervalValuesAllowed    ) {
        super(
        );
        this.intervalValuesAllowed = intervalValuesAllowed;
    }


    public boolean getIntervalvaluesallowed() {
        return intervalValuesAllowed;
    }

    public void setIntervalvaluesallowed(boolean intervalValuesAllowed) {
        this.intervalValuesAllowed = intervalValuesAllowed;
    }


}