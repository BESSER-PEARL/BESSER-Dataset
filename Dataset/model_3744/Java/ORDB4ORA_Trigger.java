





import java.util.List;
import java.util.ArrayList;

public class ORDB4ORA_Trigger  {

    private String Body;
    private String Event;
    private String Name;
    private String Action;





    private ORDB4ORA_Table ordb4ora_table;




    private List<ORDB4ORA_StructuralComponent> ordb4ora_structuralcomponents;




    private ORDB4ORA_Table ordb4ora_table;


    public ORDB4ORA_Trigger(
        String Body,        String Event,        String Name,        String Action    ) {
        this.Body = Body;
        this.Event = Event;
        this.Name = Name;
        this.Action = Action;
        this.ordb4ora_structuralcomponents = new ArrayList<>();
    }

    public ORDB4ORA_Trigger(
        String Body,        String Event,        String Name,        String Action        ArrayList<ORDB4ORA_StructuralComponent> ordb4ora_structuralcomponents    ) {
        this.Body = Body;
        this.Event = Event;
        this.Name = Name;
        this.Action = Action;
        this.ordb4ora_structuralcomponents = ordb4ora_structuralcomponents;
    }

    public String getBody() {
        return Body;
    }

    public void setBody(String Body) {
        this.Body = Body;
    }
    public String getEvent() {
        return Event;
    }

    public void setEvent(String Event) {
        this.Event = Event;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getAction() {
        return Action;
    }

    public void setAction(String Action) {
        this.Action = Action;
    }

    public ORDB4ORA_Table getOrdb4ora_table() {
        return ordb4ora_table;
    }

    public void setOrdb4ora_table(ORDB4ORA_Table ordb4ora_table) {
        this.ordb4ora_table = ordb4ora_table;
    }
    public List<ORDB4ORA_StructuralComponent> getOrdb4ora_structuralcomponents() {
        return ordb4ora_structuralcomponents;
    }

    public void addOrdb4ora_structuralcomponent(Ordb4ora_structuralcomponent ordb4ora_structuralcomponent) {
        this.ordb4ora_structuralcomponents.add(ordb4ora_structuralcomponent);
    }
    public ORDB4ORA_Table getOrdb4ora_table() {
        return ordb4ora_table;
    }

    public void setOrdb4ora_table(ORDB4ORA_Table ordb4ora_table) {
        this.ordb4ora_table = ordb4ora_table;
    }

}