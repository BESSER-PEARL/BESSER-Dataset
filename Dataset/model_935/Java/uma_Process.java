





import java.util.List;
import java.util.ArrayList;

public class uma_Process extends Activity {

    private String includesPattern;
    private String diagramURI;
    private String defaultContext;
    private String validContext;



    public uma_Process(
        String includesPattern,        String diagramURI,        String defaultContext,        String validContext    ) {
        super(
        );
        this.includesPattern = includesPattern;
        this.diagramURI = diagramURI;
        this.defaultContext = defaultContext;
        this.validContext = validContext;
    }


    public String getIncludespattern() {
        return includesPattern;
    }

    public void setIncludespattern(String includesPattern) {
        this.includesPattern = includesPattern;
    }
    public String getDiagramuri() {
        return diagramURI;
    }

    public void setDiagramuri(String diagramURI) {
        this.diagramURI = diagramURI;
    }
    public String getDefaultcontext() {
        return defaultContext;
    }

    public void setDefaultcontext(String defaultContext) {
        this.defaultContext = defaultContext;
    }
    public String getValidcontext() {
        return validContext;
    }

    public void setValidcontext(String validContext) {
        this.validContext = validContext;
    }


}