





import java.util.List;
import java.util.ArrayList;

public class scmodel_Transition  {

    private String triggerExpRateCodeImports;
    private String messageCheckerCode;
    private boolean selfTransition;
    private String guardImports;
    private String triggerCodeLanguage;
    private String id;
    private String guard;
    private String triggerConditionCodeImports;
    private String onTransition;
    private String messageCheckerType;
    private float priority;
    private String triggerConditionCode;
    private boolean defaultTransition;
    private String triggerTimedCodeImports;
    private String triggerExpRateCode;
    private float triggerTime;
    private String messageCheckerCodeImports;
    private boolean outOfBranch;
    private String onTransitionImports;
    private String messageCheckerClass;
    private String triggerProbCode;
    private String messageCheckerConditionLanguage;
    private String triggerTimedCode;
    private String triggerProbCodeImports;
    private String triggerType;
    private String uuid;





    private scmodel_AbstractState scmodel_abstractstate;




    private scmodel_StateMachine scmodel_statemachine;




    private scmodel_AbstractState scmodel_abstractstate;


    public scmodel_Transition(
        String triggerExpRateCodeImports,        String messageCheckerCode,        boolean selfTransition,        String guardImports,        String triggerCodeLanguage,        String id,        String guard,        String triggerConditionCodeImports,        String onTransition,        String messageCheckerType,        float priority,        String triggerConditionCode,        boolean defaultTransition,        String triggerTimedCodeImports,        String triggerExpRateCode,        float triggerTime,        String messageCheckerCodeImports,        boolean outOfBranch,        String onTransitionImports,        String messageCheckerClass,        String triggerProbCode,        String messageCheckerConditionLanguage,        String triggerTimedCode,        String triggerProbCodeImports,        String triggerType,        String uuid    ) {
        this.triggerExpRateCodeImports = triggerExpRateCodeImports;
        this.messageCheckerCode = messageCheckerCode;
        this.selfTransition = selfTransition;
        this.guardImports = guardImports;
        this.triggerCodeLanguage = triggerCodeLanguage;
        this.id = id;
        this.guard = guard;
        this.triggerConditionCodeImports = triggerConditionCodeImports;
        this.onTransition = onTransition;
        this.messageCheckerType = messageCheckerType;
        this.priority = priority;
        this.triggerConditionCode = triggerConditionCode;
        this.defaultTransition = defaultTransition;
        this.triggerTimedCodeImports = triggerTimedCodeImports;
        this.triggerExpRateCode = triggerExpRateCode;
        this.triggerTime = triggerTime;
        this.messageCheckerCodeImports = messageCheckerCodeImports;
        this.outOfBranch = outOfBranch;
        this.onTransitionImports = onTransitionImports;
        this.messageCheckerClass = messageCheckerClass;
        this.triggerProbCode = triggerProbCode;
        this.messageCheckerConditionLanguage = messageCheckerConditionLanguage;
        this.triggerTimedCode = triggerTimedCode;
        this.triggerProbCodeImports = triggerProbCodeImports;
        this.triggerType = triggerType;
        this.uuid = uuid;
    }


    public String getTriggerexpratecodeimports() {
        return triggerExpRateCodeImports;
    }

    public void setTriggerexpratecodeimports(String triggerExpRateCodeImports) {
        this.triggerExpRateCodeImports = triggerExpRateCodeImports;
    }
    public String getMessagecheckercode() {
        return messageCheckerCode;
    }

    public void setMessagecheckercode(String messageCheckerCode) {
        this.messageCheckerCode = messageCheckerCode;
    }
    public boolean getSelftransition() {
        return selfTransition;
    }

    public void setSelftransition(boolean selfTransition) {
        this.selfTransition = selfTransition;
    }
    public String getGuardimports() {
        return guardImports;
    }

    public void setGuardimports(String guardImports) {
        this.guardImports = guardImports;
    }
    public String getTriggercodelanguage() {
        return triggerCodeLanguage;
    }

