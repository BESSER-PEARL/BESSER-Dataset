





import java.util.List;
import java.util.ArrayList;

public class model_Folder extends FolderContainer, Documentable, ArchimateModelObject, Properties {

    private String type;



    public model_Folder(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}