





import java.util.List;
import java.util.ArrayList;

public class doc_book_Book extends BookContainer {

    private String version;
    private String copyrightText;
    private String copyrightMarker;
    private String title;



    public doc_book_Book(
        String version,        String copyrightText,        String copyrightMarker,        String title    ) {
        super(
        );
        this.version = version;
        this.copyrightText = copyrightText;
        this.copyrightMarker = copyrightMarker;
        this.title = title;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getCopyrighttext() {
        return copyrightText;
    }

    public void setCopyrighttext(String copyrightText) {
        this.copyrightText = copyrightText;
    }
    public String getCopyrightmarker() {
        return copyrightMarker;
    }

    public void setCopyrightmarker(String copyrightMarker) {
        this.copyrightMarker = copyrightMarker;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }


}