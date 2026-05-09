





import java.util.List;
import java.util.ArrayList;

public class library_Book  {

    private String title;





    private library_Author library_author;




    private library_Shelf library_shelf;




    private library_Author library_author;


    public library_Book(
        String title    ) {
        this.title = title;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public library_Author getLibrary_author() {
        return library_author;
    }

    public void setLibrary_author(library_Author library_author) {
        this.library_author = library_author;
    }
    public library_Shelf getLibrary_shelf() {
        return library_shelf;
    }

    public void setLibrary_shelf(library_Shelf library_shelf) {
        this.library_shelf = library_shelf;
    }
    public library_Author getLibrary_author() {
        return library_author;
    }

    public void setLibrary_author(library_Author library_author) {
        this.library_author = library_author;
    }

}