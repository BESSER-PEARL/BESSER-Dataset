





import java.util.List;
import java.util.ArrayList;

public class ORDB4ORA_Trigger  {

    private String Event;
    private String Body;
    private String Action;
    private String Name;





    private ORDB4ORA_Table ordb4ora_table;




    private List<ORDB4ORA_StructuralComponent> ordb4ora_structuralcomponents;




    private ORDB4ORA_Table ordb4ora_table;


    public ORDB4ORA_Trigger(
        String Event,        String Body,        String Action,        String Name    ) {
        this.Event = Event;
        this.Body = Body;
        this.Action = Action;
        this.Name = Name;
        this.ordb4ora_structuralcomponents = new ArrayList<>();
    }

    public ORDB4ORA_Trigger(
        String Event,        String Body,        String Action,        String Name        ArrayList<ORDB4ORA_StructuralComponent> ordb4ora_structuralcomponents    ) {
        this.Event = Event;
        this.Body = Body;
        this.Action = Action;
        this.Name = Name;
        this.ordb4ora_structuralcomponents = ordb4ora_structuralcomponents;
    }

    public String getEvent() {
        return Event;
    }

    public void setEvent(String Event) {
        this.Event = Event;
    }
    public String getBody() {
        return Body;
    }

    public void setBody(String Body) {
        this.Body = Body;
    }
    public String getAction() {
        return Action;
    }

    public void setAction(String Action) {
        this.Action = Action;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
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