





import java.util.List;
import java.util.ArrayList;

public class library3_BookType  {

    private String pages;
    private String isbn;
    private String author;
    private String title;
    private String name;
    private String dimension;
    private String download;





    private library3_BookInfoType library3_bookinfotype;


    public library3_BookType(
        String pages,        String isbn,        String author,        String title,        String name,        String dimension,        String download    ) {
        this.pages = pages;
        this.isbn = isbn;
        this.author = author;
        this.title = title;
        this.name = name;
        this.dimension = dimension;
        this.download = download;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDimension() {
        return dimension;
    }

    public void setDimension(String dimension) {
        this.dimension = dimension;
    }
    public String getDownload() {
        return download;
    }

    public void setDownload(String download) {
        this.download = download;
    }

    public library3_BookInfoType getLibrary3_bookinfotype() {
        return library3_bookinfotype;
    }

    public void setLibrary3_bookinfotype(library3_BookInfoType library3_bookinfotype) {
        this.library3_bookinfotype = library3_bookinfotype;
    }

}