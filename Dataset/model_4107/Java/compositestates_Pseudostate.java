





import java.util.List;
import java.util.ArrayList;

public class compositestates_Pseudostate extends AbstractState {

    private String kind;



    public compositestates_Pseudostate(
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