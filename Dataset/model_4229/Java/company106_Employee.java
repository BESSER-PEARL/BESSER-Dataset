





import java.util.List;
import java.util.ArrayList;

public class company106_Employee  {

    private String fullName;
    private int address;
    private String socialSecurityNumber;





    private company106_Workstation company106_workstation;




    private company106_Workstation company106_workstation;




    private company106_Room company106_room;


    public company106_Employee(
        String fullName,        int address,        String socialSecurityNumber    ) {
        this.fullName = fullName;
        this.address = address;
        this.socialSecurityNumber = socialSecurityNumber;
    }


    public String getFullname() {
        return fullName;
    }

    public void setFullname(String fullName) {
        this.fullName = fullName;
    }
    public int getAddress() {
        return address;
    }

    public void setAddress(int address) {
        this.address = address;
    }
    public String getSocialsecuritynumber() {
        return socialSecurityNumber;
    }

    public void setSocialsecuritynumber(String socialSecurityNumber) {
        this.socialSecurityNumber = socialSecurityNumber;
    }

    public company106_Workstation getCompany106_workstation() {
        return company106_workstation;
    }

    public void setCompany106_workstation(company106_Workstation company106_workstation) {
        this.company106_workstation = company106_workstation;
    }
    public company106_Workstation getCompany106_workstation() {
        return company106_workstation;
    }

    public void setCompany106_workstation(company106_Workstation company106_workstation) {
        this.company106_workstation = company106_workstation;
    }
    public company106_Room getCompany106_room() {
        return company106_room;
    }

    public void setCompany106_room(company106_Room company106_room) {
        this.company106_room = company106_room;
    }

}