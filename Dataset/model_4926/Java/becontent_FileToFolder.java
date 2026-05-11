





import java.util.List;
import java.util.ArrayList;

public class becontent_FileToFolder extends NotStructuredElement {

    private String name;
    private String label;
    private String extension;
    private String extensionMessage;
    private boolean isMandatory;



    public becontent_FileToFolder(
        String name,        String label,        String extension,        String extensionMessage,        boolean isMandatory    ) {
        super(
        );
        this.name = name;
        this.label = label;
        this.extension = extension;
        this.extensionMessage = extensionMessage;
        this.isMandatory = isMandatory;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getExtension() {
        return extension;
    }

    public void setExtension(String extension) {
        this.extension = extension;
    }
    public String getExtensionmessage() {
        return extensionMessage;
    }

    public void setExtensionmessage(String extensionMessage) {
        this.extensionMessage = extensionMessage;
    }
    public boolean getIsmandatory() {
        return isMandatory;
    }

    public void setIsmandatory(boolean isMandatory) {
        this.isMandatory = isMandatory;
    }


}