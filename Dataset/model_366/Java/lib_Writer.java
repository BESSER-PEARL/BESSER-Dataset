





import java.util.List;
import java.util.ArrayList;

public class lib_Writer  {

    private String name;





    private lib_Library lib_library;


    public lib_Writer(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public lib_Library getLib_library() {
        return lib_library;
    }

    public void setLib_library(lib_Library lib_library) {
        this.lib_library = lib_library;
    }

}