





import java.util.List;
import java.util.ArrayList;

public class library3Simplified_Book  {

    private String title;
    private String dimension;
    private String author;
    private String download;
    private int pages;
    private String isbn;
    private String name;





    private library3Simplified_Library library3simplified_library;




    private library3Simplified_Customer library3simplified_customer;




    private library3Simplified_BookInfo library3simplified_bookinfo;


    public library3Simplified_Book(
        String title,        String dimension,        String author,        String download,        int pages,        String isbn,        String name    ) {
        this.title = title;
        this.dimension = dimension;
        this.author = author;
        this.download = download;
        this.pages = pages;
        this.isbn = isbn;
        this.name = name;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getDimension() {
        return dimension;
    }

    public void setDimension(String dimension) {
        this.dimension = dimension;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getDownload() {
        return download;
    }

    public void setDownload(String download) {
        this.download = download;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public library3Simplified_BookInfo getLibrary3simplified_bookinfo() {
        return library3simplified_bookinfo;
    }

    public void setLibrary3simplified_bookinfo(library3Simplified_BookInfo library3simplified_bookinfo) {
        this.library3simplified_bookinfo = library3simplified_bookinfo;
    }

}