





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Process extends Element, Standard {

    private String processVolumetrics;
    private boolean isAutomated;
    private String processCritiality;





    private contentfwk_Process contentfwk_process;




    private contentfwk_Function contentfwk_function;




    private List<contentfwk_Function> contentfwk_functions;




    private List<contentfwk_Process> contentfwk_processs;




    private contentfwk_Function contentfwk_function;




    private List<contentfwk_Function> contentfwk_functions;




    private contentfwk_Process contentfwk_process;


    public contentfwk_Process(
        String processVolumetrics,        boolean isAutomated,        String processCritiality    ) {
        super(
        );
        this.processVolumetrics = processVolumetrics;
        this.isAutomated = isAutomated;
        this.processCritiality = processCritiality;
        this.contentfwk_functions = new ArrayList<>();
        this.contentfwk_processs = new ArrayList<>();
        this.contentfwk_functions = new ArrayList<>();
    }

    public contentfwk_Process(
        String processVolumetrics,        boolean isAutomated,        String processCritiality        ArrayList<contentfwk_Function> contentfwk_functions,        ArrayList<contentfwk_Process> contentfwk_processs,        ArrayList<contentfwk_Function> contentfwk_functions    ) {
        this.processVolumetrics = processVolumetrics;
        this.isAutomated = isAutomated;
        this.processCritiality = processCritiality;
        this.contentfwk_functions = contentfwk_functions;
        this.contentfwk_processs = contentfwk_processs;
        this.contentfwk_functions = contentfwk_functions;
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
    public String getProcesscritiality() {
        return processCritiality;
    }

    public void setProcesscritiality(String processCritiality) {
        this.processCritiality = processCritiality;
    }

    public contentfwk_Process getContentfwk_process() {
        return contentfwk_process;
    }

    public void setContentfwk_process(contentfwk_Process contentfwk_process) {
        this.contentfwk_process = contentfwk_process;
    }
    public contentfwk_Function getContentfwk_function() {
        return contentfwk_function;
    }

    public void setContentfwk_function(contentfwk_Function contentfwk_function) {
        this.contentfwk_function = contentfwk_function;
    }
    public List<contentfwk_Function> getContentfwk_functions() {
        return contentfwk_functions;
    }

    public void addContentfwk_function(Contentfwk_function contentfwk_function) {
        this.contentfwk_functions.add(contentfwk_function);
    }
    public List<contentfwk_Process> getContentfwk_processs() {
        return contentfwk_processs;
    }

    public void addContentfwk_process(Contentfwk_process contentfwk_process) {
        this.contentfwk_processs.add(contentfwk_process);
    }
    public contentfwk_Function getContentfwk_function() {
        return contentfwk_function;
    }

    public void setContentfwk_function(contentfwk_Function contentfwk_function) {
        this.contentfwk_function = contentfwk_function;
    }
    public List<contentfwk_Function> getContentfwk_functions() {
        return contentfwk_functions;
    }

    public void addContentfwk_function(Contentfwk_function contentfwk_function) {
        this.contentfwk_functions.add(contentfwk_function);
    }
    public contentfwk_Process getContentfwk_process() {
        return contentfwk_process;
    }

    public void setContentfwk_process(contentfwk_Process contentfwk_process) {
        this.contentfwk_process = contentfwk_process;
    }

}