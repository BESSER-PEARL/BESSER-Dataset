





import java.util.List;
import java.util.ArrayList;

public class uma_Process extends Activity {

    private String defaultContext;
    private String includesPattern;
    private String validContext;
    private String diagramURI;



    public uma_Process(
        String defaultContext,        String includesPattern,        String validContext,        String diagramURI    ) {
        super(
        );
        this.defaultContext = defaultContext;
        this.includesPattern = includesPattern;
        this.validContext = validContext;
        this.diagramURI = diagramURI;
    }


    public String getDefaultcontext() {
        return defaultContext;
    }

    public void setDefaultcontext(String defaultContext) {
        this.defaultContext = defaultContext;
    }
    public String getIncludespattern() {
        return includesPattern;
    }

    public void setIncludespattern(String includesPattern) {
        this.includesPattern = includesPattern;
    }
    public String getValidcontext() {
        return validContext;
    }

    public void setValidcontext(String validContext) {
        this.validContext = validContext;
    }
    public String getDiagramuri() {
        return diagramURI;
    }

    public void setDiagramuri(String diagramURI) {
        this.diagramURI = diagramURI;
    }


}