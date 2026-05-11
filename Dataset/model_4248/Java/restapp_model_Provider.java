





import java.util.List;
import java.util.ArrayList;

public class restapp_model_Provider  {

    private String Address;
    private String CNPJ;
    private String contact;
    private String name;
    private String phone;
    private int id;



    public restapp_model_Provider(
        String Address,        String CNPJ,        String contact,        String name,        String phone,        int id    ) {
        this.Address = Address;
        this.CNPJ = CNPJ;
        this.contact = contact;
        this.name = name;
        this.phone = phone;
        this.id = id;
    }


    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getCnpj() {
        return CNPJ;
    }

    public void setCnpj(String CNPJ) {
        this.CNPJ = CNPJ;
    }
    public String getContact() {
        return contact;
    }

    public void setContact(String contact) {
        this.contact = contact;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}