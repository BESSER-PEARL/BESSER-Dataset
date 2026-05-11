





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Actor extends Element {

    private String actorTasks;
    private String actorGoal;
    private String FTEs;





    private contentfwk_Service contentfwk_service;




    private contentfwk_OrganizationUnit contentfwk_organizationunit;




    private List<contentfwk_Process> contentfwk_processs;




    private List<contentfwk_Actor> contentfwk_actors;




    private contentfwk_BusinessArchitecture contentfwk_businessarchitecture;




    private contentfwk_Function contentfwk_function;




    private contentfwk_Function contentfwk_function;




    private List<contentfwk_Function> contentfwk_functions;




    private List<contentfwk_Service> contentfwk_services;




    private contentfwk_OrganizationUnit contentfwk_organizationunit;




    private List<contentfwk_Function> contentfwk_functions;




    private contentfwk_Process contentfwk_process;


    public contentfwk_Actor(
        String actorTasks,        String actorGoal,        String FTEs    ) {
        super(
        );
        this.actorTasks = actorTasks;
        this.actorGoal = actorGoal;
        this.FTEs = FTEs;
        this.contentfwk_processs = new ArrayList<>();
        this.contentfwk_actors = new ArrayList<>();
        this.contentfwk_functions = new ArrayList<>();
        this.contentfwk_services = new ArrayList<>();
        this.contentfwk_functions = new ArrayList<>();
    }

    public contentfwk_Actor(
        String actorTasks,        String actorGoal,        String FTEs        ArrayList<contentfwk_Process> contentfwk_processs,        ArrayList<contentfwk_Actor> contentfwk_actors,        ArrayList<contentfwk_Function> contentfwk_functions,        ArrayList<contentfwk_Service> contentfwk_services,        ArrayList<contentfwk_Function> contentfwk_functions    ) {
        this.actorTasks = actorTasks;
        this.actorGoal = actorGoal;
        this.FTEs = FTEs;
        this.contentfwk_processs = contentfwk_processs;
        this.contentfwk_actors = contentfwk_actors;
        this.contentfwk_functions = contentfwk_functions;
        this.contentfwk_services = contentfwk_services;
        this.contentfwk_functions = contentfwk_functions;
    }

    public String getActortasks() {
        return actorTasks;
    }

    public void setActortasks(String actorTasks) {
        this.actorTasks = actorTasks;
    }
    public String getActorgoal() {
        return actorGoal;
    }

    public void setActorgoal(String actorGoal) {
        this.actorGoal = actorGoal;
    }
    public String getFtes() {
        return FTEs;
    }

    public void setFtes(String FTEs) {
        this.FTEs = FTEs;
    }

    public contentfwk_Service getContentfwk_service() {
        return contentfwk_service;
    }

    public void setContentfwk_service(contentfwk_Service contentfwk_service) {
        this.contentfwk_service = contentfwk_service;
    }
    public contentfwk_OrganizationUnit getContentfwk_organizationunit() {
        return contentfwk_organizationunit;
    }

    public void setContentfwk_organizationunit(contentfwk_OrganizationUnit contentfwk_organizationunit) {
        this.contentfwk_organizationunit = contentfwk_organizationunit;
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
    public contentfwk_BusinessArchitecture getContentfwk_businessarchitecture() {
        return contentfwk_businessarchitecture;
    }

    public void setContentfwk_businessarchitecture(contentfwk_BusinessArchitecture contentfwk_businessarchitecture) {
        this.contentfwk_businessarchitecture = contentfwk_businessarchitecture;
    }
    public contentfwk_Function getContentfwk_function() {
        return contentfwk_function;
    }

    public void setContentfwk_function(contentfwk_Function contentfwk_function) {
        this.contentfwk_function = contentfwk_function;
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
    public List<contentfwk_Service> getContentfwk_services() {
        return contentfwk_services;
    }

    public void addContentfwk_service(Contentfwk_service contentfwk_service) {
        this.contentfwk_services.add(contentfwk_service);
    }
    public contentfwk_OrganizationUnit getContentfwk_organizationunit() {
        return contentfwk_organizationunit;
    }

    public void setContentfwk_organizationunit(contentfwk_OrganizationUnit contentfwk_organizationunit) {
        this.contentfwk_organizationunit = contentfwk_organizationunit;
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