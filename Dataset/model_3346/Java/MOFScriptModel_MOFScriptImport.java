





import java.util.List;
import java.util.ArrayList;

public class MOFScriptModel_MOFScriptImport extends MOFScriptObject {

    private String name;
    private String uri;
    private String importSemantics;
    private String type;



    public MOFScriptModel_MOFScriptImport(
        String name,        String uri,        String importSemantics,        String type    ) {
        super(
        );
        this.name = name;
        this.uri = uri;
        this.importSemantics = importSemantics;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }
    public String getImportsemantics() {
        return importSemantics;
    }

    public void setImportsemantics(String importSemantics) {
        this.importSemantics = importSemantics;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}