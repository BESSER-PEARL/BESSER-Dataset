





import java.util.List;
import java.util.ArrayList;

public class cjsidl_guardParam  {

    private String guardConst;





    private cjsidl_popTransition cjsidl_poptransition;




    private cjsidl_transParam cjsidl_transparam;


    public cjsidl_guardParam(
        String guardConst    ) {
        this.guardConst = guardConst;
    }


    public String getGuardconst() {
        return guardConst;
    }

    public void setGuardconst(String guardConst) {
        this.guardConst = guardConst;
    }

    public cjsidl_popTransition getCjsidl_poptransition() {
        return cjsidl_poptransition;
    }

    public void setCjsidl_poptransition(cjsidl_popTransition cjsidl_poptransition) {
        this.cjsidl_poptransition = cjsidl_poptransition;
    }
    public cjsidl_transParam getCjsidl_transparam() {
        return cjsidl_transparam;
    }

    public void setCjsidl_transparam(cjsidl_transParam cjsidl_transparam) {
        this.cjsidl_transparam = cjsidl_transparam;
    }

}