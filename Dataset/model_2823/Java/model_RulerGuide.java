





import java.util.List;
import java.util.ArrayList;

public class model_RulerGuide  {

    private int position;





    private model_ScreenRuler model_screenruler;


    public model_RulerGuide(
        int position    ) {
        this.position = position;
    }


    public int getPosition() {
        return position;
    }

    public void setPosition(int position) {
        this.position = position;
    }

    public model_ScreenRuler getModel_screenruler() {
        return model_screenruler;
    }

    public void setModel_screenruler(model_ScreenRuler model_screenruler) {
        this.model_screenruler = model_screenruler;
    }

}