





import java.util.List;
import java.util.ArrayList;

public class library_Book  {

    private int pages;
    private String title;





    private List<library_Author> library_authors;


    public library_Book(
        int pages,        String title    ) {
        this.pages = pages;
        this.title = title;
        this.library_authors = new ArrayList<>();
    }

    public library_Book(
        int pages,        String title        ArrayList<library_Author> library_authors    ) {
        this.pages = pages;
        this.title = title;
        this.library_authors = library_authors;
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

    public List<library_Author> getLibrary_authors() {
        return library_authors;
    }

    public void addLibrary_author(Library_author library_author) {
        this.library_authors.add(library_author);
    }

}