





import java.util.List;
import java.util.ArrayList;

public class eel_Integral extends MeasurementUncertaintyInformation {

    private String function;





    private eel_Interval eel_interval;


    public eel_Integral(
        String function    ) {
        super(
        );
        this.function = function;
    }


    public String getFunction() {
        return function;
    }

    public void setFunction(String function) {
        this.function = function;
    }

    public eel_Interval getEel_interval() {
        return eel_interval;
    }

    public void setEel_interval(eel_Interval eel_interval) {
        this.eel_interval = eel_interval;
    }

}