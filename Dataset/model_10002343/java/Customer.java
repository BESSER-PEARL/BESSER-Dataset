





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String Gender;
    private float cellNo;
    private String name;
    private String emailAddress;
    private String DOB;





    private Account account;


    public Customer(
        String Gender,        float cellNo,        String name,        String emailAddress,        String DOB    ) {
        this.Gender = Gender;
        this.cellNo = cellNo;
        this.name = name;
        this.emailAddress = emailAddress;
        this.DOB = DOB;
    }


    public String getGender() {
        return Gender;
    }

    public void setGender(String Gender) {
        this.Gender = Gender;
    }
    public float getCellno() {
        return cellNo;
    }

    public void setCellno(float cellNo) {
        this.cellNo = cellNo;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getEmailaddress() {
        return emailAddress;
    }

    public void setEmailaddress(String emailAddress) {
        this.emailAddress = emailAddress;
    }
    public String getDob() {
        return DOB;
    }

    public void setDob(String DOB) {
        this.DOB = DOB;
    }

    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }

}