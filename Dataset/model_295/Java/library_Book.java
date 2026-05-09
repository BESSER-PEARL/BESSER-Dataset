





import java.util.List;
import java.util.ArrayList;

public class library_Book  {

    private int pages;
    private String title;
    private String category;





    private library_Library library_library;




    private library_Writer library_writer;




    private library_Book library_book;




    private library_Writer library_writer;


    public library_Book(
        int pages,        String title,        String category    ) {
        this.pages = pages;
        this.title = title;
        this.category = category;
    }


    public int getPages() {
        return pages;
    }

    public void setPages(int pages) {
        this.pages = pages;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public library_Library getLibrary_library() {
        return library_library;
    }

    public void setLibrary_library(library_Library library_library) {
        this.library_library = library_library;
    }
    public library_Writer getLibrary_writer() {
        return library_writer;
    }

    public void setLibrary_writer(library_Writer library_writer) {
        this.library_writer = library_writer;
    }
    public library_Book getLibrary_book() {
        return library_book;
    }

    public void setLibrary_book(library_Book library_book) {
        this.library_book = library_book;
    }
    public library_Writer getLibrary_writer() {
        return library_writer;
    }

    public void setLibrary_writer(library_Writer library_writer) {
        this.library_writer = library_writer;
    }

}