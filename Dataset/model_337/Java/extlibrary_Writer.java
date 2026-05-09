





import java.util.List;
import java.util.ArrayList;

public class extlibrary_Writer extends Person {

    private String name;





    private extlibrary_Library extlibrary_library;


    public extlibrary_Writer(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public extlibrary_Library getExtlibrary_library() {
        return extlibrary_library;
    }

    public void setExtlibrary_library(extlibrary_Library extlibrary_library) {
        this.extlibrary_library = extlibrary_library;
    }

}