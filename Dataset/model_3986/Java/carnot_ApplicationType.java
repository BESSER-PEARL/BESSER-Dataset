





import java.util.List;
import java.util.ArrayList;

public class carnot_ApplicationType extends ITypedElement, IIdentifiableModelElement, IAccessPointOwner {

    private String interactive;





    private List<carnot_ContextType> carnot_contexttypes;




    private carnot_ModelType carnot_modeltype;




    private carnot_ApplicationSymbolType carnot_applicationsymboltype;




    private List<carnot_ActivityType> carnot_activitytypes;




    private carnot_ActivityType carnot_activitytype;




    private List<carnot_ApplicationSymbolType> carnot_applicationsymboltypes;


    public carnot_ApplicationType(
        String interactive    ) {
        super(
        );
        this.interactive = interactive;
        this.carnot_contexttypes = new ArrayList<>();
        this.carnot_activitytypes = new ArrayList<>();
        this.carnot_applicationsymboltypes = new ArrayList<>();
    }

    public carnot_ApplicationType(
        String interactive        ArrayList<carnot_ContextType> carnot_contexttypes,        ArrayList<carnot_ActivityType> carnot_activitytypes,        ArrayList<carnot_ApplicationSymbolType> carnot_applicationsymboltypes    ) {
        this.interactive = interactive;
        this.carnot_contexttypes = carnot_contexttypes;
        this.carnot_activitytypes = carnot_activitytypes;
        this.carnot_applicationsymboltypes = carnot_applicationsymboltypes;
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
    public carnot_ApplicationSymbolType getCarnot_applicationsymboltype() {
        return carnot_applicationsymboltype;
    }

    public void setCarnot_applicationsymboltype(carnot_ApplicationSymbolType carnot_applicationsymboltype) {
        this.carnot_applicationsymboltype = carnot_applicationsymboltype;
    }
    public List<carnot_ActivityType> getCarnot_activitytypes() {
        return carnot_activitytypes;
    }

    public void addCarnot_activitytype(Carnot_activitytype carnot_activitytype) {
        this.carnot_activitytypes.add(carnot_activitytype);
    }
    public carnot_ActivityType getCarnot_activitytype() {
        return carnot_activitytype;
    }

    public void setCarnot_activitytype(carnot_ActivityType carnot_activitytype) {
        this.carnot_activitytype = carnot_activitytype;
    }
    public List<carnot_ApplicationSymbolType> getCarnot_applicationsymboltypes() {
        return carnot_applicationsymboltypes;
    }

    public void addCarnot_applicationsymboltype(Carnot_applicationsymboltype carnot_applicationsymboltype) {
        this.carnot_applicationsymboltypes.add(carnot_applicationsymboltype);
    }

}