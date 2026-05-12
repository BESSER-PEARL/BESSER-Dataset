




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Administrator  {

    private int userId;
    private String name;
    private String address;
    private int phone;
    private LocalDate dateOfBirth;
    private String adminType;
    private String emailId;



    public Administrator(
        int userId,        String name,        String address,        int phone,        LocalDate dateOfBirth,        String adminType,        String emailId    ) {
        this.userId = userId;
        this.name = name;
        this.address = address;
        this.phone = phone;
        this.dateOfBirth = dateOfBirth;
        this.adminType = adminType;
        this.emailId = emailId;
    }


    public int getUserid() {
        return userId;
    }

    public void setUserid(int userId) {
        this.userId = userId;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public int getPhone() {
        return phone;
    }

    public void setPhone(int phone) {
        this.phone = phone;
    }
    public LocalDate getDateofbirth() {
        return dateOfBirth;
    }

    public void setDateofbirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }
    public String getAdmintype() {
        return adminType;
    }

    public void setAdmintype(String adminType) {
        this.adminType = adminType;
    }
    public String getEmailid() {
        return emailId;
    }

    public void setEmailid(String emailId) {
        this.emailId = emailId;
    }


}