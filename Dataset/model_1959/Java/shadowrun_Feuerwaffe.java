





import java.util.List;
import java.util.ArrayList;

public class shadowrun_Feuerwaffe extends AbstaktFernKampfwaffe {

    private String modie;
    private int kapazitaet;
    private String munitionstyp;





    private shadowrun_MunitionsBehealter shadowrun_munitionsbehealter;


    public shadowrun_Feuerwaffe(
        String modie,        int kapazitaet,        String munitionstyp    ) {
        super(
        );
        this.modie = modie;
        this.kapazitaet = kapazitaet;
        this.munitionstyp = munitionstyp;
    }


    public String getModie() {
        return modie;
    }

    public void setModie(String modie) {
        this.modie = modie;
    }
    public int getKapazitaet() {
        return kapazitaet;
    }

    public void setKapazitaet(int kapazitaet) {
        this.kapazitaet = kapazitaet;
    }
    public String getMunitionstyp() {
        return munitionstyp;
    }

    public void setMunitionstyp(String munitionstyp) {
        this.munitionstyp = munitionstyp;
    }

    public shadowrun_MunitionsBehealter getShadowrun_munitionsbehealter() {
        return shadowrun_munitionsbehealter;
    }

    public void setShadowrun_munitionsbehealter(shadowrun_MunitionsBehealter shadowrun_munitionsbehealter) {
        this.shadowrun_munitionsbehealter = shadowrun_munitionsbehealter;
    }

}