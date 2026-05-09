





import java.util.List;
import java.util.ArrayList;

public class reviews_LineLocation extends Location {

    private int rangeMin;
    private int rangeMax;



    public reviews_LineLocation(
        int rangeMin,        int rangeMax    ) {
        super(
        );
        this.rangeMin = rangeMin;
        this.rangeMax = rangeMax;
    }


    public int getRangemin() {
        return rangeMin;
    }

    public void setRangemin(int rangeMin) {
        this.rangeMin = rangeMin;
    }
    public int getRangemax() {
        return rangeMax;
    }

    public void setRangemax(int rangeMax) {
        this.rangeMax = rangeMax;
    }


}