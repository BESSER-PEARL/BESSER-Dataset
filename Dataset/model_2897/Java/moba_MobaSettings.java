





import java.util.List;
import java.util.ArrayList;

public class moba_MobaSettings extends MobaApplicationFeature {

    private boolean active;
    private String name;





    private moba_MobaSettings moba_mobasettings;


    public moba_MobaSettings(
        boolean active,        String name    ) {
        super(
        );
        this.active = active;
        this.name = name;
    }


    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public moba_MobaSettings getMoba_mobasettings() {
        return moba_mobasettings;
    }

    public void setMoba_mobasettings(moba_MobaSettings moba_mobasettings) {
        this.moba_mobasettings = moba_mobasettings;
    }

}