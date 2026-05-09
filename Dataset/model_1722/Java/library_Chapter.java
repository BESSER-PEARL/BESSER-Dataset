





import java.util.List;
import java.util.ArrayList;

public class library_Chapter  {

    private int pages;
    private String name;





    private library_Book library_book;


    public library_Chapter(
        int pages,        String name    ) {
        this.pages = pages;
        this.name = name;
    }


    public int getPages() {
        return pages;
    }

    public void setPages(int pages) {
        this.pages = pages;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public library_Book getLibrary_book() {
        return library_book;
    }

    public void setLibrary_book(library_Book library_book) {
        this.library_book = library_book;
    }

}