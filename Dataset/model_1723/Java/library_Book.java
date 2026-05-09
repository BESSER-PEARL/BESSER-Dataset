





import java.util.List;
import java.util.ArrayList;

public class library_Book  {

    private String Name;
    private String genre;



    public library_Book(
        String Name,        String genre    ) {
        this.Name = Name;
        this.genre = genre;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getGenre() {
        return genre;
    }

    public void setGenre(String genre) {
        this.genre = genre;
    }


}