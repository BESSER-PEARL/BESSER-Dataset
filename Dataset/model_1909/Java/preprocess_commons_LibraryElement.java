





import java.util.List;
import java.util.ArrayList;

public class preprocess_commons_LibraryElement extends Element {

    private String libraryName;



    public preprocess_commons_LibraryElement(
        String libraryName    ) {
        super(
        );
        this.libraryName = libraryName;
    }


    public String getLibraryname() {
        return libraryName;
    }

    public void setLibraryname(String libraryName) {
        this.libraryName = libraryName;
    }


}