    public void setTriggercodelanguage(String triggerCodeLanguage) {
        this.triggerCodeLanguage = triggerCodeLanguage;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getGuard() {
        return guard;
    }

    public void setGuard(String guard) {
        this.guard = guard;
    }
    public String getTriggerconditioncodeimports() {
        return triggerConditionCodeImports;
    }

    public void setTriggerconditioncodeimports(String triggerConditionCodeImports) {
        this.triggerConditionCodeImports = triggerConditionCodeImports;
    }
    public String getOntransition() {
        return onTransition;
    }

    public void setOntransition(String onTransition) {
        this.onTransition = onTransition;
    }
    public String getMessagecheckertype() {
        return messageCheckerType;
    }

    public void setMessagecheckertype(String messageCheckerType) {
        this.messageCheckerType = messageCheckerType;
    }
    public float getPriority() {
        return priority;
    }

    public void setPriority(float priority) {
        this.priority = priority;
    }
    public String getTriggerconditioncode() {
        return triggerConditionCode;
    }

    public void setTriggerconditioncode(String triggerConditionCode) {
        this.triggerConditionCode = triggerConditionCode;
    }
    public boolean getDefaulttransition() {
        return defaultTransition;
    }

    public void setDefaulttransition(boolean defaultTransition) {
        this.defaultTransition = defaultTransition;
    }
    public String getTriggertimedcodeimports() {
        return triggerTimedCodeImports;
    }

    public void setTriggertimedcodeimports(String triggerTimedCodeImports) {
        this.triggerTimedCodeImports = triggerTimedCodeImports;
    }
    public String getTriggerexpratecode() {
        return triggerExpRateCode;
    }

    public void setTriggerexpratecode(String triggerExpRateCode) {
        this.triggerExpRateCode = triggerExpRateCode;
    }
    public float getTriggertime() {
        return triggerTime;
    }

    public void setTriggertime(float triggerTime) {
        this.triggerTime = triggerTime;
    }
    public String getMessagecheckercodeimports() {
        return messageCheckerCodeImports;
    }

    public void setMessagecheckercodeimports(String messageCheckerCodeImports) {
        this.messageCheckerCodeImports = messageCheckerCodeImports;
    }
    public boolean getOutofbranch() {
        return outOfBranch;
    }

    public void setOutofbranch(boolean outOfBranch) {
        this.outOfBranch = outOfBranch;
    }
    public String getOntransitionimports() {
        return onTransitionImports;
    }

    public void setOntransitionimports(String onTransitionImports) {
        this.onTransitionImports = onTransitionImports;
    }
    public String getMessagecheckerclass() {
        return messageCheckerClass;
    }

    public void setMessagecheckerclass(String messageCheckerClass) {
        this.messageCheckerClass = messageCheckerClass;
    }
    public String getTriggerprobcode() {
        return triggerProbCode;
    }

    public void setTriggerprobcode(String triggerProbCode) {
        this.triggerProbCode = triggerProbCode;
    }
    public String getMessagecheckerconditionlanguage() {
        return messageCheckerConditionLanguage;
    }

    public void setMessagecheckerconditionlanguage(String messageCheckerConditionLanguage) {
        this.messageCheckerConditionLanguage = messageCheckerConditionLanguage;
    }
    public String getTriggertimedcode() {
        return triggerTimedCode;
    }

    public void setTriggertimedcode(String triggerTimedCode) {
        this.triggerTimedCode = triggerTimedCode;
    }
    public String getTriggerprobcodeimports() {
        return triggerProbCodeImports;
    }

    public void setTriggerprobcodeimports(String triggerProbCodeImports) {
        this.triggerProbCodeImports = triggerProbCodeImports;
    }
    public String getTriggertype() {
        return triggerType;
    }

    public void setTriggertype(String triggerType) {
        this.triggerType = triggerType;
    }
    public String getUuid() {
        return uuid;
    }

    public void setUuid(String uuid) {
        this.uuid = uuid;
    }

    public scmodel_AbstractState getScmodel_abstractstate() {
        return scmodel_abstractstate;
    }

    public void setScmodel_abstractstate(scmodel_AbstractState scmodel_abstractstate) {
        this.scmodel_abstractstate = scmodel_abstractstate;
    }
    public scmodel_StateMachine getScmodel_statemachine() {
        return scmodel_statemachine;
    }

    public void setScmodel_statemachine(scmodel_StateMachine scmodel_statemachine) {
        this.scmodel_statemachine = scmodel_statemachine;
    }
    public scmodel_AbstractState getScmodel_abstractstate() {
        return scmodel_abstractstate;
    }

    public void setScmodel_abstractstate(scmodel_AbstractState scmodel_abstractstate) {
        this.scmodel_abstractstate = scmodel_abstractstate;
    }

}