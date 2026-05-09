





import java.util.List;
import java.util.ArrayList;

public class library_Book  {

    private String name;
    private String rating;





    private library_Author library_author;


    public library_Book(
        String name,        String rating    ) {
        this.name = name;
        this.rating = rating;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getRating() {
        return rating;
    }

    public void setRating(String rating) {
        this.rating = rating;
    }

    public library_Author getLibrary_author() {
        return library_author;
    }

    public void setLibrary_author(library_Author library_author) {
        this.library_author = library_author;
    }

}