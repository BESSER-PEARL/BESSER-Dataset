





import java.util.List;
import java.util.ArrayList;

public class becontent_File extends NotStructuredElement {

    private String label;
    private String extension;
    private boolean isMandatory;
    private String extensionMessage;
    private String name;



    public becontent_File(
        String label,        String extension,        boolean isMandatory,        String extensionMessage,        String name    ) {
        super(
        );
        this.label = label;
        this.extension = extension;
        this.isMandatory = isMandatory;
        this.extensionMessage = extensionMessage;
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
    public boolean getIsmandatory() {
        return isMandatory;
    }

    public void setIsmandatory(boolean isMandatory) {
        this.isMandatory = isMandatory;
    }
    public String getExtensionmessage() {
        return extensionMessage;
    }

    public void setExtensionmessage(String extensionMessage) {
        this.extensionMessage = extensionMessage;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}