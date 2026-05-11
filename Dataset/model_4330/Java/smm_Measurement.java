





import java.util.List;
import java.util.ArrayList;

public class smm_Measurement extends SmmElement {

    private String breakValue;
    private String error;



    public smm_Measurement(
        String breakValue,        String error    ) {
        super(
        );
        this.breakValue = breakValue;
        this.error = error;
    }


    public String getBreakvalue() {
        return breakValue;
    }

    public void setBreakvalue(String breakValue) {
        this.breakValue = breakValue;
    }
    public String getError() {
        return error;
    }

    public void setError(String error) {
        this.error = error;
    }


}