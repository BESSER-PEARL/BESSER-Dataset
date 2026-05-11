





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Actor extends Element {

    private String actorTasks;
    private String actorGoal;
    private String FTEs;





    private contentfwk_Function contentfwk_function;




    private List<contentfwk_Process> contentfwk_processs;




    private contentfwk_OrganizationUnit contentfwk_organizationunit;




    private contentfwk_OrganizationUnit contentfwk_organizationunit;




    private List<contentfwk_Function> contentfwk_functions;




    private contentfwk_Process contentfwk_process;




    private contentfwk_BusinessArchitecture contentfwk_businessarchitecture;




    private contentfwk_Location contentfwk_location;




    private contentfwk_Event contentfwk_event;




    private contentfwk_Function contentfwk_function;




    private List<contentfwk_Event> contentfwk_events;




    private List<contentfwk_Event> contentfwk_events;




    private List<contentfwk_Function> contentfwk_functions;




    private contentfwk_Actor contentfwk_actor;




    private contentfwk_Event contentfwk_event;




    private contentfwk_Location contentfwk_location;


    public contentfwk_Actor(
        String actorTasks,        String actorGoal,        String FTEs    ) {
        super(
        );
        this.actorTasks = actorTasks;
        this.actorGoal = actorGoal;
        this.FTEs = FTEs;
        this.contentfwk_processs = new ArrayList<>();
        this.contentfwk_functions = new ArrayList<>();
        this.contentfwk_events = new ArrayList<>();
        this.contentfwk_events = new ArrayList<>();
        this.contentfwk_functions = new ArrayList<>();
    }

    public contentfwk_Actor(
        String actorTasks,        String actorGoal,        String FTEs        ArrayList<contentfwk_Process> contentfwk_processs,        ArrayList<contentfwk_Function> contentfwk_functions,        ArrayList<contentfwk_Event> contentfwk_events,        ArrayList<contentfwk_Event> contentfwk_events,        ArrayList<contentfwk_Function> contentfwk_functions    ) {
        this.actorTasks = actorTasks;
        this.actorGoal = actorGoal;
        this.FTEs = FTEs;
        this.contentfwk_processs = contentfwk_processs;
        this.contentfwk_functions = contentfwk_functions;
        this.contentfwk_events = contentfwk_events;
        this.contentfwk_events = contentfwk_events;
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
    public contentfwk_OrganizationUnit getContentfwk_organizationunit() {
        return contentfwk_organizationunit;
    }

    public void setContentfwk_organizationunit(contentfwk_OrganizationUnit contentfwk_organizationunit) {
        this.contentfwk_organizationunit = contentfwk_organizationunit;
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
    public contentfwk_BusinessArchitecture getContentfwk_businessarchitecture() {
        return contentfwk_businessarchitecture;
    }

    public void setContentfwk_businessarchitecture(contentfwk_BusinessArchitecture contentfwk_businessarchitecture) {
        this.contentfwk_businessarchitecture = contentfwk_businessarchitecture;
    }
    public contentfwk_Location getContentfwk_location() {
        return contentfwk_location;
    }

    public void setContentfwk_location(contentfwk_Location contentfwk_location) {
        this.contentfwk_location = contentfwk_location;
    }
    public contentfwk_Event getContentfwk_event() {
        return contentfwk_event;
    }

    public void setContentfwk_event(contentfwk_Event contentfwk_event) {
        this.contentfwk_event = contentfwk_event;
    }
    public contentfwk_Function getContentfwk_function() {
        return contentfwk_function;
    }

    public void setContentfwk_function(contentfwk_Function contentfwk_function) {
        this.contentfwk_function = contentfwk_function;
    }
    public List<contentfwk_Event> getContentfwk_events() {
        return contentfwk_events;
    }

    public void addContentfwk_event(Contentfwk_event contentfwk_event) {
        this.contentfwk_events.add(contentfwk_event);
    }
    public List<contentfwk_Event> getContentfwk_events() {
        return contentfwk_events;
    }

    public void addContentfwk_event(Contentfwk_event contentfwk_event) {
        this.contentfwk_events.add(contentfwk_event);
    }
    public List<contentfwk_Function> getContentfwk_functions() {
        return contentfwk_functions;
    }

    public void addContentfwk_function(Contentfwk_function contentfwk_function) {
        this.contentfwk_functions.add(contentfwk_function);
    }
    public contentfwk_Actor getContentfwk_actor() {
        return contentfwk_actor;
    }

    public void setContentfwk_actor(contentfwk_Actor contentfwk_actor) {
        this.contentfwk_actor = contentfwk_actor;
    }
    public contentfwk_Event getContentfwk_event() {
        return contentfwk_event;
    }

    public void setContentfwk_event(contentfwk_Event contentfwk_event) {
        this.contentfwk_event = contentfwk_event;
    }
    public contentfwk_Location getContentfwk_location() {
        return contentfwk_location;
    }

    public void setContentfwk_location(contentfwk_Location contentfwk_location) {
        this.contentfwk_location = contentfwk_location;
    }

}