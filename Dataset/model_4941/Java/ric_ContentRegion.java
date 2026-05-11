





import java.util.List;
import java.util.ArrayList;

public class ric_ContentRegion  {






    private ric_Portal ric_portal;




    private List<ric_Document> ric_documents;


    public ric_ContentRegion(
    ) {
        this.ric_documents = new ArrayList<>();
    }

    public ric_ContentRegion(
        ArrayList<ric_Document> ric_documents    ) {
        this.ric_documents = ric_documents;
    }


    public ric_Portal getRic_portal() {
        return ric_portal;
    }

    public void setRic_portal(ric_Portal ric_portal) {
        this.ric_portal = ric_portal;
    }
    public List<ric_Document> getRic_documents() {
        return ric_documents;
    }

    public void addRic_document(Ric_document ric_document) {
        this.ric_documents.add(ric_document);
    }

}