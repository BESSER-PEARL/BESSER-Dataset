





import java.util.List;
import java.util.ArrayList;

public class model_xsd_XSDDiagnostic extends XSDConcreteComponent {

    private String locationURI;
    private int column;
    private String substitutions;
    private String key;
    private String node;
    private int line;
    private String severity;
    private String annotationURI;
    private String message;



    public model_xsd_XSDDiagnostic(
        String locationURI,        int column,        String substitutions,        String key,        String node,        int line,        String severity,        String annotationURI,        String message    ) {
        super(
        );
        this.locationURI = locationURI;
        this.column = column;
        this.substitutions = substitutions;
        this.key = key;
        this.node = node;
        this.line = line;
        this.severity = severity;
        this.annotationURI = annotationURI;
        this.message = message;
    }


    public String getLocationuri() {
        return locationURI;
    }

    public void setLocationuri(String locationURI) {
        this.locationURI = locationURI;
    }
    public int getColumn() {
        return column;
    }

    public void setColumn(int column) {
        this.column = column;
    }
    public String getSubstitutions() {
        return substitutions;
    }

    public void setSubstitutions(String substitutions) {
        this.substitutions = substitutions;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getNode() {
        return node;
    }

    public void setNode(String node) {
        this.node = node;
    }
    public int getLine() {
        return line;
    }

    public void setLine(int line) {
        this.line = line;
    }
    public String getSeverity() {
        return severity;
    }

    public void setSeverity(String severity) {
        this.severity = severity;
    }
    public String getAnnotationuri() {
        return annotationURI;
    }

    public void setAnnotationuri(String annotationURI) {
        this.annotationURI = annotationURI;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }


}