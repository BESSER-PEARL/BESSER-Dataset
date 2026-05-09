





import java.util.List;
import java.util.ArrayList;

public class imported_model_Book  {

    private int pages;





    private imported_model_Library imported_model_library;


    public imported_model_Book(
        int pages    ) {
        this.pages = pages;
    }


    public int getPages() {
        return pages;
    }

    public void setPages(int pages) {
        this.pages = pages;
    }

    public imported_model_Library getImported_model_library() {
        return imported_model_library;
    }

    public void setImported_model_library(imported_model_Library imported_model_library) {
        this.imported_model_library = imported_model_library;
    }

}