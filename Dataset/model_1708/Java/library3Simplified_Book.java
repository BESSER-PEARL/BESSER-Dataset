





import java.util.List;
import java.util.ArrayList;

public class library3Simplified_Book  {

    private int pages;
    private String isbn;
    private String title;
    private String name;
    private String author;





    private library3Simplified_BookInfo library3simplified_bookinfo;




    private library3Simplified_Library library3simplified_library;




    private library3Simplified_Customer library3simplified_customer;


    public library3Simplified_Book(
        int pages,        String isbn,        String title,        String name,        String author    ) {
        this.pages = pages;
        this.isbn = isbn;
        this.title = title;
        this.name = name;
        this.author = author;
    }


    public int getPages() {
        return pages;
    }

    public void setPages(int pages) {
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

    public library3Simplified_BookInfo getLibrary3simplified_bookinfo() {
        return library3simplified_bookinfo;
    }

    public void setLibrary3simplified_bookinfo(library3Simplified_BookInfo library3simplified_bookinfo) {
        this.library3simplified_bookinfo = library3simplified_bookinfo;
    }
    public library3Simplified_Library getLibrary3simplified_library() {
        return library3simplified_library;
    }

    public void setLibrary3simplified_library(library3Simplified_Library library3simplified_library) {
        this.library3simplified_library = library3simplified_library;
    }
    public library3Simplified_Customer getLibrary3simplified_customer() {
        return library3simplified_customer;
    }

    public void setLibrary3simplified_customer(library3Simplified_Customer library3simplified_customer) {
        this.library3simplified_customer = library3simplified_customer;
    }

}