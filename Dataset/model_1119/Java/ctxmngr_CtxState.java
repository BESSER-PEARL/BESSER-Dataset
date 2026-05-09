





import java.util.List;
import java.util.ArrayList;

public class ctxmngr_CtxState extends NamedElement {

    private boolean isEnd;
    private boolean isStart;





    private List<ctxmngr_CtxTransition> ctxmngr_ctxtransitions;




    private ctxmngr_ContextManager ctxmngr_contextmanager;




    private List<ctxmngr_CtxTransition> ctxmngr_ctxtransitions;




    private ctxmngr_CtxTransition ctxmngr_ctxtransition;




    private ctxmngr_CtxTransition ctxmngr_ctxtransition;




    private ctxmngr_ContextManager ctxmngr_contextmanager;




    private ctxmngr_ContextManager ctxmngr_contextmanager;




    private List<ctxmngr_ManagerState> ctxmngr_managerstates;




    private ctxmngr_ContextManager ctxmngr_contextmanager;


    public ctxmngr_CtxState(
        boolean isEnd,        boolean isStart    ) {
        super(
        );
        this.isEnd = isEnd;
        this.isStart = isStart;
        this.ctxmngr_ctxtransitions = new ArrayList<>();
        this.ctxmngr_ctxtransitions = new ArrayList<>();
        this.ctxmngr_managerstates = new ArrayList<>();
    }

    public ctxmngr_CtxState(
        boolean isEnd,        boolean isStart        ArrayList<ctxmngr_CtxTransition> ctxmngr_ctxtransitions,        ArrayList<ctxmngr_CtxTransition> ctxmngr_ctxtransitions,        ArrayList<ctxmngr_ManagerState> ctxmngr_managerstates    ) {
        this.isEnd = isEnd;
        this.isStart = isStart;
        this.ctxmngr_ctxtransitions = ctxmngr_ctxtransitions;
        this.ctxmngr_ctxtransitions = ctxmngr_ctxtransitions;
        this.ctxmngr_managerstates = ctxmngr_managerstates;
    }

    public boolean getIsend() {
        return isEnd;
    }

    public void setIsend(boolean isEnd) {
        this.isEnd = isEnd;
    }
    public boolean getIsstart() {
        return isStart;
    }

    public void setIsstart(boolean isStart) {
        this.isStart = isStart;
    }

    public List<ctxmngr_CtxTransition> getCtxmngr_ctxtransitions() {
        return ctxmngr_ctxtransitions;
    }

    public void addCtxmngr_ctxtransition(Ctxmngr_ctxtransition ctxmngr_ctxtransition) {
        this.ctxmngr_ctxtransitions.add(ctxmngr_ctxtransition);
    }
    public ctxmngr_ContextManager getCtxmngr_contextmanager() {
        return ctxmngr_contextmanager;
    }

    public void setCtxmngr_contextmanager(ctxmngr_ContextManager ctxmngr_contextmanager) {
        this.ctxmngr_contextmanager = ctxmngr_contextmanager;
    }
    public List<ctxmngr_CtxTransition> getCtxmngr_ctxtransitions() {
        return ctxmngr_ctxtransitions;
    }

    public void addCtxmngr_ctxtransition(Ctxmngr_ctxtransition ctxmngr_ctxtransition) {
        this.ctxmngr_ctxtransitions.add(ctxmngr_ctxtransition);
    }
    public ctxmngr_CtxTransition getCtxmngr_ctxtransition() {
        return ctxmngr_ctxtransition;
    }

    public void setCtxmngr_ctxtransition(ctxmngr_CtxTransition ctxmngr_ctxtransition) {
        this.ctxmngr_ctxtransition = ctxmngr_ctxtransition;
    }
    public ctxmngr_CtxTransition getCtxmngr_ctxtransition() {
        return ctxmngr_ctxtransition;
    }

    public void setCtxmngr_ctxtransition(ctxmngr_CtxTransition ctxmngr_ctxtransition) {
        this.ctxmngr_ctxtransition = ctxmngr_ctxtransition;
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
    public List<ctxmngr_ManagerState> getCtxmngr_managerstates() {
        return ctxmngr_managerstates;
    }

    public void addCtxmngr_managerstate(Ctxmngr_managerstate ctxmngr_managerstate) {
        this.ctxmngr_managerstates.add(ctxmngr_managerstate);
    }
    public ctxmngr_ContextManager getCtxmngr_contextmanager() {
        return ctxmngr_contextmanager;
    }

    public void setCtxmngr_contextmanager(ctxmngr_ContextManager ctxmngr_contextmanager) {
        this.ctxmngr_contextmanager = ctxmngr_contextmanager;
    }

}