





import java.util.List;
import java.util.ArrayList;

public class library3Simplified_Book  {

    private String name;
    private String isbn;
    private int pages;
    private String dimension;
    private String title;
    private String download;
    private String author;





    private library3Simplified_BookInfo library3simplified_bookinfo;


    public library3Simplified_Book(
        String name,        String isbn,        int pages,        String dimension,        String title,        String download,        String author    ) {
        this.name = name;
        this.isbn = isbn;
        this.pages = pages;
        this.dimension = dimension;
        this.title = title;
        this.download = download;
        this.author = author;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }
    public int getPages() {
        return pages;
    }

    public void setPages(int pages) {
        this.pages = pages;
    }
    public String getDimension() {
        return dimension;
    }

    public void setDimension(String dimension) {
        this.dimension = dimension;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getDownload() {
        return download;
    }

    public void setDownload(String download) {
        this.download = download;
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

}