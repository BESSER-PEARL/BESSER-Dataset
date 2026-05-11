





import java.util.List;
import java.util.ArrayList;

public class myTuto_Import extends AbstractElement {

    private String importedNameSpace;



    public myTuto_Import(
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