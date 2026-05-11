





import java.util.List;
import java.util.ArrayList;

public class ecvi_Veterinarian  {

    private String licenseIssueState;
    private String licenseNumber;
    private String nationalAccreditationNumber;





    private ecvi_Ecvi ecvi_ecvi;




    private ecvi_Address ecvi_address;




    private ecvi_Person ecvi_person;


    public ecvi_Veterinarian(
        String licenseIssueState,        String licenseNumber,        String nationalAccreditationNumber    ) {
        this.licenseIssueState = licenseIssueState;
        this.licenseNumber = licenseNumber;
        this.nationalAccreditationNumber = nationalAccreditationNumber;
    }


    public String getLicenseissuestate() {
        return licenseIssueState;
    }

    public void setLicenseissuestate(String licenseIssueState) {
        this.licenseIssueState = licenseIssueState;
    }
    public String getLicensenumber() {
        return licenseNumber;
    }

    public void setLicensenumber(String licenseNumber) {
        this.licenseNumber = licenseNumber;
    }
    public String getNationalaccreditationnumber() {
        return nationalAccreditationNumber;
    }

    public void setNationalaccreditationnumber(String nationalAccreditationNumber) {
        this.nationalAccreditationNumber = nationalAccreditationNumber;
    }

    public ecvi_Ecvi getEcvi_ecvi() {
        return ecvi_ecvi;
    }

    public void setEcvi_ecvi(ecvi_Ecvi ecvi_ecvi) {
        this.ecvi_ecvi = ecvi_ecvi;
    }
    public ecvi_Address getEcvi_address() {
        return ecvi_address;
    }

    public void setEcvi_address(ecvi_Address ecvi_address) {
        this.ecvi_address = ecvi_address;
    }
    public ecvi_Person getEcvi_person() {
        return ecvi_person;
    }

    public void setEcvi_person(ecvi_Person ecvi_person) {
        this.ecvi_person = ecvi_person;
    }

}