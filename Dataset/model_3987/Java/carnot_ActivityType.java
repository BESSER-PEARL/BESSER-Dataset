





import java.util.List;
import java.util.ArrayList;

public class carnot_ActivityType extends IEventHandlerOwner, IIdentifiableModelElement {

    private String implementation;
    private String subProcessMode;
    private String join;
    private String hibernateOnCreation;
    private String split;
    private String loopCondition;
    private String loopType;
    private String allowsAbortByPerformer;





    private List<carnot_TransitionType> carnot_transitiontypes;




    private carnot_IModelParticipant carnot_imodelparticipant;




    private carnot_ProcessDefinitionType carnot_processdefinitiontype;




    private carnot_IModelParticipant carnot_imodelparticipant;




    private carnot_ProcessDefinitionType carnot_processdefinitiontype;




    private carnot_TransitionType carnot_transitiontype;




    private List<carnot_TransitionType> carnot_transitiontypes;




    private carnot_IModelParticipant carnot_imodelparticipant;




    private List<carnot_DataMappingType> carnot_datamappingtypes;




    private carnot_ProcessDefinitionType carnot_processdefinitiontype;




    private carnot_TransitionType carnot_transitiontype;


    public carnot_ActivityType(
        String implementation,        String subProcessMode,        String join,        String hibernateOnCreation,        String split,        String loopCondition,        String loopType,        String allowsAbortByPerformer    ) {
        super(
        );
        this.implementation = implementation;
        this.subProcessMode = subProcessMode;
        this.join = join;
        this.hibernateOnCreation = hibernateOnCreation;
        this.split = split;
        this.loopCondition = loopCondition;
        this.loopType = loopType;
        this.allowsAbortByPerformer = allowsAbortByPerformer;
        this.carnot_transitiontypes = new ArrayList<>();
        this.carnot_transitiontypes = new ArrayList<>();
        this.carnot_datamappingtypes = new ArrayList<>();
    }

    public carnot_ActivityType(
        String implementation,        String subProcessMode,        String join,        String hibernateOnCreation,        String split,        String loopCondition,        String loopType,        String allowsAbortByPerformer        ArrayList<carnot_TransitionType> carnot_transitiontypes,        ArrayList<carnot_TransitionType> carnot_transitiontypes,        ArrayList<carnot_DataMappingType> carnot_datamappingtypes    ) {
        this.implementation = implementation;
        this.subProcessMode = subProcessMode;
        this.join = join;
        this.hibernateOnCreation = hibernateOnCreation;
        this.split = split;
        this.loopCondition = loopCondition;
        this.loopType = loopType;
        this.allowsAbortByPerformer = allowsAbortByPerformer;
        this.carnot_transitiontypes = carnot_transitiontypes;
        this.carnot_transitiontypes = carnot_transitiontypes;
        this.carnot_datamappingtypes = carnot_datamappingtypes;
    }

    public String getImplementation() {
        return implementation;
    }

    public void setImplementation(String implementation) {
        this.implementation = implementation;
    }
    public String getSubprocessmode() {
        return subProcessMode;
    }

    public void setSubprocessmode(String subProcessMode) {
        this.subProcessMode = subProcessMode;
    }
    public String getJoin() {
        return join;
    }

    public void setJoin(String join) {
        this.join = join;
    }
    public String getHibernateoncreation() {
        return hibernateOnCreation;
    }

    public void setHibernateoncreation(String hibernateOnCreation) {
        this.hibernateOnCreation = hibernateOnCreation;
    }
    public String getSplit() {
        return split;
    }

    public void setSplit(String split) {
        this.split = split;
    }
    public String getLoopcondition() {
        return loopCondition;
    }

    public void setLoopcondition(String loopCondition) {
        this.loopCondition = loopCondition;
    }
    public String getLooptype() {
        return loopType;
    }

    public void setLooptype(String loopType) {
        this.loopType = loopType;
    }
    public String getAllowsabortbyperformer() {
        return allowsAbortByPerformer;
    }

    public void setAllowsabortbyperformer(String allowsAbortByPerformer) {
        this.allowsAbortByPerformer = allowsAbortByPerformer;
    }

    public List<carnot_TransitionType> getCarnot_transitiontypes() {
        return carnot_transitiontypes;
    }

    public void addCarnot_transitiontype(Carnot_transitiontype carnot_transitiontype) {
        this.carnot_transitiontypes.add(carnot_transitiontype);
    }
    public carnot_IModelParticipant getCarnot_imodelparticipant() {
        return carnot_imodelparticipant;
    }

    public void setCarnot_imodelparticipant(carnot_IModelParticipant carnot_imodelparticipant) {
        this.carnot_imodelparticipant = carnot_imodelparticipant;
    }
    public carnot_ProcessDefinitionType getCarnot_processdefinitiontype() {
        return carnot_processdefinitiontype;
    }

    public void setCarnot_processdefinitiontype(carnot_ProcessDefinitionType carnot_processdefinitiontype) {
        this.carnot_processdefinitiontype = carnot_processdefinitiontype;
    }
    public carnot_IModelParticipant getCarnot_imodelparticipant() {
        return carnot_imodelparticipant;
    }

    public void setCarnot_imodelparticipant(carnot_IModelParticipant carnot_imodelparticipant) {
        this.carnot_imodelparticipant = carnot_imodelparticipant;
    }
    public carnot_ProcessDefinitionType getCarnot_processdefinitiontype() {
        return carnot_processdefinitiontype;
    }

    public void setCarnot_processdefinitiontype(carnot_ProcessDefinitionType carnot_processdefinitiontype) {
        this.carnot_processdefinitiontype = carnot_processdefinitiontype;
    }
    public carnot_TransitionType getCarnot_transitiontype() {
        return carnot_transitiontype;
    }

    public void setCarnot_transitiontype(carnot_TransitionType carnot_transitiontype) {
        this.carnot_transitiontype = carnot_transitiontype;
    }
    public List<carnot_TransitionType> getCarnot_transitiontypes() {
        return carnot_transitiontypes;
    }

    public void addCarnot_transitiontype(Carnot_transitiontype carnot_transitiontype) {
        this.carnot_transitiontypes.add(carnot_transitiontype);
    }
    public carnot_IModelParticipant getCarnot_imodelparticipant() {
        return carnot_imodelparticipant;
    }

    public void setCarnot_imodelparticipant(carnot_IModelParticipant carnot_imodelparticipant) {
        this.carnot_imodelparticipant = carnot_imodelparticipant;
    }
    public List<carnot_DataMappingType> getCarnot_datamappingtypes() {
        return carnot_datamappingtypes;
    }

    public void addCarnot_datamappingtype(Carnot_datamappingtype carnot_datamappingtype) {
        this.carnot_datamappingtypes.add(carnot_datamappingtype);
    }
    public carnot_ProcessDefinitionType getCarnot_processdefinitiontype() {
        return carnot_processdefinitiontype;
    }

    public void setCarnot_processdefinitiontype(carnot_ProcessDefinitionType carnot_processdefinitiontype) {
        this.carnot_processdefinitiontype = carnot_processdefinitiontype;
    }
    public carnot_TransitionType getCarnot_transitiontype() {
        return carnot_transitiontype;
    }

    public void setCarnot_transitiontype(carnot_TransitionType carnot_transitiontype) {
        this.carnot_transitiontype = carnot_transitiontype;
    }

}