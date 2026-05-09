





import java.util.List;
import java.util.ArrayList;

public class column_Book  {

    private String title;
    private String pages;
    private String weight;
    private String author;



    public column_Book(
        String title,        String pages,        String weight,        String author    ) {
        this.title = title;
        this.pages = pages;
        this.weight = weight;
        this.author = author;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getPages() {
        return pages;
    }

    public void setPages(String pages) {
        this.pages = pages;
    }
    public String getWeight() {
        return weight;
    }

    public void setWeight(String weight) {
        this.weight = weight;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }


}