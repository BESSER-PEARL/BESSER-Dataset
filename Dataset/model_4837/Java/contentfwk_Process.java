





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Process extends Standard, Element {

    private boolean isAutomated;
    private String processCritiality;
    private String processVolumetrics;





    private contentfwk_Process contentfwk_process;




    private List<contentfwk_Actor> contentfwk_actors;




    private contentfwk_OrganizationUnit contentfwk_organizationunit;




    private List<contentfwk_OrganizationUnit> contentfwk_organizationunits;




    private contentfwk_Function contentfwk_function;




    private contentfwk_Product contentfwk_product;




    private contentfwk_BusinessArchitecture contentfwk_businessarchitecture;




    private List<contentfwk_Process> contentfwk_processs;




    private List<contentfwk_Function> contentfwk_functions;




    private contentfwk_Process contentfwk_process;




    private contentfwk_Actor contentfwk_actor;




    private List<contentfwk_Product> contentfwk_products;




    private contentfwk_Function contentfwk_function;




    private List<contentfwk_Function> contentfwk_functions;


    public contentfwk_Process(
        boolean isAutomated,        String processCritiality,        String processVolumetrics    ) {
        super(
        );
        this.isAutomated = isAutomated;
        this.processCritiality = processCritiality;
        this.processVolumetrics = processVolumetrics;
        this.contentfwk_actors = new ArrayList<>();
        this.contentfwk_organizationunits = new ArrayList<>();
        this.contentfwk_processs = new ArrayList<>();
        this.contentfwk_functions = new ArrayList<>();
        this.contentfwk_products = new ArrayList<>();
        this.contentfwk_functions = new ArrayList<>();
    }

    public contentfwk_Process(
        boolean isAutomated,        String processCritiality,        String processVolumetrics        ArrayList<contentfwk_Actor> contentfwk_actors,        ArrayList<contentfwk_OrganizationUnit> contentfwk_organizationunits,        ArrayList<contentfwk_Process> contentfwk_processs,        ArrayList<contentfwk_Function> contentfwk_functions,        ArrayList<contentfwk_Product> contentfwk_products,        ArrayList<contentfwk_Function> contentfwk_functions    ) {
        this.isAutomated = isAutomated;
        this.processCritiality = processCritiality;
        this.processVolumetrics = processVolumetrics;
        this.contentfwk_actors = contentfwk_actors;
        this.contentfwk_organizationunits = contentfwk_organizationunits;
        this.contentfwk_processs = contentfwk_processs;
        this.contentfwk_functions = contentfwk_functions;
        this.contentfwk_products = contentfwk_products;
        this.contentfwk_functions = contentfwk_functions;
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

    public contentfwk_Process getContentfwk_process() {
        return contentfwk_process;
    }

    public void setContentfwk_process(contentfwk_Process contentfwk_process) {
        this.contentfwk_process = contentfwk_process;
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
    public contentfwk_Product getContentfwk_product() {
        return contentfwk_product;
    }

    public void setContentfwk_product(contentfwk_Product contentfwk_product) {
        this.contentfwk_product = contentfwk_product;
    }
    public contentfwk_BusinessArchitecture getContentfwk_businessarchitecture() {
        return contentfwk_businessarchitecture;
    }

    public void setContentfwk_businessarchitecture(contentfwk_BusinessArchitecture contentfwk_businessarchitecture) {
        this.contentfwk_businessarchitecture = contentfwk_businessarchitecture;
    }
    public List<contentfwk_Process> getContentfwk_processs() {
        return contentfwk_processs;
    }

    public void addContentfwk_process(Contentfwk_process contentfwk_process) {
        this.contentfwk_processs.add(contentfwk_process);
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
    public contentfwk_Actor getContentfwk_actor() {
        return contentfwk_actor;
    }

    public void setContentfwk_actor(contentfwk_Actor contentfwk_actor) {
        this.contentfwk_actor = contentfwk_actor;
    }
    public List<contentfwk_Product> getContentfwk_products() {
        return contentfwk_products;
    }

    public void addContentfwk_product(Contentfwk_product contentfwk_product) {
        this.contentfwk_products.add(contentfwk_product);
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

}