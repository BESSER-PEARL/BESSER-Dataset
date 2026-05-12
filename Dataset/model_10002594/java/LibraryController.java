





import java.util.List;
import java.util.ArrayList;

public class LibraryController  {

    private String libraryDataAcces;



    public LibraryController(
        String libraryDataAcces    ) {
        this.libraryDataAcces = libraryDataAcces;
    }


    public String getLibrarydataacces() {
        return libraryDataAcces;
    }

    public void setLibrarydataacces(String libraryDataAcces) {
        this.libraryDataAcces = libraryDataAcces;
    }


}