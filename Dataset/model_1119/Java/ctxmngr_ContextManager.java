





import java.util.List;
import java.util.ArrayList;

public class ctxmngr_ContextManager extends NamedElement {






    private List<ctxmngr_RemoteFiringDependency> ctxmngr_remotefiringdependencys;




    private ctxmngr_CtxTransition ctxmngr_ctxtransition;




    private List<ctxmngr_CtxTransition> ctxmngr_ctxtransitions;




    private List<ctxmngr_Manager> ctxmngr_managers;




    private ctxmngr_RemoteFiringDependency ctxmngr_remotefiringdependency;


    public ctxmngr_ContextManager(
    ) {
        super(
        );
        this.ctxmngr_remotefiringdependencys = new ArrayList<>();
        this.ctxmngr_ctxtransitions = new ArrayList<>();
        this.ctxmngr_managers = new ArrayList<>();
    }

    public ctxmngr_ContextManager(
        ArrayList<ctxmngr_RemoteFiringDependency> ctxmngr_remotefiringdependencys,        ArrayList<ctxmngr_CtxTransition> ctxmngr_ctxtransitions,        ArrayList<ctxmngr_Manager> ctxmngr_managers    ) {
        this.ctxmngr_remotefiringdependencys = ctxmngr_remotefiringdependencys;
        this.ctxmngr_ctxtransitions = ctxmngr_ctxtransitions;
        this.ctxmngr_managers = ctxmngr_managers;
    }


    public List<ctxmngr_RemoteFiringDependency> getCtxmngr_remotefiringdependencys() {
        return ctxmngr_remotefiringdependencys;
    }

    public void addCtxmngr_remotefiringdependency(Ctxmngr_remotefiringdependency ctxmngr_remotefiringdependency) {
        this.ctxmngr_remotefiringdependencys.add(ctxmngr_remotefiringdependency);
    }
    public ctxmngr_CtxTransition getCtxmngr_ctxtransition() {
        return ctxmngr_ctxtransition;
    }

    public void setCtxmngr_ctxtransition(ctxmngr_CtxTransition ctxmngr_ctxtransition) {
        this.ctxmngr_ctxtransition = ctxmngr_ctxtransition;
    }
    public List<ctxmngr_CtxTransition> getCtxmngr_ctxtransitions() {
        return ctxmngr_ctxtransitions;
    }

    public void addCtxmngr_ctxtransition(Ctxmngr_ctxtransition ctxmngr_ctxtransition) {
        this.ctxmngr_ctxtransitions.add(ctxmngr_ctxtransition);
    }
    public List<ctxmngr_Manager> getCtxmngr_managers() {
        return ctxmngr_managers;
    }

    public void addCtxmngr_manager(Ctxmngr_manager ctxmngr_manager) {
        this.ctxmngr_managers.add(ctxmngr_manager);
    }
    public ctxmngr_RemoteFiringDependency getCtxmngr_remotefiringdependency() {
        return ctxmngr_remotefiringdependency;
    }

    public void setCtxmngr_remotefiringdependency(ctxmngr_RemoteFiringDependency ctxmngr_remotefiringdependency) {
        this.ctxmngr_remotefiringdependency = ctxmngr_remotefiringdependency;
    }

}