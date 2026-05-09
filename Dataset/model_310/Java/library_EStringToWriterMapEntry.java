





import java.util.List;
import java.util.ArrayList;

public class library_EStringToWriterMapEntry  {

    private String key;





    private library_Library library_library;




    private library_Writer library_writer;


    public library_EStringToWriterMapEntry(
        String key    ) {
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public library_Library getLibrary_library() {
        return library_library;
    }

    public void setLibrary_library(library_Library library_library) {
        this.library_library = library_library;
    }
    public library_Writer getLibrary_writer() {
        return library_writer;
    }

    public void setLibrary_writer(library_Writer library_writer) {
        this.library_writer = library_writer;
    }

}