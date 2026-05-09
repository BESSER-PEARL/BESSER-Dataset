





import java.util.List;
import java.util.ArrayList;

public class a_Book  {

    private String author;
    private String title;
    private String published;





    private a_Model a_model;


    public a_Book(
        String author,        String title,        String published    ) {
        this.author = author;
        this.title = title;
        this.published = published;
    }


    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getPublished() {
        return published;
    }

    public void setPublished(String published) {
        this.published = published;
    }

    public a_Model getA_model() {
        return a_model;
    }

    public void setA_model(a_Model a_model) {
        this.a_model = a_model;
    }

}