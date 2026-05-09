





import java.util.List;
import java.util.ArrayList;

public class ClassDiagram_Company_GuestRecord  {

    private String adress;
    private String ssn;
    private String payment;
    private String phoneNumber;
    private String name;





    private ClassDiagram_Company classdiagram_company;


    public ClassDiagram_Company_GuestRecord(
        String adress,        String ssn,        String payment,        String phoneNumber,        String name    ) {
        this.adress = adress;
        this.ssn = ssn;
        this.payment = payment;
        this.phoneNumber = phoneNumber;
        this.name = name;
    }


    public String getAdress() {
        return adress;
    }

    public void setAdress(String adress) {
        this.adress = adress;
    }
    public String getSsn() {
        return ssn;
    }

    public void setSsn(String ssn) {
        this.ssn = ssn;
    }
    public String getPayment() {
        return payment;
    }

    public void setPayment(String payment) {
        this.payment = payment;
    }
    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ClassDiagram_Company getClassdiagram_company() {
        return classdiagram_company;
    }

    public void setClassdiagram_company(ClassDiagram_Company classdiagram_company) {
        this.classdiagram_company = classdiagram_company;
    }

}