





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String emailAddress;
    private float cellNo;
    private String name;
    private String Gender;
    private String DOB;





    private Account account;


    public Customer(
        String emailAddress,        float cellNo,        String name,        String Gender,        String DOB    ) {
        this.emailAddress = emailAddress;
        this.cellNo = cellNo;
        this.name = name;
        this.Gender = Gender;
        this.DOB = DOB;
    }


    public String getEmailaddress() {
        return emailAddress;
    }

    public void setEmailaddress(String emailAddress) {
        this.emailAddress = emailAddress;
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
    public String getGender() {
        return Gender;
    }

    public void setGender(String Gender) {
        this.Gender = Gender;
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