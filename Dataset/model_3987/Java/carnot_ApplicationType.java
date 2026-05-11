





import java.util.List;
import java.util.ArrayList;

public class carnot_ApplicationType extends IIdentifiableModelElement, ITypedElement, IAccessPointOwner {

    private String interactive;





    private List<carnot_ContextType> carnot_contexttypes;




    private carnot_ModelType carnot_modeltype;




    private carnot_ActivityType carnot_activitytype;




    private List<carnot_ActivityType> carnot_activitytypes;


    public carnot_ApplicationType(
        String interactive    ) {
        super(
        );
        this.interactive = interactive;
        this.carnot_contexttypes = new ArrayList<>();
        this.carnot_activitytypes = new ArrayList<>();
    }

    public carnot_ApplicationType(
        String interactive        ArrayList<carnot_ContextType> carnot_contexttypes,        ArrayList<carnot_ActivityType> carnot_activitytypes    ) {
        this.interactive = interactive;
        this.carnot_contexttypes = carnot_contexttypes;
        this.carnot_activitytypes = carnot_activitytypes;
    }

    public String getInteractive() {
        return interactive;
    }

    public void setInteractive(String interactive) {
        this.interactive = interactive;
    }

    public List<carnot_ContextType> getCarnot_contexttypes() {
        return carnot_contexttypes;
    }

    public void addCarnot_contexttype(Carnot_contexttype carnot_contexttype) {
        this.carnot_contexttypes.add(carnot_contexttype);
    }
    public carnot_ModelType getCarnot_modeltype() {
        return carnot_modeltype;
    }

    public void setCarnot_modeltype(carnot_ModelType carnot_modeltype) {
        this.carnot_modeltype = carnot_modeltype;
    }
    public carnot_ActivityType getCarnot_activitytype() {
        return carnot_activitytype;
    }

    public void setCarnot_activitytype(carnot_ActivityType carnot_activitytype) {
        this.carnot_activitytype = carnot_activitytype;
    }
    public List<carnot_ActivityType> getCarnot_activitytypes() {
        return carnot_activitytypes;
    }

    public void addCarnot_activitytype(Carnot_activitytype carnot_activitytype) {
        this.carnot_activitytypes.add(carnot_activitytype);
    }

}