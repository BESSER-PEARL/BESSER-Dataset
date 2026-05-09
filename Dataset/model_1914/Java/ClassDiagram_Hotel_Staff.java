





import java.util.List;
import java.util.ArrayList;

public class ClassDiagram_Hotel_Staff  {

    private String lastName;
    private String ssn;
    private String hasWorkTitel;
    private String firstName;





    private ClassDiagram_Company_Hotel classdiagram_company_hotel;


    public ClassDiagram_Hotel_Staff(
        String lastName,        String ssn,        String hasWorkTitel,        String firstName    ) {
        this.lastName = lastName;
        this.ssn = ssn;
        this.hasWorkTitel = hasWorkTitel;
        this.firstName = firstName;
    }


    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getSsn() {
        return ssn;
    }

    public void setSsn(String ssn) {
        this.ssn = ssn;
    }
    public String getHasworktitel() {
        return hasWorkTitel;
    }

    public void setHasworktitel(String hasWorkTitel) {
        this.hasWorkTitel = hasWorkTitel;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }

    public ClassDiagram_Company_Hotel getClassdiagram_company_hotel() {
        return classdiagram_company_hotel;
    }

    public void setClassdiagram_company_hotel(ClassDiagram_Company_Hotel classdiagram_company_hotel) {
        this.classdiagram_company_hotel = classdiagram_company_hotel;
    }

}