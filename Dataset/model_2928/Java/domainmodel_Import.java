





import java.util.List;
import java.util.ArrayList;

public class domainmodel_Import extends AbstractElement {

    private String importedNameSpace;



    public domainmodel_Import(
        String importedNameSpace    ) {
        super(
        );
        this.importedNameSpace = importedNameSpace;
    }


    public String getImportednamespace() {
        return importedNameSpace;
    }

    public void setImportednamespace(String importedNameSpace) {
        this.importedNameSpace = importedNameSpace;
    }


}