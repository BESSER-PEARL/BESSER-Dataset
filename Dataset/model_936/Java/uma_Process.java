





import java.util.List;
import java.util.ArrayList;

public class uma_Process extends Activity {

    private String validContext;
    private String defaultContext;
    private String diagramURI;
    private String includesPattern;



    public uma_Process(
        String validContext,        String defaultContext,        String diagramURI,        String includesPattern    ) {
        super(
        );
        this.validContext = validContext;
        this.defaultContext = defaultContext;
        this.diagramURI = diagramURI;
        this.includesPattern = includesPattern;
    }


    public String getValidcontext() {
        return validContext;
    }

    public void setValidcontext(String validContext) {
        this.validContext = validContext;
    }
    public String getDefaultcontext() {
        return defaultContext;
    }

    public void setDefaultcontext(String defaultContext) {
        this.defaultContext = defaultContext;
    }
    public String getDiagramuri() {
        return diagramURI;
    }

    public void setDiagramuri(String diagramURI) {
        this.diagramURI = diagramURI;
    }
    public String getIncludespattern() {
        return includesPattern;
    }

    public void setIncludespattern(String includesPattern) {
        this.includesPattern = includesPattern;
    }


}