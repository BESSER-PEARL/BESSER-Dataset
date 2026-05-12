





import java.util.List;
import java.util.ArrayList;

public class Resource  {

    private int NumberAvailable;
    private boolean Private;
    private None Type;
    private String Description;
    private String Name;
    private int Id;



    public Resource(
        int NumberAvailable,        boolean Private,        None Type,        String Description,        String Name,        int Id    ) {
        this.NumberAvailable = NumberAvailable;
        this.Private = Private;
        this.Type = Type;
        this.Description = Description;
        this.Name = Name;
        this.Id = Id;
    }


    public int getNumberavailable() {
        return NumberAvailable;
    }

    public void setNumberavailable(int NumberAvailable) {
        this.NumberAvailable = NumberAvailable;
    }
    public boolean getPrivate() {
        return Private;
    }

    public void setPrivate(boolean Private) {
        this.Private = Private;
    }
    public None getType() {
        return Type;
    }

    public void setType(None Type) {
        this.Type = Type;
    }
    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
    }


}