





import java.util.List;
import java.util.ArrayList;

public class YasperEPNML114_TransitionType  {

    private String text;





    private YasperEPNML114_Transition yasperepnml114_transition;




    private YasperEPNML114_Page yasperepnml114_page;


    public YasperEPNML114_TransitionType(
        String text    ) {
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public YasperEPNML114_Transition getYasperepnml114_transition() {
        return yasperepnml114_transition;
    }

    public void setYasperepnml114_transition(YasperEPNML114_Transition yasperepnml114_transition) {
        this.yasperepnml114_transition = yasperepnml114_transition;
    }
    public YasperEPNML114_Page getYasperepnml114_page() {
        return yasperepnml114_page;
    }

    public void setYasperepnml114_page(YasperEPNML114_Page yasperepnml114_page) {
        this.yasperepnml114_page = yasperepnml114_page;
    }

}