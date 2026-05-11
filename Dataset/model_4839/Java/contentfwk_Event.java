





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Event extends Element {






    private contentfwk_Process contentfwk_process;




    private contentfwk_Actor contentfwk_actor;




    private List<contentfwk_Process> contentfwk_processs;




    private List<contentfwk_Service> contentfwk_services;




    private contentfwk_Actor contentfwk_actor;




    private contentfwk_Actor contentfwk_actor;




    private contentfwk_BusinessArchitecture contentfwk_businessarchitecture;




    private contentfwk_Service contentfwk_service;




    private List<contentfwk_Actor> contentfwk_actors;




    private List<contentfwk_Process> contentfwk_processs;




    private contentfwk_Process contentfwk_process;


    public contentfwk_Event(
    ) {
        super(
        );
        this.contentfwk_processs = new ArrayList<>();
        this.contentfwk_services = new ArrayList<>();
        this.contentfwk_actors = new ArrayList<>();
        this.contentfwk_processs = new ArrayList<>();
    }

    public contentfwk_Event(
        ArrayList<contentfwk_Process> contentfwk_processs,        ArrayList<contentfwk_Service> contentfwk_services,        ArrayList<contentfwk_Actor> contentfwk_actors,        ArrayList<contentfwk_Process> contentfwk_processs    ) {
        this.contentfwk_processs = contentfwk_processs;
        this.contentfwk_services = contentfwk_services;
        this.contentfwk_actors = contentfwk_actors;
        this.contentfwk_processs = contentfwk_processs;
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
    public List<contentfwk_Process> getContentfwk_processs() {
        return contentfwk_processs;
    }

    public void addContentfwk_process(Contentfwk_process contentfwk_process) {
        this.contentfwk_processs.add(contentfwk_process);
    }
    public List<contentfwk_Service> getContentfwk_services() {
        return contentfwk_services;
    }

    public void addContentfwk_service(Contentfwk_service contentfwk_service) {
        this.contentfwk_services.add(contentfwk_service);
    }
    public contentfwk_Actor getContentfwk_actor() {
        return contentfwk_actor;
    }

    public void setContentfwk_actor(contentfwk_Actor contentfwk_actor) {
        this.contentfwk_actor = contentfwk_actor;
    }
    public contentfwk_Actor getContentfwk_actor() {
        return contentfwk_actor;
    }

    public void setContentfwk_actor(contentfwk_Actor contentfwk_actor) {
        this.contentfwk_actor = contentfwk_actor;
    }
    public contentfwk_BusinessArchitecture getContentfwk_businessarchitecture() {
        return contentfwk_businessarchitecture;
    }

    public void setContentfwk_businessarchitecture(contentfwk_BusinessArchitecture contentfwk_businessarchitecture) {
        this.contentfwk_businessarchitecture = contentfwk_businessarchitecture;
    }
    public contentfwk_Service getContentfwk_service() {
        return contentfwk_service;
    }

    public void setContentfwk_service(contentfwk_Service contentfwk_service) {
        this.contentfwk_service = contentfwk_service;
    }
    public List<contentfwk_Actor> getContentfwk_actors() {
        return contentfwk_actors;
    }

    public void addContentfwk_actor(Contentfwk_actor contentfwk_actor) {
        this.contentfwk_actors.add(contentfwk_actor);
    }
    public List<contentfwk_Process> getContentfwk_processs() {
        return contentfwk_processs;
    }

    public void addContentfwk_process(Contentfwk_process contentfwk_process) {
        this.contentfwk_processs.add(contentfwk_process);
    }
    public contentfwk_Process getContentfwk_process() {
        return contentfwk_process;
    }

    public void setContentfwk_process(contentfwk_Process contentfwk_process) {
        this.contentfwk_process = contentfwk_process;
    }

}