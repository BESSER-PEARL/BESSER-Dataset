





import java.util.List;
import java.util.ArrayList;

public class r1_Interval extends Expression {

    private String highClosed;
    private String lowClosed;



    public r1_Interval(
        String highClosed,        String lowClosed    ) {
        super(
        );
        this.highClosed = highClosed;
        this.lowClosed = lowClosed;
    }


    public String getHighclosed() {
        return highClosed;
    }

    public void setHighclosed(String highClosed) {
        this.highClosed = highClosed;
    }
    public String getLowclosed() {
        return lowClosed;
    }

    public void setLowclosed(String lowClosed) {
        this.lowClosed = lowClosed;
    }


}