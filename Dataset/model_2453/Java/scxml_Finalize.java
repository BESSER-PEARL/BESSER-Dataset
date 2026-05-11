





import java.util.List;
import java.util.ArrayList;

public class scxml_Finalize  {






    private List<scxml_Param> scxml_params;




    private List<scxml_If> scxml_ifs;




    private List<scxml_Log> scxml_logs;




    private List<scxml_Send> scxml_sends;




    private List<scxml_Validate> scxml_validates;




    private List<scxml_Assign> scxml_assigns;




    private List<scxml_Raise> scxml_raises;




    private scxml_Invoke scxml_invoke;


    public scxml_Finalize(
    ) {
        this.scxml_params = new ArrayList<>();
        this.scxml_ifs = new ArrayList<>();
        this.scxml_logs = new ArrayList<>();
        this.scxml_sends = new ArrayList<>();
        this.scxml_validates = new ArrayList<>();
        this.scxml_assigns = new ArrayList<>();
        this.scxml_raises = new ArrayList<>();
    }

    public scxml_Finalize(
        ArrayList<scxml_Param> scxml_params,        ArrayList<scxml_If> scxml_ifs,        ArrayList<scxml_Log> scxml_logs,        ArrayList<scxml_Send> scxml_sends,        ArrayList<scxml_Validate> scxml_validates,        ArrayList<scxml_Assign> scxml_assigns,        ArrayList<scxml_Raise> scxml_raises    ) {
        this.scxml_params = scxml_params;
        this.scxml_ifs = scxml_ifs;
        this.scxml_logs = scxml_logs;
        this.scxml_sends = scxml_sends;
        this.scxml_validates = scxml_validates;
        this.scxml_assigns = scxml_assigns;
        this.scxml_raises = scxml_raises;
    }


    public List<scxml_Param> getScxml_params() {
        return scxml_params;
    }

    public void addScxml_param(Scxml_param scxml_param) {
        this.scxml_params.add(scxml_param);
    }
    public List<scxml_If> getScxml_ifs() {
        return scxml_ifs;
    }

    public void addScxml_if(Scxml_if scxml_if) {
        this.scxml_ifs.add(scxml_if);
    }
    public List<scxml_Log> getScxml_logs() {
        return scxml_logs;
    }

    public void addScxml_log(Scxml_log scxml_log) {
        this.scxml_logs.add(scxml_log);
    }
    public List<scxml_Send> getScxml_sends() {
        return scxml_sends;
    }

    public void addScxml_send(Scxml_send scxml_send) {
        this.scxml_sends.add(scxml_send);
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
    public List<scxml_Raise> getScxml_raises() {
        return scxml_raises;
    }

    public void addScxml_raise(Scxml_raise scxml_raise) {
        this.scxml_raises.add(scxml_raise);
    }
    public scxml_Invoke getScxml_invoke() {
        return scxml_invoke;
    }

    public void setScxml_invoke(scxml_Invoke scxml_invoke) {
        this.scxml_invoke = scxml_invoke;
    }

}