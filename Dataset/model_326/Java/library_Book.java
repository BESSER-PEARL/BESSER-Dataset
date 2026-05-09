





import java.util.List;
import java.util.ArrayList;

public class library_Book  {

    private String title;
    private String category;
    private int pages;





    private library_Writer library_writer;




    private library_Writer library_writer;




    private List<library_Writer> library_writers;




    private library_Library library_library;




    private library_Library library_library;




    private library_Writer library_writer;


    public library_Book(
        String title,        String category,        int pages    ) {
        this.title = title;
        this.category = category;
        this.pages = pages;
        this.library_writers = new ArrayList<>();
    }

    public library_Book(
        String title,        String category,        int pages        ArrayList<library_Writer> library_writers    ) {
        this.title = title;
        this.category = category;
        this.pages = pages;
        this.library_writers = library_writers;
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
    public int getPages() {
        return pages;
    }

    public void setPages(int pages) {
        this.pages = pages;
    }

    public library_Writer getLibrary_writer() {
        return library_writer;
    }

    public void setLibrary_writer(library_Writer library_writer) {
        this.library_writer = library_writer;
    }
    public library_Writer getLibrary_writer() {
        return library_writer;
    }

    public void setLibrary_writer(library_Writer library_writer) {
        this.library_writer = library_writer;
    }
    public List<library_Writer> getLibrary_writers() {
        return library_writers;
    }

    public void addLibrary_writer(Library_writer library_writer) {
        this.library_writers.add(library_writer);
    }
    public library_Library getLibrary_library() {
        return library_library;
    }

    public void setLibrary_library(library_Library library_library) {
        this.library_library = library_library;
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

}