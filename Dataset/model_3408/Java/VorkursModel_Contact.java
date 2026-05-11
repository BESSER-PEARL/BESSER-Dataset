





import java.util.List;
import java.util.ArrayList;

public class VorkursModel_Contact  {

    private String Email;
    private String phonenumber;





    private VorkursModel_Person vorkursmodel_person;


    public VorkursModel_Contact(
        String Email,        String phonenumber    ) {
        this.Email = Email;
        this.phonenumber = phonenumber;
    }


    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getPhonenumber() {
        return phonenumber;
    }

    public void setPhonenumber(String phonenumber) {
        this.phonenumber = phonenumber;
    }

    public VorkursModel_Person getVorkursmodel_person() {
        return vorkursmodel_person;
    }

    public void setVorkursmodel_person(VorkursModel_Person vorkursmodel_person) {
        this.vorkursmodel_person = vorkursmodel_person;
    }

}