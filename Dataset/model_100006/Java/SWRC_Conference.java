





import java.util.List;
import java.util.ArrayList;

public class SWRC_Conference extends Event {

    private String series;



    public SWRC_Conference(
        String series    ) {
        super(
        );
        this.series = series;
    }


    public String getSeries() {
        return series;
    }

    public void setSeries(String series) {
        this.series = series;
    }


}