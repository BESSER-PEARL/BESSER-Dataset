





import java.util.List;
import java.util.ArrayList;

public class publicationExample_Humanity  {






    private List<publicationExample_Publication> publicationexample_publications;


    public publicationExample_Humanity(
    ) {
        this.publicationexample_publications = new ArrayList<>();
    }

    public publicationExample_Humanity(
        ArrayList<publicationExample_Publication> publicationexample_publications    ) {
        this.publicationexample_publications = publicationexample_publications;
    }


    public List<publicationExample_Publication> getPublicationexample_publications() {
        return publicationexample_publications;
    }

    public void addPublicationexample_publication(Publicationexample_publication publicationexample_publication) {
        this.publicationexample_publications.add(publicationexample_publication);
    }

}