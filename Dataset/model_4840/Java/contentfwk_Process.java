





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Process extends Standard, Element {

    private String processCritiality;
    private boolean isAutomated;
    private String processVolumetrics;





    private contentfwk_Function contentfwk_function;




    private List<contentfwk_Function> contentfwk_functions;




    private contentfwk_BusinessArchitecture contentfwk_businessarchitecture;




    private List<contentfwk_Function> contentfwk_functions;




    private List<contentfwk_Process> contentfwk_processs;




    private List<contentfwk_Actor> contentfwk_actors;




    private contentfwk_OrganizationUnit contentfwk_organizationunit;




    private contentfwk_Process contentfwk_process;




    private List<contentfwk_OrganizationUnit> contentfwk_organizationunits;




    private contentfwk_Function contentfwk_function;




    private List<contentfwk_Process> contentfwk_processs;




    private contentfwk_Actor contentfwk_actor;


    public contentfwk_Process(
        String processCritiality,        boolean isAutomated,        String processVolumetrics    ) {
        super(
        );
        this.processCritiality = processCritiality;
        this.isAutomated = isAutomated;
        this.processVolumetrics = processVolumetrics;
        this.contentfwk_functions = new ArrayList<>();
        this.contentfwk_functions = new ArrayList<>();
        this.contentfwk_processs = new ArrayList<>();
        this.contentfwk_actors = new ArrayList<>();
        this.contentfwk_organizationunits = new ArrayList<>();
        this.contentfwk_processs = new ArrayList<>();
    }

    public contentfwk_Process(
        String processCritiality,        boolean isAutomated,        String processVolumetrics        ArrayList<contentfwk_Function> contentfwk_functions,        ArrayList<contentfwk_Function> contentfwk_functions,        ArrayList<contentfwk_Process> contentfwk_processs,        ArrayList<contentfwk_Actor> contentfwk_actors,        ArrayList<contentfwk_OrganizationUnit> contentfwk_organizationunits,        ArrayList<contentfwk_Process> contentfwk_processs    ) {
        this.processCritiality = processCritiality;
        this.isAutomated = isAutomated;
        this.processVolumetrics = processVolumetrics;
        this.contentfwk_functions = contentfwk_functions;
        this.contentfwk_functions = contentfwk_functions;
        this.contentfwk_processs = contentfwk_processs;
        this.contentfwk_actors = contentfwk_actors;
        this.contentfwk_organizationunits = contentfwk_organizationunits;
        this.contentfwk_processs = contentfwk_processs;
    }

    public String getProcesscritiality() {
        return processCritiality;
    }

    public void setProcesscritiality(String processCritiality) {
        this.processCritiality = processCritiality;
    }
    public boolean getIsautomated() {
        return isAutomated;
    }

    public void setIsautomated(boolean isAutomated) {
        this.isAutomated = isAutomated;
    }
    public String getProcessvolumetrics() {
        return processVolumetrics;
    }

    public void setProcessvolumetrics(String processVolumetrics) {
        this.processVolumetrics = processVolumetrics;
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
    public contentfwk_BusinessArchitecture getContentfwk_businessarchitecture() {
        return contentfwk_businessarchitecture;
    }

    public void setContentfwk_businessarchitecture(contentfwk_BusinessArchitecture contentfwk_businessarchitecture) {
        this.contentfwk_businessarchitecture = contentfwk_businessarchitecture;
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
    public List<contentfwk_Actor> getContentfwk_actors() {
        return contentfwk_actors;
    }

    public void addContentfwk_actor(Contentfwk_actor contentfwk_actor) {
        this.contentfwk_actors.add(contentfwk_actor);
    }
    public contentfwk_OrganizationUnit getContentfwk_organizationunit() {
        return contentfwk_organizationunit;
    }

    public void setContentfwk_organizationunit(contentfwk_OrganizationUnit contentfwk_organizationunit) {
        this.contentfwk_organizationunit = contentfwk_organizationunit;
    }
    public contentfwk_Process getContentfwk_process() {
        return contentfwk_process;
    }

    public void setContentfwk_process(contentfwk_Process contentfwk_process) {
        this.contentfwk_process = contentfwk_process;
    }
    public List<contentfwk_OrganizationUnit> getContentfwk_organizationunits() {
        return contentfwk_organizationunits;
    }

    public void addContentfwk_organizationunit(Contentfwk_organizationunit contentfwk_organizationunit) {
        this.contentfwk_organizationunits.add(contentfwk_organizationunit);
    }
    public contentfwk_Function getContentfwk_function() {
        return contentfwk_function;
    }

    public void setContentfwk_function(contentfwk_Function contentfwk_function) {
        this.contentfwk_function = contentfwk_function;
    }
    public List<contentfwk_Process> getContentfwk_processs() {
        return contentfwk_processs;
    }

    public void addContentfwk_process(Contentfwk_process contentfwk_process) {
        this.contentfwk_processs.add(contentfwk_process);
    }
    public contentfwk_Actor getContentfwk_actor() {
        return contentfwk_actor;
    }

    public void setContentfwk_actor(contentfwk_Actor contentfwk_actor) {
        this.contentfwk_actor = contentfwk_actor;
    }

}