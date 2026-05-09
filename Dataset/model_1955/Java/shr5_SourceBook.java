





import java.util.List;
import java.util.ArrayList;

public class shr5_SourceBook extends Beschreibbar, Identifiable {

    private String endShrTime;
    private String startShrTime;
    private String code;



    public shr5_SourceBook(
        String endShrTime,        String startShrTime,        String code    ) {
        super(
        );
        this.endShrTime = endShrTime;
        this.startShrTime = startShrTime;
        this.code = code;
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
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }


}