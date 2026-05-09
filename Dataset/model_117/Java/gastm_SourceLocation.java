





import java.util.List;
import java.util.ArrayList;

public class gastm_SourceLocation extends GASTMSourceObject {

    private String startLine;
    private String endLine;
    private String endPosition;
    private String startPosition;





    private gastm_SourceFileReference gastm_sourcefilereference;




    private gastm_GASTMSyntaxObject gastm_gastmsyntaxobject;


    public gastm_SourceLocation(
        String startLine,        String endLine,        String endPosition,        String startPosition    ) {
        super(
        );
        this.startLine = startLine;
        this.endLine = endLine;
        this.endPosition = endPosition;
        this.startPosition = startPosition;
    }


    public String getStartline() {
        return startLine;
    }

    public void setStartline(String startLine) {
        this.startLine = startLine;
    }
    public String getEndline() {
        return endLine;
    }

    public void setEndline(String endLine) {
        this.endLine = endLine;
    }
    public String getEndposition() {
        return endPosition;
    }

    public void setEndposition(String endPosition) {
        this.endPosition = endPosition;
    }
    public String getStartposition() {
        return startPosition;
    }

    public void setStartposition(String startPosition) {
        this.startPosition = startPosition;
    }

    public gastm_SourceFileReference getGastm_sourcefilereference() {
        return gastm_sourcefilereference;
    }

    public void setGastm_sourcefilereference(gastm_SourceFileReference gastm_sourcefilereference) {
        this.gastm_sourcefilereference = gastm_sourcefilereference;
    }
    public gastm_GASTMSyntaxObject getGastm_gastmsyntaxobject() {
        return gastm_gastmsyntaxobject;
    }

    public void setGastm_gastmsyntaxobject(gastm_GASTMSyntaxObject gastm_gastmsyntaxobject) {
        this.gastm_gastmsyntaxobject = gastm_gastmsyntaxobject;
    }

}