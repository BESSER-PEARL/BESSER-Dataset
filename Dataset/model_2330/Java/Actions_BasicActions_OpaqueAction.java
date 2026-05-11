





import java.util.List;
import java.util.ArrayList;

public class Actions_BasicActions_OpaqueAction extends Action {

    private String body;
    private String language;





    private List<OutputPin> outputpins;




    private List<InputPin> inputpins;


    public Actions_BasicActions_OpaqueAction(
        String body,        String language    ) {
        super(
        );
        this.body = body;
        this.language = language;
        this.outputpins = new ArrayList<>();
        this.inputpins = new ArrayList<>();
    }

    public Actions_BasicActions_OpaqueAction(
        String body,        String language        ArrayList<OutputPin> outputpins,        ArrayList<InputPin> inputpins    ) {
        this.body = body;
        this.language = language;
        this.outputpins = outputpins;
        this.inputpins = inputpins;
    }

    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }
    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }

    public List<OutputPin> getOutputpins() {
        return outputpins;
    }

    public void addOutputpin(Outputpin outputpin) {
        this.outputpins.add(outputpin);
    }
    public List<InputPin> getInputpins() {
        return inputpins;
    }

    public void addInputpin(Inputpin inputpin) {
        this.inputpins.add(inputpin);
    }

}