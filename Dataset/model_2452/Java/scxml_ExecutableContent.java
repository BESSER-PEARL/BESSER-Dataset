





import java.util.List;
import java.util.ArrayList;

public class scxml_ExecutableContent  {

    private String group;





    private List<scxml_Script> scxml_scripts;




    private List<scxml_Raise> scxml_raises;




    private List<scxml_If> scxml_ifs;




    private scxml_Invoke scxml_invoke;




    private List<scxml_Log> scxml_logs;


    public scxml_ExecutableContent(
        String group    ) {
        this.group = group;
        this.scxml_scripts = new ArrayList<>();
        this.scxml_raises = new ArrayList<>();
        this.scxml_ifs = new ArrayList<>();
        this.scxml_logs = new ArrayList<>();
    }

    public scxml_ExecutableContent(
        String group        ArrayList<scxml_Script> scxml_scripts,        ArrayList<scxml_Raise> scxml_raises,        ArrayList<scxml_If> scxml_ifs,        ArrayList<scxml_Log> scxml_logs    ) {
        this.group = group;
        this.scxml_scripts = scxml_scripts;
        this.scxml_raises = scxml_raises;
        this.scxml_ifs = scxml_ifs;
        this.scxml_logs = scxml_logs;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public List<scxml_Script> getScxml_scripts() {
        return scxml_scripts;
    }

    public void addScxml_script(Scxml_script scxml_script) {
        this.scxml_scripts.add(scxml_script);
    }
    public List<scxml_Raise> getScxml_raises() {
        return scxml_raises;
    }

    public void addScxml_raise(Scxml_raise scxml_raise) {
        this.scxml_raises.add(scxml_raise);
    }
    public List<scxml_If> getScxml_ifs() {
        return scxml_ifs;
    }

    public void addScxml_if(Scxml_if scxml_if) {
        this.scxml_ifs.add(scxml_if);
    }
    public scxml_Invoke getScxml_invoke() {
        return scxml_invoke;
    }

    public void setScxml_invoke(scxml_Invoke scxml_invoke) {
        this.scxml_invoke = scxml_invoke;
    }
    public List<scxml_Log> getScxml_logs() {
        return scxml_logs;
    }

    public void addScxml_log(Scxml_log scxml_log) {
        this.scxml_logs.add(scxml_log);
    }

}