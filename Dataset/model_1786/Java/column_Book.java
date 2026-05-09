





import java.util.List;
import java.util.ArrayList;

public class column_Book  {

    private String weight;
    private String pages;
    private String author;
    private String title;



    public column_Book(
        String weight,        String pages,        String author,        String title    ) {
        this.weight = weight;
        this.pages = pages;
        this.author = author;
        this.title = title;
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


}