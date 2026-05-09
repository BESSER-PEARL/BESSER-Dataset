





import java.util.List;
import java.util.ArrayList;

public class mytry_Book  {

    private String title;





    private mytry_Library mytry_library;


    public mytry_Book(
        String title    ) {
        this.title = title;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public mytry_Library getMytry_library() {
        return mytry_library;
    }

    public void setMytry_library(mytry_Library mytry_library) {
        this.mytry_library = mytry_library;
    }

}