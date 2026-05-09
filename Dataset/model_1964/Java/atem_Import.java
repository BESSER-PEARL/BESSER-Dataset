





import java.util.List;
import java.util.ArrayList;

public class atem_Import  {

    private String importedNamespace;





    private atem_AtemModel atem_atemmodel;


    public atem_Import(
        String importedNamespace    ) {
        this.importedNamespace = importedNamespace;
    }


    public String getImportednamespace() {
        return importedNamespace;
    }

    public void setImportednamespace(String importedNamespace) {
        this.importedNamespace = importedNamespace;
    }

    public atem_AtemModel getAtem_atemmodel() {
        return atem_atemmodel;
    }

    public void setAtem_atemmodel(atem_AtemModel atem_atemmodel) {
        this.atem_atemmodel = atem_atemmodel;
    }

}