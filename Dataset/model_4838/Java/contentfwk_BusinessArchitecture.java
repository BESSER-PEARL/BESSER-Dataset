





import java.util.List;
import java.util.ArrayList;

public class contentfwk_BusinessArchitecture extends Architecture {






    private List<contentfwk_Control> contentfwk_controls;




    private List<contentfwk_Process> contentfwk_processs;




    private List<contentfwk_Function> contentfwk_functions;




    private List<contentfwk_Objective> contentfwk_objectives;




    private List<contentfwk_Role> contentfwk_roles;




    private List<contentfwk_Actor> contentfwk_actors;




    private List<contentfwk_OrganizationUnit> contentfwk_organizationunits;




    private List<contentfwk_Event> contentfwk_events;




    private List<contentfwk_BusinessService> contentfwk_businessservices;


    public contentfwk_BusinessArchitecture(
    ) {
        super(
        );
        this.contentfwk_controls = new ArrayList<>();
        this.contentfwk_processs = new ArrayList<>();
        this.contentfwk_functions = new ArrayList<>();
        this.contentfwk_objectives = new ArrayList<>();
        this.contentfwk_roles = new ArrayList<>();
        this.contentfwk_actors = new ArrayList<>();
        this.contentfwk_organizationunits = new ArrayList<>();
        this.contentfwk_events = new ArrayList<>();
        this.contentfwk_businessservices = new ArrayList<>();
    }

    public contentfwk_BusinessArchitecture(
        ArrayList<contentfwk_Control> contentfwk_controls,        ArrayList<contentfwk_Process> contentfwk_processs,        ArrayList<contentfwk_Function> contentfwk_functions,        ArrayList<contentfwk_Objective> contentfwk_objectives,        ArrayList<contentfwk_Role> contentfwk_roles,        ArrayList<contentfwk_Actor> contentfwk_actors,        ArrayList<contentfwk_OrganizationUnit> contentfwk_organizationunits,        ArrayList<contentfwk_Event> contentfwk_events,        ArrayList<contentfwk_BusinessService> contentfwk_businessservices    ) {
        this.contentfwk_controls = contentfwk_controls;
        this.contentfwk_processs = contentfwk_processs;
        this.contentfwk_functions = contentfwk_functions;
        this.contentfwk_objectives = contentfwk_objectives;
        this.contentfwk_roles = contentfwk_roles;
        this.contentfwk_actors = contentfwk_actors;
        this.contentfwk_organizationunits = contentfwk_organizationunits;
        this.contentfwk_events = contentfwk_events;
        this.contentfwk_businessservices = contentfwk_businessservices;
    }


    public List<contentfwk_Control> getContentfwk_controls() {
        return contentfwk_controls;
    }

    public void addContentfwk_control(Contentfwk_control contentfwk_control) {
        this.contentfwk_controls.add(contentfwk_control);
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
    public List<contentfwk_Objective> getContentfwk_objectives() {
        return contentfwk_objectives;
    }

    public void addContentfwk_objective(Contentfwk_objective contentfwk_objective) {
        this.contentfwk_objectives.add(contentfwk_objective);
    }
    public List<contentfwk_Role> getContentfwk_roles() {
        return contentfwk_roles;
    }

    public void addContentfwk_role(Contentfwk_role contentfwk_role) {
        this.contentfwk_roles.add(contentfwk_role);
    }
    public List<contentfwk_Actor> getContentfwk_actors() {
        return contentfwk_actors;
    }

    public void addContentfwk_actor(Contentfwk_actor contentfwk_actor) {
        this.contentfwk_actors.add(contentfwk_actor);
    }
    public List<contentfwk_OrganizationUnit> getContentfwk_organizationunits() {
        return contentfwk_organizationunits;
    }

    public void addContentfwk_organizationunit(Contentfwk_organizationunit contentfwk_organizationunit) {
        this.contentfwk_organizationunits.add(contentfwk_organizationunit);
    }
    public List<contentfwk_Event> getContentfwk_events() {
        return contentfwk_events;
    }

    public void addContentfwk_event(Contentfwk_event contentfwk_event) {
        this.contentfwk_events.add(contentfwk_event);
    }
    public List<contentfwk_BusinessService> getContentfwk_businessservices() {
        return contentfwk_businessservices;
    }

    public void addContentfwk_businessservice(Contentfwk_businessservice contentfwk_businessservice) {
        this.contentfwk_businessservices.add(contentfwk_businessservice);
    }

}