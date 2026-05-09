





import java.util.List;
import java.util.ArrayList;

public class library_book  {

    private String pages;
    private String title;
    private String author;
    private String published;



    public library_book(
        String pages,        String title,        String author,        String published    ) {
        this.pages = pages;
        this.title = title;
        this.author = author;
        this.published = published;
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
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getPublished() {
        return published;
    }

    public void setPublished(String published) {
        this.published = published;
    }


}