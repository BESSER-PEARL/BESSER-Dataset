





import java.util.List;
import java.util.ArrayList;

public class FSmachine_TimeConnection extends AbstractConection {

    private String when;



    public FSmachine_TimeConnection(
        String when    ) {
        super(
        );
        this.when = when;
    }


    public String getWhen() {
        return when;
    }

    public void setWhen(String when) {
        this.when = when;
    }


}