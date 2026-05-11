





import java.util.List;
import java.util.ArrayList;

public class AbstractEquation  {






    private SOS_adtmm_CondEquation sos_adtmm_condequation;




    private SOS_AlgebraicCondition sos_algebraiccondition;


    public AbstractEquation(
    ) {
    }



    public SOS_adtmm_CondEquation getSos_adtmm_condequation() {
        return sos_adtmm_condequation;
    }

    public void setSos_adtmm_condequation(SOS_adtmm_CondEquation sos_adtmm_condequation) {
        this.sos_adtmm_condequation = sos_adtmm_condequation;
    }
    public SOS_AlgebraicCondition getSos_algebraiccondition() {
        return sos_algebraiccondition;
    }

    public void setSos_algebraiccondition(SOS_AlgebraicCondition sos_algebraiccondition) {
        this.sos_algebraiccondition = sos_algebraiccondition;
    }

}