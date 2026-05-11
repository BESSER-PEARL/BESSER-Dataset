





import java.util.List;
import java.util.ArrayList;

public class SPL_Place extends Expression {






    private SPL_PushStat spl_pushstat;




    private SPL_SetStat spl_setstat;


    public SPL_Place(
    ) {
        super(
        );
    }



    public SPL_PushStat getSpl_pushstat() {
        return spl_pushstat;
    }

    public void setSpl_pushstat(SPL_PushStat spl_pushstat) {
        this.spl_pushstat = spl_pushstat;
    }
    public SPL_SetStat getSpl_setstat() {
        return spl_setstat;
    }

    public void setSpl_setstat(SPL_SetStat spl_setstat) {
        this.spl_setstat = spl_setstat;
    }

}