





import java.util.List;
import java.util.ArrayList;

public class shadowrun_PersonaZauber  {

    private int stufe;





    private shadowrun_Zauber shadowrun_zauber;




    private shadowrun_MagiePersona shadowrun_magiepersona;


    public shadowrun_PersonaZauber(
        int stufe    ) {
        this.stufe = stufe;
    }


    public int getStufe() {
        return stufe;
    }

    public void setStufe(int stufe) {
        this.stufe = stufe;
    }

    public shadowrun_Zauber getShadowrun_zauber() {
        return shadowrun_zauber;
    }

    public void setShadowrun_zauber(shadowrun_Zauber shadowrun_zauber) {
        this.shadowrun_zauber = shadowrun_zauber;
    }
    public shadowrun_MagiePersona getShadowrun_magiepersona() {
        return shadowrun_magiepersona;
    }

    public void setShadowrun_magiepersona(shadowrun_MagiePersona shadowrun_magiepersona) {
        this.shadowrun_magiepersona = shadowrun_magiepersona;
    }

}