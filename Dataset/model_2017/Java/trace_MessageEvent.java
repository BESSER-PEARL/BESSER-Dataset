





import java.util.List;
import java.util.ArrayList;

public class trace_MessageEvent extends Event {

    private String kind;



    public trace_MessageEvent(
        String kind    ) {
        super(
        );
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }


}