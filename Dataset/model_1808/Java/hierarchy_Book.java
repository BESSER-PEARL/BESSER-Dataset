





import java.util.List;
import java.util.ArrayList;

public class hierarchy_Book  {

    private String genre;
    private String Name;





    private hierarchy_NonFiction hierarchy_nonfiction;




    private hierarchy_Fiction hierarchy_fiction;


    public hierarchy_Book(
        String genre,        String Name    ) {
        this.genre = genre;
        this.Name = Name;
    }


    public String getGenre() {
        return genre;
    }

    public void setGenre(String genre) {
        this.genre = genre;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public hierarchy_NonFiction getHierarchy_nonfiction() {
        return hierarchy_nonfiction;
    }

    public void setHierarchy_nonfiction(hierarchy_NonFiction hierarchy_nonfiction) {
        this.hierarchy_nonfiction = hierarchy_nonfiction;
    }
    public hierarchy_Fiction getHierarchy_fiction() {
        return hierarchy_fiction;
    }

    public void setHierarchy_fiction(hierarchy_Fiction hierarchy_fiction) {
        this.hierarchy_fiction = hierarchy_fiction;
    }

}