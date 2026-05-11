





import java.util.List;
import java.util.ArrayList;

public class mid_editor_Editor extends ExtendibleElement {

    private String modelUri;
    private String id;
    private String wizardId;
    private String fileExtensions;
    private String wizardDialogClass;



    public mid_editor_Editor(
        String modelUri,        String id,        String wizardId,        String fileExtensions,        String wizardDialogClass    ) {
        super(
        );
        this.modelUri = modelUri;
        this.id = id;
        this.wizardId = wizardId;
        this.fileExtensions = fileExtensions;
        this.wizardDialogClass = wizardDialogClass;
    }


    public String getModeluri() {
        return modelUri;
    }

    public void setModeluri(String modelUri) {
        this.modelUri = modelUri;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getWizardid() {
        return wizardId;
    }

    public void setWizardid(String wizardId) {
        this.wizardId = wizardId;
    }
    public String getFileextensions() {
        return fileExtensions;
    }

    public void setFileextensions(String fileExtensions) {
        this.fileExtensions = fileExtensions;
    }
    public String getWizarddialogclass() {
        return wizardDialogClass;
    }

    public void setWizarddialogclass(String wizardDialogClass) {
        this.wizardDialogClass = wizardDialogClass;
    }


}