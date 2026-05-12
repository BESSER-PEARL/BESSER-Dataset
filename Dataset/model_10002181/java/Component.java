





import java.util.List;
import java.util.ArrayList;

public class Component  {

    private String Name;
    private String Storage_or_sehlf;
    private String ID;
    private String Type;
    private String attribute;
    private String Expiry_date;



    public Component(
        String Name,        String Storage_or_sehlf,        String ID,        String Type,        String attribute,        String Expiry_date    ) {
        this.Name = Name;
        this.Storage_or_sehlf = Storage_or_sehlf;
        this.ID = ID;
        this.Type = Type;
        this.attribute = attribute;
        this.Expiry_date = Expiry_date;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getStorage_or_sehlf() {
        return Storage_or_sehlf;
    }

    public void setStorage_or_sehlf(String Storage_or_sehlf) {
        this.Storage_or_sehlf = Storage_or_sehlf;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getExpiry_date() {
        return Expiry_date;
    }

    public void setExpiry_date(String Expiry_date) {
        this.Expiry_date = Expiry_date;
    }


}