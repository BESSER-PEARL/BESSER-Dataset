





import java.util.List;
import java.util.ArrayList;

public class entityDsl_Spinner extends WinFormControlType {

    private int minimumValue;
    private int maximumValue;
    private int defaultValue;



    public entityDsl_Spinner(
        int minimumValue,        int maximumValue,        int defaultValue    ) {
        super(
        );
        this.minimumValue = minimumValue;
        this.maximumValue = maximumValue;
        this.defaultValue = defaultValue;
    }


    public int getMinimumvalue() {
        return minimumValue;
    }

    public void setMinimumvalue(int minimumValue) {
        this.minimumValue = minimumValue;
    }
    public int getMaximumvalue() {
        return maximumValue;
    }

    public void setMaximumvalue(int maximumValue) {
        this.maximumValue = maximumValue;
    }
    public int getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(int defaultValue) {
        this.defaultValue = defaultValue;
    }


}