





import java.util.List;
import java.util.ArrayList;

public class swt_ProgressBar extends IntervalControl {

    private String state;



    public swt_ProgressBar(
        String state    ) {
        super(
        );
        this.state = state;
    }


    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }


}