





import java.util.List;
import java.util.ArrayList;

public class uma_ProcessComponent extends ProcessPackage {

    private String authors;
    private String copyright;
    private String version;
    private String changeDescription;
    private String changeDate;





    private uma_Process uma_process;




    private uma_ProcessComponentInterface uma_processcomponentinterface;


    public uma_ProcessComponent(
        String authors,        String copyright,        String version,        String changeDescription,        String changeDate    ) {
        super(
        );
        this.authors = authors;
        this.copyright = copyright;
        this.version = version;
        this.changeDescription = changeDescription;
        this.changeDate = changeDate;
    }


    public String getAuthors() {
        return authors;
    }

    public void setAuthors(String authors) {
        this.authors = authors;
    }
    public String getCopyright() {
        return copyright;
    }

    public void setCopyright(String copyright) {
        this.copyright = copyright;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getChangedescription() {
        return changeDescription;
    }

    public void setChangedescription(String changeDescription) {
        this.changeDescription = changeDescription;
    }
    public String getChangedate() {
        return changeDate;
    }

    public void setChangedate(String changeDate) {
        this.changeDate = changeDate;
    }

    public uma_Process getUma_process() {
        return uma_process;
    }

    public void setUma_process(uma_Process uma_process) {
        this.uma_process = uma_process;
    }
    public uma_ProcessComponentInterface getUma_processcomponentinterface() {
        return uma_processcomponentinterface;
    }

    public void setUma_processcomponentinterface(uma_ProcessComponentInterface uma_processcomponentinterface) {
        this.uma_processcomponentinterface = uma_processcomponentinterface;
    }

}