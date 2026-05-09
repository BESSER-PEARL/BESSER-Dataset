





import java.util.List;
import java.util.ArrayList;

public class capellacommon_ChangeEvent extends StateEvent {

    private String kind;



    public capellacommon_ChangeEvent(
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