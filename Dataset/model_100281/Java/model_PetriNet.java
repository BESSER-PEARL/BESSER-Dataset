





import java.util.List;
import java.util.ArrayList;

public class model_PetriNet extends HasLabel, HasToolInfo, HasName, HasId {

    private String kind;
    private String timeType;



    public model_PetriNet(
        String kind,        String timeType    ) {
        super(
        );
        this.kind = kind;
        this.timeType = timeType;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getTimetype() {
        return timeType;
    }

    public void setTimetype(String timeType) {
        this.timeType = timeType;
    }


}