





import java.util.List;
import java.util.ArrayList;

public class swt_IntervalSelector extends IntervalControl {

    private int increment;
    private int pageIncrement;
    private String orientationStyle;



    public swt_IntervalSelector(
        int increment,        int pageIncrement,        String orientationStyle    ) {
        super(
        );
        this.increment = increment;
        this.pageIncrement = pageIncrement;
        this.orientationStyle = orientationStyle;
    }


    public int getIncrement() {
        return increment;
    }

    public void setIncrement(int increment) {
        this.increment = increment;
    }
    public int getPageincrement() {
        return pageIncrement;
    }

    public void setPageincrement(int pageIncrement) {
        this.pageIncrement = pageIncrement;
    }
    public String getOrientationstyle() {
        return orientationStyle;
    }

    public void setOrientationstyle(String orientationStyle) {
        this.orientationStyle = orientationStyle;
    }


}