





import java.util.List;
import java.util.ArrayList;

public class standard_InfectorInoculatorCollection extends NodeDecorator, Modifiable {

    private String importFolder;



    public standard_InfectorInoculatorCollection(
        String importFolder    ) {
        super(
        );
        this.importFolder = importFolder;
    }


    public String getImportfolder() {
        return importFolder;
    }

    public void setImportfolder(String importFolder) {
        this.importFolder = importFolder;
    }


}