





import java.util.List;
import java.util.ArrayList;

public class dg_RootCanvas extends Canvas {

    private String script;
    private String backgroundColor;





    private dg_Definitions dg_definitions;




    private List<dg_StyleSheet> dg_stylesheets;


    public dg_RootCanvas(
        String script,        String backgroundColor    ) {
        super(
        );
        this.script = script;
        this.backgroundColor = backgroundColor;
        this.dg_stylesheets = new ArrayList<>();
    }

    public dg_RootCanvas(
        String script,        String backgroundColor        ArrayList<dg_StyleSheet> dg_stylesheets    ) {
        this.script = script;
        this.backgroundColor = backgroundColor;
        this.dg_stylesheets = dg_stylesheets;
    }

    public String getScript() {
        return script;
    }

    public void setScript(String script) {
        this.script = script;
    }
    public String getBackgroundcolor() {
        return backgroundColor;
    }

    public void setBackgroundcolor(String backgroundColor) {
        this.backgroundColor = backgroundColor;
    }

    public dg_Definitions getDg_definitions() {
        return dg_definitions;
    }

    public void setDg_definitions(dg_Definitions dg_definitions) {
        this.dg_definitions = dg_definitions;
    }
    public List<dg_StyleSheet> getDg_stylesheets() {
        return dg_stylesheets;
    }

    public void addDg_stylesheet(Dg_stylesheet dg_stylesheet) {
        this.dg_stylesheets.add(dg_stylesheet);
    }

}