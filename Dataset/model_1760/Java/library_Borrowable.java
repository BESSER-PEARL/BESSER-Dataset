





import java.util.List;
import java.util.ArrayList;

public class library_Borrowable  {

    private int copiesAvailable;
    private String title;





    private library_CityLibrary library_citylibrary;




    private library_CityLibrary library_citylibrary;


    public library_Borrowable(
        int copiesAvailable,        String title    ) {
        this.copiesAvailable = copiesAvailable;
        this.title = title;
    }


    public int getCopiesavailable() {
        return copiesAvailable;
    }

    public void setCopiesavailable(int copiesAvailable) {
        this.copiesAvailable = copiesAvailable;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public library_CityLibrary getLibrary_citylibrary() {
        return library_citylibrary;
    }

    public void setLibrary_citylibrary(library_CityLibrary library_citylibrary) {
        this.library_citylibrary = library_citylibrary;
    }
    public library_CityLibrary getLibrary_citylibrary() {
        return library_citylibrary;
    }

    public void setLibrary_citylibrary(library_CityLibrary library_citylibrary) {
        this.library_citylibrary = library_citylibrary;
    }

}