





import java.util.List;
import java.util.ArrayList;

public class carnot_IModelParticipant extends IIdentifiableModelElement {






    private List<carnot_ISwimlaneSymbol> carnot_iswimlanesymbols;




    private carnot_ISwimlaneSymbol carnot_iswimlanesymbol;




    private List<carnot_ActivityType> carnot_activitytypes;




    private carnot_ActivityType carnot_activitytype;




    private carnot_ISwimlaneSymbol carnot_iswimlanesymbol;




    private carnot_ActivityType carnot_activitytype;


    public carnot_IModelParticipant(
    ) {
        super(
        );
        this.carnot_iswimlanesymbols = new ArrayList<>();
        this.carnot_activitytypes = new ArrayList<>();
    }

    public carnot_IModelParticipant(
        ArrayList<carnot_ISwimlaneSymbol> carnot_iswimlanesymbols,        ArrayList<carnot_ActivityType> carnot_activitytypes    ) {
        this.carnot_iswimlanesymbols = carnot_iswimlanesymbols;
        this.carnot_activitytypes = carnot_activitytypes;
    }


    public List<carnot_ISwimlaneSymbol> getCarnot_iswimlanesymbols() {
        return carnot_iswimlanesymbols;
    }

    public void addCarnot_iswimlanesymbol(Carnot_iswimlanesymbol carnot_iswimlanesymbol) {
        this.carnot_iswimlanesymbols.add(carnot_iswimlanesymbol);
    }
    public carnot_ISwimlaneSymbol getCarnot_iswimlanesymbol() {
        return carnot_iswimlanesymbol;
    }

    public void setCarnot_iswimlanesymbol(carnot_ISwimlaneSymbol carnot_iswimlanesymbol) {
        this.carnot_iswimlanesymbol = carnot_iswimlanesymbol;
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
    public carnot_ISwimlaneSymbol getCarnot_iswimlanesymbol() {
        return carnot_iswimlanesymbol;
    }

    public void setCarnot_iswimlanesymbol(carnot_ISwimlaneSymbol carnot_iswimlanesymbol) {
        this.carnot_iswimlanesymbol = carnot_iswimlanesymbol;
    }
    public carnot_ActivityType getCarnot_activitytype() {
        return carnot_activitytype;
    }

    public void setCarnot_activitytype(carnot_ActivityType carnot_activitytype) {
        this.carnot_activitytype = carnot_activitytype;
    }

}