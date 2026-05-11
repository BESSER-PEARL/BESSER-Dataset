





import java.util.List;
import java.util.ArrayList;

public class carnot_ActivityType extends IdRefOwner, IIdentifiableModelElement, IEventHandlerOwner {

    private String implementation;
    private String subProcessMode;
    private String loopCondition;
    private String join;
    private String split;
    private String hibernateOnCreation;
    private String loopType;
    private String allowsAbortByPerformer;





    private List<carnot_DataMappingType> carnot_datamappingtypes;


    public carnot_ActivityType(
        String implementation,        String subProcessMode,        String loopCondition,        String join,        String split,        String hibernateOnCreation,        String loopType,        String allowsAbortByPerformer    ) {
        super(
        );
        this.implementation = implementation;
        this.subProcessMode = subProcessMode;
        this.loopCondition = loopCondition;
        this.join = join;
        this.split = split;
        this.hibernateOnCreation = hibernateOnCreation;
        this.loopType = loopType;
        this.allowsAbortByPerformer = allowsAbortByPerformer;
        this.carnot_datamappingtypes = new ArrayList<>();
    }

    public carnot_ActivityType(
        String implementation,        String subProcessMode,        String loopCondition,        String join,        String split,        String hibernateOnCreation,        String loopType,        String allowsAbortByPerformer        ArrayList<carnot_DataMappingType> carnot_datamappingtypes    ) {
        this.implementation = implementation;
        this.subProcessMode = subProcessMode;
        this.loopCondition = loopCondition;
        this.join = join;
        this.split = split;
        this.hibernateOnCreation = hibernateOnCreation;
        this.loopType = loopType;
        this.allowsAbortByPerformer = allowsAbortByPerformer;
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
    public String getLoopcondition() {
        return loopCondition;
    }

    public void setLoopcondition(String loopCondition) {
        this.loopCondition = loopCondition;
    }
    public String getJoin() {
        return join;
    }

    public void setJoin(String join) {
        this.join = join;
    }
    public String getSplit() {
        return split;
    }

    public void setSplit(String split) {
        this.split = split;
    }
    public String getHibernateoncreation() {
        return hibernateOnCreation;
    }

    public void setHibernateoncreation(String hibernateOnCreation) {
        this.hibernateOnCreation = hibernateOnCreation;
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

    public List<carnot_DataMappingType> getCarnot_datamappingtypes() {
        return carnot_datamappingtypes;
    }

    public void addCarnot_datamappingtype(Carnot_datamappingtype carnot_datamappingtype) {
        this.carnot_datamappingtypes.add(carnot_datamappingtype);
    }

}