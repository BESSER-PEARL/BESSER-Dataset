





import java.util.List;
import java.util.ArrayList;

public class Controleur  {

    private None modeletrain;
    private None vue;





    private Vue vue;


    public Controleur(
        None modeletrain,        None vue    ) {
        this.modeletrain = modeletrain;
        this.vue = vue;
    }


    public None getModeletrain() {
        return modeletrain;
    }

    public void setModeletrain(None modeletrain) {
        this.modeletrain = modeletrain;
    }
    public None getVue() {
        return vue;
    }

    public void setVue(None vue) {
        this.vue = vue;
    }

    public Vue getVue() {
        return vue;
    }

    public void setVue(Vue vue) {
        this.vue = vue;
    }

}