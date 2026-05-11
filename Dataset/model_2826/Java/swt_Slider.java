





import java.util.List;
import java.util.ArrayList;

public class swt_Slider extends IntervalSelector {

    private int thumb;



    public swt_Slider(
        int thumb    ) {
        super(
        );
        this.thumb = thumb;
    }


    public int getThumb() {
        return thumb;
    }

    public void setThumb(int thumb) {
        this.thumb = thumb;
    }


}