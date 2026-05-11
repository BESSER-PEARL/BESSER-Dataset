





import java.util.List;
import java.util.ArrayList;

public class model_AbstractMTypeWithNameDeclaration  {

    private String name;





    private model_AbstractMTypeReference model_abstractmtypereference;


    public model_AbstractMTypeWithNameDeclaration(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public model_AbstractMTypeReference getModel_abstractmtypereference() {
        return model_abstractmtypereference;
    }

    public void setModel_abstractmtypereference(model_AbstractMTypeReference model_abstractmtypereference) {
        this.model_abstractmtypereference = model_abstractmtypereference;
    }

}