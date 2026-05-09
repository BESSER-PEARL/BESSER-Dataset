





import java.util.List;
import java.util.ArrayList;

public class library3_BookType  {

    private String pages;
    private String title;
    private String name;
    private String author;
    private String isbn;





    private library3_BookInfoType library3_bookinfotype;


    public library3_BookType(
        String pages,        String title,        String name,        String author,        String isbn    ) {
        this.pages = pages;
        this.title = title;
        this.name = name;
        this.author = author;
        this.isbn = isbn;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }

    public library3_BookInfoType getLibrary3_bookinfotype() {
        return library3_bookinfotype;
    }

    public void setLibrary3_bookinfotype(library3_BookInfoType library3_bookinfotype) {
        this.library3_bookinfotype = library3_bookinfotype;
    }

}