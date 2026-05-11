





import java.util.List;
import java.util.ArrayList;

public class smm_Measurement extends SmmElement {

    private String error;
    private String breakValue;



    public smm_Measurement(
        String error,        String breakValue    ) {
        super(
        );
        this.error = error;
        this.breakValue = breakValue;
    }


    public String getError() {
        return error;
    }

    public void setError(String error) {
        this.error = error;
    }
    public String getBreakvalue() {
        return breakValue;
    }

    public void setBreakvalue(String breakValue) {
        this.breakValue = breakValue;
    }


}