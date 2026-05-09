





import java.util.List;
import java.util.ArrayList;

public class shr5_FokusBinding  {

    private boolean active;





    private shr5_BaseMagischePersona shr5_basemagischepersona;




    private shr5_Fokus shr5_fokus;


    public shr5_FokusBinding(
        boolean active    ) {
        this.active = active;
    }


    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }

    public shr5_BaseMagischePersona getShr5_basemagischepersona() {
        return shr5_basemagischepersona;
    }

    public void setShr5_basemagischepersona(shr5_BaseMagischePersona shr5_basemagischepersona) {
        this.shr5_basemagischepersona = shr5_basemagischepersona;
    }
    public shr5_Fokus getShr5_fokus() {
        return shr5_fokus;
    }

    public void setShr5_fokus(shr5_Fokus shr5_fokus) {
        this.shr5_fokus = shr5_fokus;
    }

}