





import java.util.List;
import java.util.ArrayList;

public class mid_editor_Editor extends ExtendibleElement {

    private String wizardId;
    private String wizardDialogClass;
    private String fileExtensions;
    private String id;
    private String modelUri;



    public mid_editor_Editor(
        String wizardId,        String wizardDialogClass,        String fileExtensions,        String id,        String modelUri    ) {
        super(
        );
        this.wizardId = wizardId;
        this.wizardDialogClass = wizardDialogClass;
        this.fileExtensions = fileExtensions;
        this.id = id;
        this.modelUri = modelUri;
    }


    public String getWizardid() {
        return wizardId;
    }

    public void setWizardid(String wizardId) {
        this.wizardId = wizardId;
    }
    public String getWizarddialogclass() {
        return wizardDialogClass;
    }

    public void setWizarddialogclass(String wizardDialogClass) {
        this.wizardDialogClass = wizardDialogClass;
    }
    public String getFileextensions() {
        return fileExtensions;
    }

    public void setFileextensions(String fileExtensions) {
        this.fileExtensions = fileExtensions;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getModeluri() {
        return modelUri;
    }

    public void setModeluri(String modelUri) {
        this.modelUri = modelUri;
    }


}