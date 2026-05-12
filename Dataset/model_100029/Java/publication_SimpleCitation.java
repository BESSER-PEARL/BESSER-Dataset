




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class publication_SimpleCitation extends SimpleFeature {

    private String source;
    private LocalDate date;
    private String authorList;





    private publication_BiblioReferenceSet publication_biblioreferenceset;


    public publication_SimpleCitation(
        String source,        LocalDate date,        String authorList    ) {
        super(
        );
        this.source = source;
        this.date = date;
        this.authorList = authorList;
    }


    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public String getAuthorlist() {
        return authorList;
    }

    public void setAuthorlist(String authorList) {
        this.authorList = authorList;
    }

    public publication_BiblioReferenceSet getPublication_biblioreferenceset() {
        return publication_biblioreferenceset;
    }

    public void setPublication_biblioreferenceset(publication_BiblioReferenceSet publication_biblioreferenceset) {
        this.publication_biblioreferenceset = publication_biblioreferenceset;
    }

}