





import java.util.List;
import java.util.ArrayList;

public class Library3_BookType  {

    private String pages;
    private String isbn;
    private String title;
    private String author;
    private String name;



    public Library3_BookType(
        String pages,        String isbn,        String title,        String author,        String name    ) {
        this.pages = pages;
        this.isbn = isbn;
        this.title = title;
        this.author = author;
        this.name = name;
    }


    public String getPages() {
        return pages;
    }

    public void setPages(String pages) {
        this.pages = pages;
    }
    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}