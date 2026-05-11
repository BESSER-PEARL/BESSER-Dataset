





import java.util.List;
import java.util.ArrayList;

public class cal_Import  {

    private String importedNamespace;





    private cal_AstEntity cal_astentity;


    public cal_Import(
        String importedNamespace    ) {
        this.importedNamespace = importedNamespace;
    }


    public String getImportednamespace() {
        return importedNamespace;
    }

    public void setImportednamespace(String importedNamespace) {
        this.importedNamespace = importedNamespace;
    }

    public cal_AstEntity getCal_astentity() {
        return cal_astentity;
    }

    public void setCal_astentity(cal_AstEntity cal_astentity) {
        this.cal_astentity = cal_astentity;
    }

}