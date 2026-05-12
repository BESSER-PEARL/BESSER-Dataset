




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String name;
    private LocalDate dateOfBirth;
    private String address;
    private String emailAddress;
    private String GP_Address;
    private String phoneNumber;





    private List<Medical_Record_NHS_Number> medical_record_nhs_numbers;


    public Patient(
        String name,        LocalDate dateOfBirth,        String address,        String emailAddress,        String GP_Address,        String phoneNumber    ) {
        this.name = name;
        this.dateOfBirth = dateOfBirth;
        this.address = address;
        this.emailAddress = emailAddress;
        this.GP_Address = GP_Address;
        this.phoneNumber = phoneNumber;
        this.medical_record_nhs_numbers = new ArrayList<>();
    }

    public Patient(
        String name,        LocalDate dateOfBirth,        String address,        String emailAddress,        String GP_Address,        String phoneNumber        ArrayList<Medical_Record_NHS_Number> medical_record_nhs_numbers    ) {
        this.name = name;
        this.dateOfBirth = dateOfBirth;
        this.address = address;
        this.emailAddress = emailAddress;
        this.GP_Address = GP_Address;
        this.phoneNumber = phoneNumber;
        this.medical_record_nhs_numbers = medical_record_nhs_numbers;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public LocalDate getDateofbirth() {
        return dateOfBirth;
    }

    public void setDateofbirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getEmailaddress() {
        return emailAddress;
    }

    public void setEmailaddress(String emailAddress) {
        this.emailAddress = emailAddress;
    }
    public String getGp_address() {
        return GP_Address;
    }

    public void setGp_address(String GP_Address) {
        this.GP_Address = GP_Address;
    }
    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public List<Medical_Record_NHS_Number> getMedical_record_nhs_numbers() {
        return medical_record_nhs_numbers;
    }

    public void addMedical_record_nhs_number(Medical_record_nhs_number medical_record_nhs_number) {
        this.medical_record_nhs_numbers.add(medical_record_nhs_number);
    }

}