





import java.util.List;
import java.util.ArrayList;

public class model_base_Folder extends ISpecmateModelObject {

    private boolean library;



    public model_base_Folder(
        boolean library    ) {
        super(
        );
        this.library = library;
    }


    public boolean getLibrary() {
        return library;
    }

    public void setLibrary(boolean library) {
        this.library = library;
    }


}