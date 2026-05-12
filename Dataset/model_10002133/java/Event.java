





import java.util.List;
import java.util.ArrayList;

public class Event  {

    private None Groups;
    private None Panels;
    private String Description;
    private None Resources;
    private int Id;
    private String Date;
    private String Name;



    public Event(
        None Groups,        None Panels,        String Description,        None Resources,        int Id,        String Date,        String Name    ) {
        this.Groups = Groups;
        this.Panels = Panels;
        this.Description = Description;
        this.Resources = Resources;
        this.Id = Id;
        this.Date = Date;
        this.Name = Name;
    }


    public None getGroups() {
        return Groups;
    }

    public void setGroups(None Groups) {
        this.Groups = Groups;
    }
    public None getPanels() {
        return Panels;
    }

    public void setPanels(None Panels) {
        this.Panels = Panels;
    }
    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }
    public None getResources() {
        return Resources;
    }

    public void setResources(None Resources) {
        this.Resources = Resources;
    }
    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
    }
    public String getDate() {
        return Date;
    }

    public void setDate(String Date) {
        this.Date = Date;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}