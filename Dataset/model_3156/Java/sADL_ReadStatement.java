





import java.util.List;
import java.util.ArrayList;

public class sADL_ReadStatement extends SadlModelElement {

    private String filename;
    private String templateFilename;



    public sADL_ReadStatement(
        String filename,        String templateFilename    ) {
        super(
        );
        this.filename = filename;
        this.templateFilename = templateFilename;
    }


    public String getFilename() {
        return filename;
    }

    public void setFilename(String filename) {
        this.filename = filename;
    }
    public String getTemplatefilename() {
        return templateFilename;
    }

    public void setTemplatefilename(String templateFilename) {
        this.templateFilename = templateFilename;
    }


}