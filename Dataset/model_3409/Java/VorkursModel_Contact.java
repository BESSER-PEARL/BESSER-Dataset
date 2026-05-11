





import java.util.List;
import java.util.ArrayList;

public class VorkursModel_Contact  {

    private String phonenumber;
    private String Email;





    private VorkursModel_Person vorkursmodel_person;




    private VorkursModel_Address vorkursmodel_address;


    public VorkursModel_Contact(
        String phonenumber,        String Email    ) {
        this.phonenumber = phonenumber;
        this.Email = Email;
    }


    public String getPhonenumber() {
        return phonenumber;
    }

    public void setPhonenumber(String phonenumber) {
        this.phonenumber = phonenumber;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }

    public VorkursModel_Person getVorkursmodel_person() {
        return vorkursmodel_person;
    }

    public void setVorkursmodel_person(VorkursModel_Person vorkursmodel_person) {
        this.vorkursmodel_person = vorkursmodel_person;
    }
    public VorkursModel_Address getVorkursmodel_address() {
        return vorkursmodel_address;
    }

    public void setVorkursmodel_address(VorkursModel_Address vorkursmodel_address) {
        this.vorkursmodel_address = vorkursmodel_address;
    }

}