





import java.util.List;
import java.util.ArrayList;

public class DocBook_Book  {






    private List<DocBook_Article> docbook_articles;




    private DocBook_DocBook docbook_docbook;


    public DocBook_Book(
    ) {
        this.docbook_articles = new ArrayList<>();
    }

    public DocBook_Book(
        ArrayList<DocBook_Article> docbook_articles    ) {
        this.docbook_articles = docbook_articles;
    }


    public List<DocBook_Article> getDocbook_articles() {
        return docbook_articles;
    }

    public void addDocbook_article(Docbook_article docbook_article) {
        this.docbook_articles.add(docbook_article);
    }
    public DocBook_DocBook getDocbook_docbook() {
        return docbook_docbook;
    }

    public void setDocbook_docbook(DocBook_DocBook docbook_docbook) {
        this.docbook_docbook = docbook_docbook;
    }

}