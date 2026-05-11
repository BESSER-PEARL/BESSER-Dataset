





import java.util.List;
import java.util.ArrayList;

public class events_AtomicEventPattern extends EventPattern {

    private String type;



    public events_AtomicEventPattern(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}