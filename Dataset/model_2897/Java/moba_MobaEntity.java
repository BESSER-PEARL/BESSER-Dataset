





import java.util.List;
import java.util.ArrayList;

public class moba_MobaEntity extends MobaData {

    private String name;





    private moba_MobaEntity moba_mobaentity;




    private moba_MobaCache moba_mobacache;




    private moba_MobaSettingsEntityReference moba_mobasettingsentityreference;


    public moba_MobaEntity(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public moba_MobaEntity getMoba_mobaentity() {
        return moba_mobaentity;
    }

    public void setMoba_mobaentity(moba_MobaEntity moba_mobaentity) {
        this.moba_mobaentity = moba_mobaentity;
    }
    public moba_MobaCache getMoba_mobacache() {
        return moba_mobacache;
    }

    public void setMoba_mobacache(moba_MobaCache moba_mobacache) {
        this.moba_mobacache = moba_mobacache;
    }
    public moba_MobaSettingsEntityReference getMoba_mobasettingsentityreference() {
        return moba_mobasettingsentityreference;
    }

    public void setMoba_mobasettingsentityreference(moba_MobaSettingsEntityReference moba_mobasettingsentityreference) {
        this.moba_mobasettingsentityreference = moba_mobasettingsentityreference;
    }

}