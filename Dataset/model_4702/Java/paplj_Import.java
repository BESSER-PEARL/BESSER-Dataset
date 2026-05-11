





import java.util.List;
import java.util.ArrayList;

public class paplj_Import  {

    private String importedNamespace;





    private paplj_Program paplj_program;


    public paplj_Import(
        String importedNamespace    ) {
        this.importedNamespace = importedNamespace;
    }


    public String getImportednamespace() {
        return importedNamespace;
    }

    public void setImportednamespace(String importedNamespace) {
        this.importedNamespace = importedNamespace;
    }

    public paplj_Program getPaplj_program() {
        return paplj_program;
    }

    public void setPaplj_program(paplj_Program paplj_program) {
        this.paplj_program = paplj_program;
    }

}