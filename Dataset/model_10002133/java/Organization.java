





import java.util.List;
import java.util.ArrayList;

public class Organization  {

    private String Name;
    private String Description;
    private None Events;
    private None Owners;
    private String Url;
    private None Groups;
    private int Id;



    public Organization(
        String Name,        String Description,        None Events,        None Owners,        String Url,        None Groups,        int Id    ) {
        this.Name = Name;
        this.Description = Description;
        this.Events = Events;
        this.Owners = Owners;
        this.Url = Url;
        this.Groups = Groups;
        this.Id = Id;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }
    public None getEvents() {
        return Events;
    }

    public void setEvents(None Events) {
        this.Events = Events;
    }
    public None getOwners() {
        return Owners;
    }

    public void setOwners(None Owners) {
        this.Owners = Owners;
    }
    public String getUrl() {
        return Url;
    }

    public void setUrl(String Url) {
        this.Url = Url;
    }
    public None getGroups() {
        return Groups;
    }

    public void setGroups(None Groups) {
        this.Groups = Groups;
    }
    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
    }


}