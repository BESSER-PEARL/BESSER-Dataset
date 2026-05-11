





import java.util.List;
import java.util.ArrayList;

public class Concept_Signal extends Thing {

    private String Signal_actualState;



    public Concept_Signal(
        String Signal_actualState    ) {
        super(
        );
        this.Signal_actualState = Signal_actualState;
    }


    public String getSignal_actualstate() {
        return Signal_actualState;
    }

    public void setSignal_actualstate(String Signal_actualState) {
        this.Signal_actualState = Signal_actualState;
    }


}