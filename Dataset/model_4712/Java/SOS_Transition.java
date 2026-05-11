





import java.util.List;
import java.util.ArrayList;

public class SOS_Transition extends Condition {






    private SOS_Conclusion sos_conclusion;


    public SOS_Transition(
    ) {
        super(
        );
    }



    public SOS_Conclusion getSos_conclusion() {
        return sos_conclusion;
    }

    public void setSos_conclusion(SOS_Conclusion sos_conclusion) {
        this.sos_conclusion = sos_conclusion;
    }

}