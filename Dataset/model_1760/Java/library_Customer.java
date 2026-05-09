





import java.util.List;
import java.util.ArrayList;

public class library_Customer  {

    private String name;





    private library_CityLibrary library_citylibrary;




    private List<library_Borrowable> library_borrowables;


    public library_Customer(
        String name    ) {
        this.name = name;
        this.library_borrowables = new ArrayList<>();
    }

    public library_Customer(
        String name        ArrayList<library_Borrowable> library_borrowables    ) {
        this.name = name;
        this.library_borrowables = library_borrowables;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public library_CityLibrary getLibrary_citylibrary() {
        return library_citylibrary;
    }

    public void setLibrary_citylibrary(library_CityLibrary library_citylibrary) {
        this.library_citylibrary = library_citylibrary;
    }
    public List<library_Borrowable> getLibrary_borrowables() {
        return library_borrowables;
    }

    public void addLibrary_borrowable(Library_borrowable library_borrowable) {
        this.library_borrowables.add(library_borrowable);
    }

}