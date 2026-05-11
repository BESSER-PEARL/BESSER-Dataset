





import java.util.List;
import java.util.ArrayList;

public class scxml_OnEntry  {






    private List<scxml_Param> scxml_params;




    private List<scxml_Send> scxml_sends;




    private List<scxml_If> scxml_ifs;




    private List<scxml_Raise> scxml_raises;




    private scxml_State scxml_state;




    private List<scxml_Validate> scxml_validates;




    private List<scxml_Assign> scxml_assigns;




    private scxml_FinalState scxml_finalstate;




    private List<scxml_Log> scxml_logs;




    private scxml_Parallel scxml_parallel;


    public scxml_OnEntry(
    ) {
        this.scxml_params = new ArrayList<>();
        this.scxml_sends = new ArrayList<>();
        this.scxml_ifs = new ArrayList<>();
        this.scxml_raises = new ArrayList<>();
        this.scxml_validates = new ArrayList<>();
        this.scxml_assigns = new ArrayList<>();
        this.scxml_logs = new ArrayList<>();
    }

    public scxml_OnEntry(
        ArrayList<scxml_Param> scxml_params,        ArrayList<scxml_Send> scxml_sends,        ArrayList<scxml_If> scxml_ifs,        ArrayList<scxml_Raise> scxml_raises,        ArrayList<scxml_Validate> scxml_validates,        ArrayList<scxml_Assign> scxml_assigns,        ArrayList<scxml_Log> scxml_logs    ) {
        this.scxml_params = scxml_params;
        this.scxml_sends = scxml_sends;
        this.scxml_ifs = scxml_ifs;
        this.scxml_raises = scxml_raises;
        this.scxml_validates = scxml_validates;
        this.scxml_assigns = scxml_assigns;
        this.scxml_logs = scxml_logs;
    }


    public List<scxml_Param> getScxml_params() {
        return scxml_params;
    }

    public void addScxml_param(Scxml_param scxml_param) {
        this.scxml_params.add(scxml_param);
    }
    public List<scxml_Send> getScxml_sends() {
        return scxml_sends;
    }

    public void addScxml_send(Scxml_send scxml_send) {
        this.scxml_sends.add(scxml_send);
    }
    public List<scxml_If> getScxml_ifs() {
        return scxml_ifs;
    }

    public void addScxml_if(Scxml_if scxml_if) {
        this.scxml_ifs.add(scxml_if);
    }
    public List<scxml_Raise> getScxml_raises() {
        return scxml_raises;
    }

    public void addScxml_raise(Scxml_raise scxml_raise) {
        this.scxml_raises.add(scxml_raise);
    }
    public scxml_State getScxml_state() {
        return scxml_state;
    }

    public void setScxml_state(scxml_State scxml_state) {
        this.scxml_state = scxml_state;
    }
    public List<scxml_Validate> getScxml_validates() {
        return scxml_validates;
    }

    public void addScxml_validate(Scxml_validate scxml_validate) {
        this.scxml_validates.add(scxml_validate);
    }
    public List<scxml_Assign> getScxml_assigns() {
        return scxml_assigns;
    }

    public void addScxml_assign(Scxml_assign scxml_assign) {
        this.scxml_assigns.add(scxml_assign);
    }
    public scxml_FinalState getScxml_finalstate() {
        return scxml_finalstate;
    }

    public void setScxml_finalstate(scxml_FinalState scxml_finalstate) {
        this.scxml_finalstate = scxml_finalstate;
    }
    public List<scxml_Log> getScxml_logs() {
        return scxml_logs;
    }

    public void addScxml_log(Scxml_log scxml_log) {
        this.scxml_logs.add(scxml_log);
    }
    public scxml_Parallel getScxml_parallel() {
        return scxml_parallel;
    }

    public void setScxml_parallel(scxml_Parallel scxml_parallel) {
        this.scxml_parallel = scxml_parallel;
    }

}