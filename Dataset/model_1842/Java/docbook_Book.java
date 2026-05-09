





import java.util.List;
import java.util.ArrayList;

public class docbook_Book  {






    private docbook_DocBook docbook_docbook;




    private List<docbook_Article> docbook_articles;


    public docbook_Book(
    ) {
        this.docbook_articles = new ArrayList<>();
    }

    public docbook_Book(
        ArrayList<docbook_Article> docbook_articles    ) {
        this.docbook_articles = docbook_articles;
    }


    public docbook_DocBook getDocbook_docbook() {
        return docbook_docbook;
    }

    public void setDocbook_docbook(docbook_DocBook docbook_docbook) {
        this.docbook_docbook = docbook_docbook;
    }
    public List<docbook_Article> getDocbook_articles() {
        return docbook_articles;
    }

    public void addDocbook_article(Docbook_article docbook_article) {
        this.docbook_articles.add(docbook_article);
    }

}