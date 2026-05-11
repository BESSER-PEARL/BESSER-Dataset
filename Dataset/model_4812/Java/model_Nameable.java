





import java.util.List;
import java.util.ArrayList;

public class model_Nameable  {

    private String name;





    private model_Folder model_folder;


    public model_Nameable(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public model_Folder getModel_folder() {
        return model_folder;
    }

    public void setModel_folder(model_Folder model_folder) {
        this.model_folder = model_folder;
    }

}