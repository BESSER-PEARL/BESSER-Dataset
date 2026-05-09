





import java.util.List;
import java.util.ArrayList;

public class reviews_LineLocation extends Location {

    private int rangeMax;
    private int rangeMin;



    public reviews_LineLocation(
        int rangeMax,        int rangeMin    ) {
        super(
        );
        this.rangeMax = rangeMax;
        this.rangeMin = rangeMin;
    }


    public int getRangemax() {
        return rangeMax;
    }

    public void setRangemax(int rangeMax) {
        this.rangeMax = rangeMax;
    }
    public int getRangemin() {
        return rangeMin;
    }

    public void setRangemin(int rangeMin) {
        this.rangeMin = rangeMin;
    }


}