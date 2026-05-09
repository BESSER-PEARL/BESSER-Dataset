





import java.util.List;
import java.util.ArrayList;

public class ClassDiagram_Company_GuestRecord  {

    private String ssn;
    private String phoneNumber;
    private String adress;
    private String name;
    private String paymentInformation;





    private ClassDiagram_Company classdiagram_company;


    public ClassDiagram_Company_GuestRecord(
        String ssn,        String phoneNumber,        String adress,        String name,        String paymentInformation    ) {
        this.ssn = ssn;
        this.phoneNumber = phoneNumber;
        this.adress = adress;
        this.name = name;
        this.paymentInformation = paymentInformation;
    }


    public String getSsn() {
        return ssn;
    }

    public void setSsn(String ssn) {
        this.ssn = ssn;
    }
    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public String getAdress() {
        return adress;
    }

    public void setAdress(String adress) {
        this.adress = adress;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPaymentinformation() {
        return paymentInformation;
    }

    public void setPaymentinformation(String paymentInformation) {
        this.paymentInformation = paymentInformation;
    }

    public ClassDiagram_Company getClassdiagram_company() {
        return classdiagram_company;
    }

    public void setClassdiagram_company(ClassDiagram_Company classdiagram_company) {
        this.classdiagram_company = classdiagram_company;
    }

}