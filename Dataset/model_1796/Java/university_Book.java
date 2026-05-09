





import java.util.List;
import java.util.ArrayList;

public class university_Book extends NamedElement {

    private String ISBN;
    private String authorNames;





    private university_Library university_library;


    public university_Book(
        String ISBN,        String authorNames    ) {
        super(
        );
        this.ISBN = ISBN;
        this.authorNames = authorNames;
    }


    public String getIsbn() {
        return ISBN;
    }

    public void setIsbn(String ISBN) {
        this.ISBN = ISBN;
    }
    public String getAuthornames() {
        return authorNames;
    }

    public void setAuthornames(String authorNames) {
        this.authorNames = authorNames;
    }

    public university_Library getUniversity_library() {
        return university_library;
    }

    public void setUniversity_library(university_Library university_library) {
        this.university_library = university_library;
    }

}