





import java.util.List;
import java.util.ArrayList;

public class edatatypeColumn_Book  {

    private String author;
    private String weight;
    private String pages;
    private String title;



    public edatatypeColumn_Book(
        String author,        String weight,        String pages,        String title    ) {
        this.author = author;
        this.weight = weight;
        this.pages = pages;
        this.title = title;
    }


    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getWeight() {
        return weight;
    }

    public void setWeight(String weight) {
        this.weight = weight;
    }
    public String getPages() {
        return pages;
    }

    public void setPages(String pages) {
        this.pages = pages;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }


}