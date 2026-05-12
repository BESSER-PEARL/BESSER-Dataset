





import java.util.List;
import java.util.ArrayList;

public class Store  {

    private String Name;
    private String Address;





    private Register register;


    public Store(
        String Name,        String Address    ) {
        this.Name = Name;
        this.Address = Address;
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

    public Register getRegister() {
        return register;
    }

    public void setRegister(Register register) {
        this.register = register;
    }

}