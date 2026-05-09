





import java.util.List;
import java.util.ArrayList;

public class graphbt_AuthorList  {






    private List<graphbt_Author> graphbt_authors;


    public graphbt_AuthorList(
    ) {
        this.graphbt_authors = new ArrayList<>();
    }

    public graphbt_AuthorList(
        ArrayList<graphbt_Author> graphbt_authors    ) {
        this.graphbt_authors = graphbt_authors;
    }


    public List<graphbt_Author> getGraphbt_authors() {
        return graphbt_authors;
    }

    public void addGraphbt_author(Graphbt_author graphbt_author) {
        this.graphbt_authors.add(graphbt_author);
    }

}