





import java.util.List;
import java.util.ArrayList;

public class shadowrun_SourceBook extends Beschreibbar {

    private String endShrTime;
    private String startShrTime;



    public shadowrun_SourceBook(
        String endShrTime,        String startShrTime    ) {
        super(
        );
        this.endShrTime = endShrTime;
        this.startShrTime = startShrTime;
    }


    public String getEndshrtime() {
        return endShrTime;
    }

    public void setEndshrtime(String endShrTime) {
        this.endShrTime = endShrTime;
    }
    public String getStartshrtime() {
        return startShrTime;
    }

    public void setStartshrtime(String startShrTime) {
        this.startShrTime = startShrTime;
    }


}