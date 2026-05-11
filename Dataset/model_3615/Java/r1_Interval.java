





import java.util.List;
import java.util.ArrayList;

public class r1_Interval extends Expression {

    private String lowClosed;
    private String highClosed;



    public r1_Interval(
        String lowClosed,        String highClosed    ) {
        super(
        );
        this.lowClosed = lowClosed;
        this.highClosed = highClosed;
    }


    public String getLowclosed() {
        return lowClosed;
    }

    public void setLowclosed(String lowClosed) {
        this.lowClosed = lowClosed;
    }
    public String getHighclosed() {
        return highClosed;
    }

    public void setHighclosed(String highClosed) {
        this.highClosed = highClosed;
    }


}