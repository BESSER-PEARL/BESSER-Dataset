





import java.util.List;
import java.util.ArrayList;

public class libraryModel_Writer  {

    private String name;





    private libraryModel_Library librarymodel_library;


    public libraryModel_Writer(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public libraryModel_Library getLibrarymodel_library() {
        return librarymodel_library;
    }

    public void setLibrarymodel_library(libraryModel_Library librarymodel_library) {
        this.librarymodel_library = librarymodel_library;
    }

}