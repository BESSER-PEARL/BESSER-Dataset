





import java.util.List;
import java.util.ArrayList;

public class scxmlxt_DelayLiteral extends IntLiteral {

    private String timeUnit;



    public scxmlxt_DelayLiteral(
        String timeUnit    ) {
        super(
        );
        this.timeUnit = timeUnit;
    }


    public String getTimeunit() {
        return timeUnit;
    }

    public void setTimeunit(String timeUnit) {
        this.timeUnit = timeUnit;
    }


}