





import java.util.List;
import java.util.ArrayList;

public class ClassDiagram_Hotel_Staff  {

    private String firstName;
    private String lastName;
    private String ssn;
    private String stafftype;





    private ClassDiagram_Company_Hotel classdiagram_company_hotel;


    public ClassDiagram_Hotel_Staff(
        String firstName,        String lastName,        String ssn,        String stafftype    ) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.ssn = ssn;
        this.stafftype = stafftype;
    }


    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
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
    public String getStafftype() {
        return stafftype;
    }

    public void setStafftype(String stafftype) {
        this.stafftype = stafftype;
    }

    public ClassDiagram_Company_Hotel getClassdiagram_company_hotel() {
        return classdiagram_company_hotel;
    }

    public void setClassdiagram_company_hotel(ClassDiagram_Company_Hotel classdiagram_company_hotel) {
        this.classdiagram_company_hotel = classdiagram_company_hotel;
    }

}