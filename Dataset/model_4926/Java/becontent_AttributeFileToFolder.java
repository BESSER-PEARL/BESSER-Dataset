





import java.util.List;
import java.util.ArrayList;

public class becontent_AttributeFileToFolder extends TypedAttribute {






    private List<becontent_FileToFolderExtension> becontent_filetofolderextensions;


    public becontent_AttributeFileToFolder(
    ) {
        super(
        );
        this.becontent_filetofolderextensions = new ArrayList<>();
    }

    public becontent_AttributeFileToFolder(
        ArrayList<becontent_FileToFolderExtension> becontent_filetofolderextensions    ) {
        this.becontent_filetofolderextensions = becontent_filetofolderextensions;
    }


    public List<becontent_FileToFolderExtension> getBecontent_filetofolderextensions() {
        return becontent_filetofolderextensions;
    }

    public void addBecontent_filetofolderextension(Becontent_filetofolderextension becontent_filetofolderextension) {
        this.becontent_filetofolderextensions.add(becontent_filetofolderextension);
    }

}