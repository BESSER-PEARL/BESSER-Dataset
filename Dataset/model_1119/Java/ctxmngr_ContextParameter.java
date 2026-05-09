





import java.util.List;
import java.util.ArrayList;

public class ctxmngr_ContextParameter extends NamedElement {

    private boolean LitteralBoolean;
    private boolean isInput;
    private int LitteralInteger;
    private float LitteralUnlimitedNatural;
    private String LitteralString;





    private List<ctxmngr_OpaqueExpression> ctxmngr_opaqueexpressions;




    private List<ctxmngr_CtxState> ctxmngr_ctxstates;




    private ctxmngr_CtxState ctxmngr_ctxstate;




    private ctxmngr_ContextManager ctxmngr_contextmanager;




    private ctxmngr_ContextManager ctxmngr_contextmanager;


    public ctxmngr_ContextParameter(
        boolean LitteralBoolean,        boolean isInput,        int LitteralInteger,        float LitteralUnlimitedNatural,        String LitteralString    ) {
        super(
        );
        this.LitteralBoolean = LitteralBoolean;
        this.isInput = isInput;
        this.LitteralInteger = LitteralInteger;
        this.LitteralUnlimitedNatural = LitteralUnlimitedNatural;
        this.LitteralString = LitteralString;
        this.ctxmngr_opaqueexpressions = new ArrayList<>();
        this.ctxmngr_ctxstates = new ArrayList<>();
    }

    public ctxmngr_ContextParameter(
        boolean LitteralBoolean,        boolean isInput,        int LitteralInteger,        float LitteralUnlimitedNatural,        String LitteralString        ArrayList<ctxmngr_OpaqueExpression> ctxmngr_opaqueexpressions,        ArrayList<ctxmngr_CtxState> ctxmngr_ctxstates    ) {
        this.LitteralBoolean = LitteralBoolean;
        this.isInput = isInput;
        this.LitteralInteger = LitteralInteger;
        this.LitteralUnlimitedNatural = LitteralUnlimitedNatural;
        this.LitteralString = LitteralString;
        this.ctxmngr_opaqueexpressions = ctxmngr_opaqueexpressions;
        this.ctxmngr_ctxstates = ctxmngr_ctxstates;
    }

    public boolean getLitteralboolean() {
        return LitteralBoolean;
    }

    public void setLitteralboolean(boolean LitteralBoolean) {
        this.LitteralBoolean = LitteralBoolean;
    }
    public boolean getIsinput() {
        return isInput;
    }

    public void setIsinput(boolean isInput) {
        this.isInput = isInput;
    }
    public int getLitteralinteger() {
        return LitteralInteger;
    }

    public void setLitteralinteger(int LitteralInteger) {
        this.LitteralInteger = LitteralInteger;
    }
    public float getLitteralunlimitednatural() {
        return LitteralUnlimitedNatural;
    }

    public void setLitteralunlimitednatural(float LitteralUnlimitedNatural) {
        this.LitteralUnlimitedNatural = LitteralUnlimitedNatural;
    }
    public String getLitteralstring() {
        return LitteralString;
    }

    public void setLitteralstring(String LitteralString) {
        this.LitteralString = LitteralString;
    }

    public List<ctxmngr_OpaqueExpression> getCtxmngr_opaqueexpressions() {
        return ctxmngr_opaqueexpressions;
    }

    public void addCtxmngr_opaqueexpression(Ctxmngr_opaqueexpression ctxmngr_opaqueexpression) {
        this.ctxmngr_opaqueexpressions.add(ctxmngr_opaqueexpression);
    }
    public List<ctxmngr_CtxState> getCtxmngr_ctxstates() {
        return ctxmngr_ctxstates;
    }

    public void addCtxmngr_ctxstate(Ctxmngr_ctxstate ctxmngr_ctxstate) {
        this.ctxmngr_ctxstates.add(ctxmngr_ctxstate);
    }
    public ctxmngr_CtxState getCtxmngr_ctxstate() {
        return ctxmngr_ctxstate;
    }

    public void setCtxmngr_ctxstate(ctxmngr_CtxState ctxmngr_ctxstate) {
        this.ctxmngr_ctxstate = ctxmngr_ctxstate;
    }
    public ctxmngr_ContextManager getCtxmngr_contextmanager() {
        return ctxmngr_contextmanager;
    }

    public void setCtxmngr_contextmanager(ctxmngr_ContextManager ctxmngr_contextmanager) {
        this.ctxmngr_contextmanager = ctxmngr_contextmanager;
    }
    public ctxmngr_ContextManager getCtxmngr_contextmanager() {
        return ctxmngr_contextmanager;
    }

    public void setCtxmngr_contextmanager(ctxmngr_ContextManager ctxmngr_contextmanager) {
        this.ctxmngr_contextmanager = ctxmngr_contextmanager;
    }

}