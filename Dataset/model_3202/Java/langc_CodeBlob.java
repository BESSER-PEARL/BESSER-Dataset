





import java.util.List;
import java.util.ArrayList;

public class langc_CodeBlob extends CodeBlock {

    private String markerComment;
    private String text;





    private langc_DependencyBlob langc_dependencyblob;


    public langc_CodeBlob(
        String markerComment,        String text    ) {
        super(
        );
        this.markerComment = markerComment;
        this.text = text;
    }


    public String getMarkercomment() {
        return markerComment;
    }

    public void setMarkercomment(String markerComment) {
        this.markerComment = markerComment;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public langc_DependencyBlob getLangc_dependencyblob() {
        return langc_dependencyblob;
    }

    public void setLangc_dependencyblob(langc_DependencyBlob langc_dependencyblob) {
        this.langc_dependencyblob = langc_dependencyblob;
    }

}