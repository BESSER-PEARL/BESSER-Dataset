





import java.util.List;
import java.util.ArrayList;

public class jpdl32_MailType  {

    private String name;
    private String template;
    private String to;
    private String text1;
    private String text;
    private String subject;
    private String subject1;
    private String async_;
    private String group;
    private String actors;





    private jpdl32_TransitionType jpdl32_transitiontype;




    private jpdl32_DocumentRoot jpdl32_documentroot;




    private jpdl32_EventType jpdl32_eventtype;


    public jpdl32_MailType(
        String name,        String template,        String to,        String text1,        String text,        String subject,        String subject1,        String async_,        String group,        String actors    ) {
        this.name = name;
        this.template = template;
        this.to = to;
        this.text1 = text1;
        this.text = text;
        this.subject = subject;
        this.subject1 = subject1;
        this.async_ = async_;
        this.group = group;
        this.actors = actors;
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
    public String getTo() {
        return to;
    }

    public void setTo(String to) {
        this.to = to;
    }
    public String getText1() {
        return text1;
    }

    public void setText1(String text1) {
        this.text1 = text1;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }
    public String getSubject1() {
        return subject1;
    }

    public void setSubject1(String subject1) {
        this.subject1 = subject1;
    }
    public String getAsync_() {
        return async_;
    }

    public void setAsync_(String async_) {
        this.async_ = async_;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getActors() {
        return actors;
    }

    public void setActors(String actors) {
        this.actors = actors;
    }

    public jpdl32_TransitionType getJpdl32_transitiontype() {
        return jpdl32_transitiontype;
    }

    public void setJpdl32_transitiontype(jpdl32_TransitionType jpdl32_transitiontype) {
        this.jpdl32_transitiontype = jpdl32_transitiontype;
    }
    public jpdl32_DocumentRoot getJpdl32_documentroot() {
        return jpdl32_documentroot;
    }

    public void setJpdl32_documentroot(jpdl32_DocumentRoot jpdl32_documentroot) {
        this.jpdl32_documentroot = jpdl32_documentroot;
    }
    public jpdl32_EventType getJpdl32_eventtype() {
        return jpdl32_eventtype;
    }

    public void setJpdl32_eventtype(jpdl32_EventType jpdl32_eventtype) {
        this.jpdl32_eventtype = jpdl32_eventtype;
    }

}