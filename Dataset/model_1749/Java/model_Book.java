





import java.util.List;
import java.util.ArrayList;

public class model_Book  {

    private String title;





    private model_Library model_library;


    public model_Book(
        String title    ) {
        this.title = title;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public model_Library getModel_library() {
        return model_library;
    }

    public void setModel_library(model_Library model_library) {
        this.model_library = model_library;
    }

}