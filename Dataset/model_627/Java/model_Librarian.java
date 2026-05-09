





import java.util.List;
import java.util.ArrayList;

public class model_Librarian  {

    private String name;





    private model_Library model_library;


    public model_Librarian(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public model_Library getModel_library() {
        return model_library;
    }

    public void setModel_library(model_Library model_library) {
        this.model_library = model_library;
    }

}