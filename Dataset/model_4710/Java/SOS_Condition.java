





import java.util.List;
import java.util.ArrayList;

public class SOS_Condition  {






    private SOS_PremisseList sos_premisselist;




    private SOS_Conclusion sos_conclusion;


    public SOS_Condition(
    ) {
    }



    public SOS_PremisseList getSos_premisselist() {
        return sos_premisselist;
    }

    public void setSos_premisselist(SOS_PremisseList sos_premisselist) {
        this.sos_premisselist = sos_premisselist;
    }
    public SOS_Conclusion getSos_conclusion() {
        return sos_conclusion;
    }

    public void setSos_conclusion(SOS_Conclusion sos_conclusion) {
        this.sos_conclusion = sos_conclusion;
    }

}