





import java.util.List;
import java.util.ArrayList;

public class statemachines_Transition extends NamedElement {

    private String kind;



    public statemachines_Transition(
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