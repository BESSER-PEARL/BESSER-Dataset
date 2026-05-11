





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Process extends Standard, Element {

    private String processCritiality;
    private String processVolumetrics;
    private boolean isAutomated;





    private contentfwk_Process contentfwk_process;




    private contentfwk_Process contentfwk_process;




    private List<contentfwk_Process> contentfwk_processs;




    private List<contentfwk_Process> contentfwk_processs;


    public contentfwk_Process(
        String processCritiality,        String processVolumetrics,        boolean isAutomated    ) {
        super(
        );
        this.processCritiality = processCritiality;
        this.processVolumetrics = processVolumetrics;
        this.isAutomated = isAutomated;
        this.contentfwk_processs = new ArrayList<>();
        this.contentfwk_processs = new ArrayList<>();
    }

    public contentfwk_Process(
        String processCritiality,        String processVolumetrics,        boolean isAutomated        ArrayList<contentfwk_Process> contentfwk_processs,        ArrayList<contentfwk_Process> contentfwk_processs    ) {
        this.processCritiality = processCritiality;
        this.processVolumetrics = processVolumetrics;
        this.isAutomated = isAutomated;
        this.contentfwk_processs = contentfwk_processs;
        this.contentfwk_processs = contentfwk_processs;
    }

    public String getProcesscritiality() {
        return processCritiality;
    }

    public void setProcesscritiality(String processCritiality) {
        this.processCritiality = processCritiality;
    }
    public String getProcessvolumetrics() {
        return processVolumetrics;
    }

    public void setProcessvolumetrics(String processVolumetrics) {
        this.processVolumetrics = processVolumetrics;
    }
    public boolean getIsautomated() {
        return isAutomated;
    }

    public void setIsautomated(boolean isAutomated) {
        this.isAutomated = isAutomated;
    }

    public contentfwk_Process getContentfwk_process() {
        return contentfwk_process;
    }

    public void setContentfwk_process(contentfwk_Process contentfwk_process) {
        this.contentfwk_process = contentfwk_process;
    }
    public contentfwk_Process getContentfwk_process() {
        return contentfwk_process;
    }

    public void setContentfwk_process(contentfwk_Process contentfwk_process) {
        this.contentfwk_process = contentfwk_process;
    }
    public List<contentfwk_Process> getContentfwk_processs() {
        return contentfwk_processs;
    }

    public void addContentfwk_process(Contentfwk_process contentfwk_process) {
        this.contentfwk_processs.add(contentfwk_process);
    }
    public List<contentfwk_Process> getContentfwk_processs() {
        return contentfwk_processs;
    }

    public void addContentfwk_process(Contentfwk_process contentfwk_process) {
        this.contentfwk_processs.add(contentfwk_process);
    }

}