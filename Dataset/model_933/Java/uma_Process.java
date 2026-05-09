





import java.util.List;
import java.util.ArrayList;

public class uma_Process extends Activity {

    private String diagramURI;
    private String validContext;
    private String includesPattern;
    private String defaultContext;



    public uma_Process(
        String diagramURI,        String validContext,        String includesPattern,        String defaultContext    ) {
        super(
        );
        this.diagramURI = diagramURI;
        this.validContext = validContext;
        this.includesPattern = includesPattern;
        this.defaultContext = defaultContext;
    }


    public String getDiagramuri() {
        return diagramURI;
    }

    public void setDiagramuri(String diagramURI) {
        this.diagramURI = diagramURI;
    }
    public String getValidcontext() {
        return validContext;
    }

    public void setValidcontext(String validContext) {
        this.validContext = validContext;
    }
    public String getIncludespattern() {
        return includesPattern;
    }

    public void setIncludespattern(String includesPattern) {
        this.includesPattern = includesPattern;
    }
    public String getDefaultcontext() {
        return defaultContext;
    }

    public void setDefaultcontext(String defaultContext) {
        this.defaultContext = defaultContext;
    }


}