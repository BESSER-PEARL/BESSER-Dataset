





import java.util.List;
import java.util.ArrayList;

public class tracker_ReplacedTag extends Event {

    private String oldAin;



    public tracker_ReplacedTag(
        String oldAin    ) {
        super(
        );
        this.oldAin = oldAin;
    }


    public String getOldain() {
        return oldAin;
    }

    public void setOldain(String oldAin) {
        this.oldAin = oldAin;
    }


}