





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_OpaqueAction extends Action {

    private String language;
    private String body;





    private List<CompleteDSLPckg_OutputPin> completedslpckg_outputpins;




    private List<CompleteDSLPckg_InputPin> completedslpckg_inputpins;


    public CompleteDSLPckg_OpaqueAction(
        String language,        String body    ) {
        super(
        );
        this.language = language;
        this.body = body;
        this.completedslpckg_outputpins = new ArrayList<>();
        this.completedslpckg_inputpins = new ArrayList<>();
    }

    public CompleteDSLPckg_OpaqueAction(
        String language,        String body        ArrayList<CompleteDSLPckg_OutputPin> completedslpckg_outputpins,        ArrayList<CompleteDSLPckg_InputPin> completedslpckg_inputpins    ) {
        this.language = language;
        this.body = body;
        this.completedslpckg_outputpins = completedslpckg_outputpins;
        this.completedslpckg_inputpins = completedslpckg_inputpins;
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

    public List<CompleteDSLPckg_OutputPin> getCompletedslpckg_outputpins() {
        return completedslpckg_outputpins;
    }

    public void addCompletedslpckg_outputpin(Completedslpckg_outputpin completedslpckg_outputpin) {
        this.completedslpckg_outputpins.add(completedslpckg_outputpin);
    }
    public List<CompleteDSLPckg_InputPin> getCompletedslpckg_inputpins() {
        return completedslpckg_inputpins;
    }

    public void addCompletedslpckg_inputpin(Completedslpckg_inputpin completedslpckg_inputpin) {
        this.completedslpckg_inputpins.add(completedslpckg_inputpin);
    }

}