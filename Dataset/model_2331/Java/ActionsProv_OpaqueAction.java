





import java.util.List;
import java.util.ArrayList;

public class ActionsProv_OpaqueAction extends Action {

    private String language;
    private String body;





    private List<ActionsProv_OutputPin> actionsprov_outputpins;


    public ActionsProv_OpaqueAction(
        String language,        String body    ) {
        super(
        );
        this.language = language;
        this.body = body;
        this.actionsprov_outputpins = new ArrayList<>();
    }

    public ActionsProv_OpaqueAction(
        String language,        String body        ArrayList<ActionsProv_OutputPin> actionsprov_outputpins    ) {
        this.language = language;
        this.body = body;
        this.actionsprov_outputpins = actionsprov_outputpins;
    }

    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    public List<ActionsProv_OutputPin> getActionsprov_outputpins() {
        return actionsprov_outputpins;
    }

    public void addActionsprov_outputpin(Actionsprov_outputpin actionsprov_outputpin) {
        this.actionsprov_outputpins.add(actionsprov_outputpin);
    }

}