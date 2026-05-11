





import java.util.List;
import java.util.ArrayList;

public class jpdl32_DocumentRoot  {

    private String mixed;
    private String template;
    private String description;
    private String recipients;
    private String text;
    private String subject;
    private String to;





    private List<jpdl32_ActionType> jpdl32_actiontypes;




    private List<jpdl32_DecisionType> jpdl32_decisiontypes;




    private List<jpdl32_AssignmentType> jpdl32_assignmenttypes;




    private List<jpdl32_ScriptType> jpdl32_scripttypes;




    private List<jpdl32_Delegation> jpdl32_delegations;




    private List<jpdl32_TransitionType> jpdl32_transitiontypes;




    private List<jpdl32_CancelTimerType> jpdl32_canceltimertypes;




    private List<jpdl32_EventType> jpdl32_eventtypes;




    private List<jpdl32_CreateTimerType> jpdl32_createtimertypes;




    private List<jpdl32_ExceptionHandlerType> jpdl32_exceptionhandlertypes;


    public jpdl32_DocumentRoot(
        String mixed,        String template,        String description,        String recipients,        String text,        String subject,        String to    ) {
        this.mixed = mixed;
        this.template = template;
        this.description = description;
        this.recipients = recipients;
        this.text = text;
        this.subject = subject;
        this.to = to;
        this.jpdl32_actiontypes = new ArrayList<>();
        this.jpdl32_decisiontypes = new ArrayList<>();
        this.jpdl32_assignmenttypes = new ArrayList<>();
        this.jpdl32_scripttypes = new ArrayList<>();
        this.jpdl32_delegations = new ArrayList<>();
        this.jpdl32_transitiontypes = new ArrayList<>();
        this.jpdl32_canceltimertypes = new ArrayList<>();
        this.jpdl32_eventtypes = new ArrayList<>();
        this.jpdl32_createtimertypes = new ArrayList<>();
        this.jpdl32_exceptionhandlertypes = new ArrayList<>();
    }

    public jpdl32_DocumentRoot(
        String mixed,        String template,        String description,        String recipients,        String text,        String subject,        String to        ArrayList<jpdl32_ActionType> jpdl32_actiontypes,        ArrayList<jpdl32_DecisionType> jpdl32_decisiontypes,        ArrayList<jpdl32_AssignmentType> jpdl32_assignmenttypes,        ArrayList<jpdl32_ScriptType> jpdl32_scripttypes,        ArrayList<jpdl32_Delegation> jpdl32_delegations,        ArrayList<jpdl32_TransitionType> jpdl32_transitiontypes,        ArrayList<jpdl32_CancelTimerType> jpdl32_canceltimertypes,        ArrayList<jpdl32_EventType> jpdl32_eventtypes,        ArrayList<jpdl32_CreateTimerType> jpdl32_createtimertypes,        ArrayList<jpdl32_ExceptionHandlerType> jpdl32_exceptionhandlertypes    ) {
        this.mixed = mixed;
        this.template = template;
        this.description = description;
        this.recipients = recipients;
        this.text = text;
        this.subject = subject;
        this.to = to;
        this.jpdl32_actiontypes = jpdl32_actiontypes;
        this.jpdl32_decisiontypes = jpdl32_decisiontypes;
        this.jpdl32_assignmenttypes = jpdl32_assignmenttypes;
        this.jpdl32_scripttypes = jpdl32_scripttypes;
        this.jpdl32_delegations = jpdl32_delegations;
        this.jpdl32_transitiontypes = jpdl32_transitiontypes;
        this.jpdl32_canceltimertypes = jpdl32_canceltimertypes;
        this.jpdl32_eventtypes = jpdl32_eventtypes;
        this.jpdl32_createtimertypes = jpdl32_createtimertypes;
        this.jpdl32_exceptionhandlertypes = jpdl32_exceptionhandlertypes;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getTemplate() {
        return template;
    }

    public void setTemplate(String template) {
        this.template = template;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getRecipients() {
        return recipients;
    }

    public void setRecipients(String recipients) {
        this.recipients = recipients;
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
    public String getTo() {
        return to;
    }

    public void setTo(String to) {
        this.to = to;
    }

    public List<jpdl32_ActionType> getJpdl32_actiontypes() {
        return jpdl32_actiontypes;
    }

    public void addJpdl32_actiontype(Jpdl32_actiontype jpdl32_actiontype) {
        this.jpdl32_actiontypes.add(jpdl32_actiontype);
    }
    public List<jpdl32_DecisionType> getJpdl32_decisiontypes() {
        return jpdl32_decisiontypes;
    }

    public void addJpdl32_decisiontype(Jpdl32_decisiontype jpdl32_decisiontype) {
        this.jpdl32_decisiontypes.add(jpdl32_decisiontype);
    }
    public List<jpdl32_AssignmentType> getJpdl32_assignmenttypes() {
        return jpdl32_assignmenttypes;
    }

    public void addJpdl32_assignmenttype(Jpdl32_assignmenttype jpdl32_assignmenttype) {
        this.jpdl32_assignmenttypes.add(jpdl32_assignmenttype);
    }
    public List<jpdl32_ScriptType> getJpdl32_scripttypes() {
        return jpdl32_scripttypes;
    }

    public void addJpdl32_scripttype(Jpdl32_scripttype jpdl32_scripttype) {
        this.jpdl32_scripttypes.add(jpdl32_scripttype);
    }
    public List<jpdl32_Delegation> getJpdl32_delegations() {
        return jpdl32_delegations;
    }

    public void addJpdl32_delegation(Jpdl32_delegation jpdl32_delegation) {
        this.jpdl32_delegations.add(jpdl32_delegation);
    }
    public List<jpdl32_TransitionType> getJpdl32_transitiontypes() {
        return jpdl32_transitiontypes;
    }

    public void addJpdl32_transitiontype(Jpdl32_transitiontype jpdl32_transitiontype) {
        this.jpdl32_transitiontypes.add(jpdl32_transitiontype);
    }
    public List<jpdl32_CancelTimerType> getJpdl32_canceltimertypes() {
        return jpdl32_canceltimertypes;
    }

    public void addJpdl32_canceltimertype(Jpdl32_canceltimertype jpdl32_canceltimertype) {
        this.jpdl32_canceltimertypes.add(jpdl32_canceltimertype);
    }
    public List<jpdl32_EventType> getJpdl32_eventtypes() {
        return jpdl32_eventtypes;
    }

    public void addJpdl32_eventtype(Jpdl32_eventtype jpdl32_eventtype) {
        this.jpdl32_eventtypes.add(jpdl32_eventtype);
    }
    public List<jpdl32_CreateTimerType> getJpdl32_createtimertypes() {
        return jpdl32_createtimertypes;
    }

    public void addJpdl32_createtimertype(Jpdl32_createtimertype jpdl32_createtimertype) {
        this.jpdl32_createtimertypes.add(jpdl32_createtimertype);
    }
    public List<jpdl32_ExceptionHandlerType> getJpdl32_exceptionhandlertypes() {
        return jpdl32_exceptionhandlertypes;
    }

    public void addJpdl32_exceptionhandlertype(Jpdl32_exceptionhandlertype jpdl32_exceptionhandlertype) {
        this.jpdl32_exceptionhandlertypes.add(jpdl32_exceptionhandlertype);
    }

}