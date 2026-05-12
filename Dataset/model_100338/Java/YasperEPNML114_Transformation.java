





import java.util.List;
import java.util.ArrayList;

public class YasperEPNML114_Transformation  {

    private String text;





    private YasperEPNML114_AnnotationGraphics yasperepnml114_annotationgraphics;




    private YasperEPNML114_Transition yasperepnml114_transition;


    public YasperEPNML114_Transformation(
        String text    ) {
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public YasperEPNML114_AnnotationGraphics getYasperepnml114_annotationgraphics() {
        return yasperepnml114_annotationgraphics;
    }

    public void setYasperepnml114_annotationgraphics(YasperEPNML114_AnnotationGraphics yasperepnml114_annotationgraphics) {
        this.yasperepnml114_annotationgraphics = yasperepnml114_annotationgraphics;
    }
    public YasperEPNML114_Transition getYasperepnml114_transition() {
        return yasperepnml114_transition;
    }

    public void setYasperepnml114_transition(YasperEPNML114_Transition yasperepnml114_transition) {
        this.yasperepnml114_transition = yasperepnml114_transition;
    }

}