





import java.util.List;
import java.util.ArrayList;

public class carnot_ActivityType extends IEventHandlerOwner, IIdentifiableModelElement {

    private String subProcessMode;
    private String split;
    private String loopCondition;
    private String loopType;
    private String implementation;
    private String hibernateOnCreation;
    private String join;
    private String allowsAbortByPerformer;





    private List<carnot_DataMappingType> carnot_datamappingtypes;


    public carnot_ActivityType(
        String subProcessMode,        String split,        String loopCondition,        String loopType,        String implementation,        String hibernateOnCreation,        String join,        String allowsAbortByPerformer    ) {
        super(
        );
        this.subProcessMode = subProcessMode;
        this.split = split;
        this.loopCondition = loopCondition;
        this.loopType = loopType;
        this.implementation = implementation;
        this.hibernateOnCreation = hibernateOnCreation;
        this.join = join;
        this.allowsAbortByPerformer = allowsAbortByPerformer;
        this.carnot_datamappingtypes = new ArrayList<>();
    }

    public carnot_ActivityType(
        String subProcessMode,        String split,        String loopCondition,        String loopType,        String implementation,        String hibernateOnCreation,        String join,        String allowsAbortByPerformer        ArrayList<carnot_DataMappingType> carnot_datamappingtypes    ) {
        this.subProcessMode = subProcessMode;
        this.split = split;
        this.loopCondition = loopCondition;
        this.loopType = loopType;
        this.implementation = implementation;
        this.hibernateOnCreation = hibernateOnCreation;
        this.join = join;
        this.allowsAbortByPerformer = allowsAbortByPerformer;
        this.carnot_datamappingtypes = carnot_datamappingtypes;
    }

    public String getSubprocessmode() {
        return subProcessMode;
    }

    public void setSubprocessmode(String subProcessMode) {
        this.subProcessMode = subProcessMode;
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
    public String getImplementation() {
        return implementation;
    }

    public void setImplementation(String implementation) {
        this.implementation = implementation;
    }
    public String getHibernateoncreation() {
        return hibernateOnCreation;
    }

    public void setHibernateoncreation(String hibernateOnCreation) {
        this.hibernateOnCreation = hibernateOnCreation;
    }
    public String getJoin() {
        return join;
    }

    public void setJoin(String join) {
        this.join = join;
    }
    public String getAllowsabortbyperformer() {
        return allowsAbortByPerformer;
    }

    public void setAllowsabortbyperformer(String allowsAbortByPerformer) {
        this.allowsAbortByPerformer = allowsAbortByPerformer;
    }

    public List<carnot_DataMappingType> getCarnot_datamappingtypes() {
        return carnot_datamappingtypes;
    }

    public void addCarnot_datamappingtype(Carnot_datamappingtype carnot_datamappingtype) {
        this.carnot_datamappingtypes.add(carnot_datamappingtype);
    }

}