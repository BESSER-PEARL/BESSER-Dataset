





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Process extends Standard, Element {

    private String processVolumetrics;
    private boolean isAutomated;
    private String processCritiality;





    private List<contentfwk_Process> contentfwk_processs;




    private List<contentfwk_Actor> contentfwk_actors;




    private List<contentfwk_Function> contentfwk_functions;




    private contentfwk_Process contentfwk_process;




    private List<contentfwk_Function> contentfwk_functions;




    private contentfwk_Function contentfwk_function;




    private contentfwk_OrganizationUnit contentfwk_organizationunit;




    private contentfwk_Function contentfwk_function;




    private contentfwk_Actor contentfwk_actor;




    private List<contentfwk_OrganizationUnit> contentfwk_organizationunits;




    private contentfwk_Process contentfwk_process;


    public contentfwk_Process(
        String processVolumetrics,        boolean isAutomated,        String processCritiality    ) {
        super(
        );
        this.processVolumetrics = processVolumetrics;
        this.isAutomated = isAutomated;
        this.processCritiality = processCritiality;
        this.contentfwk_processs = new ArrayList<>();
        this.contentfwk_actors = new ArrayList<>();
        this.contentfwk_functions = new ArrayList<>();
        this.contentfwk_functions = new ArrayList<>();
        this.contentfwk_organizationunits = new ArrayList<>();
    }

    public contentfwk_Process(
        String processVolumetrics,        boolean isAutomated,        String processCritiality        ArrayList<contentfwk_Process> contentfwk_processs,        ArrayList<contentfwk_Actor> contentfwk_actors,        ArrayList<contentfwk_Function> contentfwk_functions,        ArrayList<contentfwk_Function> contentfwk_functions,        ArrayList<contentfwk_OrganizationUnit> contentfwk_organizationunits    ) {
        this.processVolumetrics = processVolumetrics;
        this.isAutomated = isAutomated;
        this.processCritiality = processCritiality;
        this.contentfwk_processs = contentfwk_processs;
        this.contentfwk_actors = contentfwk_actors;
        this.contentfwk_functions = contentfwk_functions;
        this.contentfwk_functions = contentfwk_functions;
        this.contentfwk_organizationunits = contentfwk_organizationunits;
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

    public List<contentfwk_Process> getContentfwk_processs() {
        return contentfwk_processs;
    }

    public void addContentfwk_process(Contentfwk_process contentfwk_process) {
        this.contentfwk_processs.add(contentfwk_process);
    }
    public List<contentfwk_Actor> getContentfwk_actors() {
        return contentfwk_actors;
    }

    public void addContentfwk_actor(Contentfwk_actor contentfwk_actor) {
        this.contentfwk_actors.add(contentfwk_actor);
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
    public contentfwk_OrganizationUnit getContentfwk_organizationunit() {
        return contentfwk_organizationunit;
    }

    public void setContentfwk_organizationunit(contentfwk_OrganizationUnit contentfwk_organizationunit) {
        this.contentfwk_organizationunit = contentfwk_organizationunit;
    }
    public contentfwk_Function getContentfwk_function() {
        return contentfwk_function;
    }

    public void setContentfwk_function(contentfwk_Function contentfwk_function) {
        this.contentfwk_function = contentfwk_function;
    }
    public contentfwk_Actor getContentfwk_actor() {
        return contentfwk_actor;
    }

    public void setContentfwk_actor(contentfwk_Actor contentfwk_actor) {
        this.contentfwk_actor = contentfwk_actor;
    }
    public List<contentfwk_OrganizationUnit> getContentfwk_organizationunits() {
        return contentfwk_organizationunits;
    }

    public void addContentfwk_organizationunit(Contentfwk_organizationunit contentfwk_organizationunit) {
        this.contentfwk_organizationunits.add(contentfwk_organizationunit);
    }
    public contentfwk_Process getContentfwk_process() {
        return contentfwk_process;
    }

    public void setContentfwk_process(contentfwk_Process contentfwk_process) {
        this.contentfwk_process = contentfwk_process;
    }

}