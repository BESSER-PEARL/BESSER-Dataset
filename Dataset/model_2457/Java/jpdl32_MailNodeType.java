





import java.util.List;
import java.util.ArrayList;

public class jpdl32_MailNodeType  {

    private String actors;
    private String subject;
    private String name;
    private String template;
    private String group;
    private String description;
    private String text1;
    private String async_;
    private String subject1;
    private String to;
    private String text;





    private List<jpdl32_TransitionType> jpdl32_transitiontypes;




    private jpdl32_DocumentRoot jpdl32_documentroot;




    private List<jpdl32_ExceptionHandlerType> jpdl32_exceptionhandlertypes;




    private List<jpdl32_EventType> jpdl32_eventtypes;


    public jpdl32_MailNodeType(
        String actors,        String subject,        String name,        String template,        String group,        String description,        String text1,        String async_,        String subject1,        String to,        String text    ) {
        this.actors = actors;
        this.subject = subject;
        this.name = name;
        this.template = template;
        this.group = group;
        this.description = description;
        this.text1 = text1;
        this.async_ = async_;
        this.subject1 = subject1;
        this.to = to;
        this.text = text;
        this.jpdl32_transitiontypes = new ArrayList<>();
        this.jpdl32_exceptionhandlertypes = new ArrayList<>();
        this.jpdl32_eventtypes = new ArrayList<>();
    }

    public jpdl32_MailNodeType(
        String actors,        String subject,        String name,        String template,        String group,        String description,        String text1,        String async_,        String subject1,        String to,        String text        ArrayList<jpdl32_TransitionType> jpdl32_transitiontypes,        ArrayList<jpdl32_ExceptionHandlerType> jpdl32_exceptionhandlertypes,        ArrayList<jpdl32_EventType> jpdl32_eventtypes    ) {
        this.actors = actors;
        this.subject = subject;
        this.name = name;
        this.template = template;
        this.group = group;
        this.description = description;
        this.text1 = text1;
        this.async_ = async_;
        this.subject1 = subject1;
        this.to = to;
        this.text = text;
        this.jpdl32_transitiontypes = jpdl32_transitiontypes;
        this.jpdl32_exceptionhandlertypes = jpdl32_exceptionhandlertypes;
        this.jpdl32_eventtypes = jpdl32_eventtypes;
    }

    public String getActors() {
        return actors;
    }

    public void setActors(String actors) {
        this.actors = actors;
    }
    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTemplate() {
        return template;
    }

    public void setTemplate(String template) {
        this.template = template;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getText1() {
        return text1;
    }

    public void setText1(String text1) {
        this.text1 = text1;
    }
    public String getAsync_() {
        return async_;
    }

    public void setAsync_(String async_) {
        this.async_ = async_;
    }
    public String getSubject1() {
        return subject1;
    }

    public void setSubject1(String subject1) {
        this.subject1 = subject1;
    }
    public String getTo() {
        return to;
    }

    public void setTo(String to) {
        this.to = to;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public List<jpdl32_TransitionType> getJpdl32_transitiontypes() {
        return jpdl32_transitiontypes;
    }

    public void addJpdl32_transitiontype(Jpdl32_transitiontype jpdl32_transitiontype) {
        this.jpdl32_transitiontypes.add(jpdl32_transitiontype);
    }
    public jpdl32_DocumentRoot getJpdl32_documentroot() {
        return jpdl32_documentroot;
    }

    public void setJpdl32_documentroot(jpdl32_DocumentRoot jpdl32_documentroot) {
        this.jpdl32_documentroot = jpdl32_documentroot;
    }
    public List<jpdl32_ExceptionHandlerType> getJpdl32_exceptionhandlertypes() {
        return jpdl32_exceptionhandlertypes;
    }

    public void addJpdl32_exceptionhandlertype(Jpdl32_exceptionhandlertype jpdl32_exceptionhandlertype) {
        this.jpdl32_exceptionhandlertypes.add(jpdl32_exceptionhandlertype);
    }
    public List<jpdl32_EventType> getJpdl32_eventtypes() {
        return jpdl32_eventtypes;
    }

    public void addJpdl32_eventtype(Jpdl32_eventtype jpdl32_eventtype) {
        this.jpdl32_eventtypes.add(jpdl32_eventtype);
    }

}