





import java.util.List;
import java.util.ArrayList;

public class stext_Import  {

    private String importedNamespace;





    private stext_ImportScope stext_importscope;


    public stext_Import(
        String importedNamespace    ) {
        this.importedNamespace = importedNamespace;
    }


    public String getImportednamespace() {
        return importedNamespace;
    }

    public void setImportednamespace(String importedNamespace) {
        this.importedNamespace = importedNamespace;
    }

    public stext_ImportScope getStext_importscope() {
        return stext_importscope;
    }

    public void setStext_importscope(stext_ImportScope stext_importscope) {
        this.stext_importscope = stext_importscope;
    }

}