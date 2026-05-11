





import java.util.List;
import java.util.ArrayList;

public class model_ZentaModel extends Folder, ZentaModelElement, Properties, FolderContainer, Nameable, Identifier, Documentable {

    private String version;
    private String file;





    private model_ZentaModelElement model_zentamodelelement;


    public model_ZentaModel(
        String version,        String file    ) {
        super(
        );
        this.version = version;
        this.file = file;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }

    public model_ZentaModelElement getModel_zentamodelelement() {
        return model_zentamodelelement;
    }

    public void setModel_zentamodelelement(model_ZentaModelElement model_zentamodelelement) {
        this.model_zentamodelelement = model_zentamodelelement;
    }

}