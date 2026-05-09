





import java.util.List;
import java.util.ArrayList;

public class shadowrun_AbstractMagischePaersona extends AbstaktPersona, BaseMagischePersona {

    private int magieBase;



    public shadowrun_AbstractMagischePaersona(
        int magieBase    ) {
        super(
        );
        this.magieBase = magieBase;
    }


    public int getMagiebase() {
        return magieBase;
    }

    public void setMagiebase(int magieBase) {
        this.magieBase = magieBase;
    }


}