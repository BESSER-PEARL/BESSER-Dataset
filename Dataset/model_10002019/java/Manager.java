





import java.util.List;
import java.util.ArrayList;

public class Manager  {

    private None Phn_no_;
    private int ID;
    private String Name;
    private String Address;



    public Manager(
        None Phn_no_,        int ID,        String Name,        String Address    ) {
        this.Phn_no_ = Phn_no_;
        this.ID = ID;
        this.Name = Name;
        this.Address = Address;
    }


    public None getPhn_no_() {
        return Phn_no_;
    }

    public void setPhn_no_(None Phn_no_) {
        this.Phn_no_ = Phn_no_;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }


}