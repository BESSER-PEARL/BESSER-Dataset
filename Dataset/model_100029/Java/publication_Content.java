





import java.util.List;
import java.util.ArrayList;

public class publication_Content extends SimpleFeature {

    private String body;





    private publication_BiblioReference publication_biblioreference;




    private publication_BiblioReference publication_biblioreference;


    public publication_Content(
        String body    ) {
        super(
        );
        this.body = body;
    }


    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    public publication_BiblioReference getPublication_biblioreference() {
        return publication_biblioreference;
    }

    public void setPublication_biblioreference(publication_BiblioReference publication_biblioreference) {
        this.publication_biblioreference = publication_biblioreference;
    }
    public publication_BiblioReference getPublication_biblioreference() {
        return publication_biblioreference;
    }

    public void setPublication_biblioreference(publication_BiblioReference publication_biblioreference) {
        this.publication_biblioreference = publication_biblioreference;
    }

}