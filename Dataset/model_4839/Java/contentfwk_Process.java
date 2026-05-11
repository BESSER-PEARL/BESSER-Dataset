





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Process extends Standard, Element {

    private boolean isAutomated;
    private String processCritiality;
    private String processVolumetrics;





    private contentfwk_Service contentfwk_service;




    private List<contentfwk_Function> contentfwk_functions;




    private contentfwk_Function contentfwk_function;




    private List<contentfwk_Function> contentfwk_functions;




    private contentfwk_Process contentfwk_process;




    private contentfwk_Process contentfwk_process;




    private List<contentfwk_Service> contentfwk_services;




    private List<contentfwk_Process> contentfwk_processs;




    private contentfwk_Function contentfwk_function;




    private contentfwk_Service contentfwk_service;




    private List<contentfwk_Service> contentfwk_services;


    public contentfwk_Process(
        boolean isAutomated,        String processCritiality,        String processVolumetrics    ) {
        super(
        );
        this.isAutomated = isAutomated;
        this.processCritiality = processCritiality;
        this.processVolumetrics = processVolumetrics;
        this.contentfwk_functions = new ArrayList<>();
        this.contentfwk_functions = new ArrayList<>();
        this.contentfwk_services = new ArrayList<>();
        this.contentfwk_processs = new ArrayList<>();
        this.contentfwk_services = new ArrayList<>();
    }

    public contentfwk_Process(
        boolean isAutomated,        String processCritiality,        String processVolumetrics        ArrayList<contentfwk_Function> contentfwk_functions,        ArrayList<contentfwk_Function> contentfwk_functions,        ArrayList<contentfwk_Service> contentfwk_services,        ArrayList<contentfwk_Process> contentfwk_processs,        ArrayList<contentfwk_Service> contentfwk_services    ) {
        this.isAutomated = isAutomated;
        this.processCritiality = processCritiality;
        this.processVolumetrics = processVolumetrics;
        this.contentfwk_functions = contentfwk_functions;
        this.contentfwk_functions = contentfwk_functions;
        this.contentfwk_services = contentfwk_services;
        this.contentfwk_processs = contentfwk_processs;
        this.contentfwk_services = contentfwk_services;
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
    public String getProcessvolumetrics() {
        return processVolumetrics;
    }

    public void setProcessvolumetrics(String processVolumetrics) {
        this.processVolumetrics = processVolumetrics;
    }

    public contentfwk_Service getContentfwk_service() {
        return contentfwk_service;
    }

    public void setContentfwk_service(contentfwk_Service contentfwk_service) {
        this.contentfwk_service = contentfwk_service;
    }
    public List<contentfwk_Function> getContentfwk_functions() {
        return contentfwk_functions;
    }

    public void addContentfwk_function(Contentfwk_function contentfwk_function) {
        this.contentfwk_functions.add(contentfwk_function);
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
    public contentfwk_Process getContentfwk_process() {
        return contentfwk_process;
    }

    public void setContentfwk_process(contentfwk_Process contentfwk_process) {
        this.contentfwk_process = contentfwk_process;
    }
    public List<contentfwk_Service> getContentfwk_services() {
        return contentfwk_services;
    }

    public void addContentfwk_service(Contentfwk_service contentfwk_service) {
        this.contentfwk_services.add(contentfwk_service);
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
    public contentfwk_Service getContentfwk_service() {
        return contentfwk_service;
    }

    public void setContentfwk_service(contentfwk_Service contentfwk_service) {
        this.contentfwk_service = contentfwk_service;
    }
    public List<contentfwk_Service> getContentfwk_services() {
        return contentfwk_services;
    }

    public void addContentfwk_service(Contentfwk_service contentfwk_service) {
        this.contentfwk_services.add(contentfwk_service);
    }

}