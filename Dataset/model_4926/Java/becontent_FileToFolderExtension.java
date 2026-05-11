





import java.util.List;
import java.util.ArrayList;

public class becontent_FileToFolderExtension extends BeContentElement {

    private String _id_model;
    private String extensionValue;
    private String extensionKey;



    public becontent_FileToFolderExtension(
        String _id_model,        String extensionValue,        String extensionKey    ) {
        super(
        );
        this._id_model = _id_model;
        this.extensionValue = extensionValue;
        this.extensionKey = extensionKey;
    }


    public String get_id_model() {
        return _id_model;
    }

    public void set_id_model(String _id_model) {
        this._id_model = _id_model;
    }
    public String getExtensionvalue() {
        return extensionValue;
    }

    public void setExtensionvalue(String extensionValue) {
        this.extensionValue = extensionValue;
    }
    public String getExtensionkey() {
        return extensionKey;
    }

    public void setExtensionkey(String extensionKey) {
        this.extensionKey = extensionKey;
    }


}