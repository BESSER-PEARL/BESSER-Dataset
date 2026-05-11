





import java.util.List;
import java.util.ArrayList;

public class esm_IEsmState  {

    private String kind;





    private esm_IEsmStateModel esm_iesmstatemodel;


    public esm_IEsmState(
        String kind    ) {
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public esm_IEsmStateModel getEsm_iesmstatemodel() {
        return esm_iesmstatemodel;
    }

    public void setEsm_iesmstatemodel(esm_IEsmStateModel esm_iesmstatemodel) {
        this.esm_iesmstatemodel = esm_iesmstatemodel;
    }

}