





import java.util.List;
import java.util.ArrayList;

public class shadowrun_AbstractMagier extends BaseMagischePersona {

    private int MagiePool;
    private int Astralpool;
    private int InitationsGrad;



    public shadowrun_AbstractMagier(
        int MagiePool,        int Astralpool,        int InitationsGrad    ) {
        super(
        );
        this.MagiePool = MagiePool;
        this.Astralpool = Astralpool;
        this.InitationsGrad = InitationsGrad;
    }


    public int getMagiepool() {
        return MagiePool;
    }

    public void setMagiepool(int MagiePool) {
        this.MagiePool = MagiePool;
    }
    public int getAstralpool() {
        return Astralpool;
    }

    public void setAstralpool(int Astralpool) {
        this.Astralpool = Astralpool;
    }
    public int getInitationsgrad() {
        return InitationsGrad;
    }

    public void setInitationsgrad(int InitationsGrad) {
        this.InitationsGrad = InitationsGrad;
    }


}