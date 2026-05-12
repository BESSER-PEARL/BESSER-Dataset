





import java.util.List;
import java.util.ArrayList;

public class LaTeX_Document  {






    private Author author;




    private Date date;




    private Title title;




    private DocumentBody documentbody;




    private Heading heading;


    public LaTeX_Document(
    ) {
    }



    public Author getAuthor() {
        return author;
    }

    public void setAuthor(Author author) {
        this.author = author;
    }
    public Date getDate() {
        return date;
    }

    public void setDate(Date date) {
        this.date = date;
    }
    public Title getTitle() {
        return title;
    }

    public void setTitle(Title title) {
        this.title = title;
    }
    public DocumentBody getDocumentbody() {
        return documentbody;
    }

    public void setDocumentbody(DocumentBody documentbody) {
        this.documentbody = documentbody;
    }
    public Heading getHeading() {
        return heading;
    }

    public void setHeading(Heading heading) {
        this.heading = heading;
    }

}