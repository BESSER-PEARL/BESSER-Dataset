





import java.util.List;
import java.util.ArrayList;

public class form_FileWidget extends Duplicable, SingleValuatedFormField {

    private String downloadType;
    private String initialResourcePath;
    private boolean updateDocument;
    private boolean downloadOnly;
    private boolean usePreview;
    private String outputDocumentName;
    private String inputType;
    private String intialResourceList;





    private form_Expression form_expression;


    public form_FileWidget(
        String downloadType,        String initialResourcePath,        boolean updateDocument,        boolean downloadOnly,        boolean usePreview,        String outputDocumentName,        String inputType,        String intialResourceList    ) {
        super(
        );
        this.downloadType = downloadType;
        this.initialResourcePath = initialResourcePath;
        this.updateDocument = updateDocument;
        this.downloadOnly = downloadOnly;
        this.usePreview = usePreview;
        this.outputDocumentName = outputDocumentName;
        this.inputType = inputType;
        this.intialResourceList = intialResourceList;
    }


    public String getDownloadtype() {
        return downloadType;
    }

    public void setDownloadtype(String downloadType) {
        this.downloadType = downloadType;
    }
    public String getInitialresourcepath() {
        return initialResourcePath;
    }

    public void setInitialresourcepath(String initialResourcePath) {
        this.initialResourcePath = initialResourcePath;
    }
    public boolean getUpdatedocument() {
        return updateDocument;
    }

    public void setUpdatedocument(boolean updateDocument) {
        this.updateDocument = updateDocument;
    }
    public boolean getDownloadonly() {
        return downloadOnly;
    }

    public void setDownloadonly(boolean downloadOnly) {
        this.downloadOnly = downloadOnly;
    }
    public boolean getUsepreview() {
        return usePreview;
    }

    public void setUsepreview(boolean usePreview) {
        this.usePreview = usePreview;
    }
    public String getOutputdocumentname() {
        return outputDocumentName;
    }

    public void setOutputdocumentname(String outputDocumentName) {
        this.outputDocumentName = outputDocumentName;
    }
    public String getInputtype() {
        return inputType;
    }

    public void setInputtype(String inputType) {
        this.inputType = inputType;
    }
    public String getIntialresourcelist() {
        return intialResourceList;
    }

    public void setIntialresourcelist(String intialResourceList) {
        this.intialResourceList = intialResourceList;
    }

    public form_Expression getForm_expression() {
        return form_expression;
    }

    public void setForm_expression(form_Expression form_expression) {
        this.form_expression = form_expression;
    }

}