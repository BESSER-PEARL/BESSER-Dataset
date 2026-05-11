





import java.util.List;
import java.util.ArrayList;

public class company104_Employee  {

    private int address;
    private String socialSecurityNumber;
    private String fullName;





    private company104_Agency company104_agency;




    private company104_Workstation company104_workstation;




    private company104_Workstation company104_workstation;




    private company104_Room company104_room;


    public company104_Employee(
        int address,        String socialSecurityNumber,        String fullName    ) {
        this.address = address;
        this.socialSecurityNumber = socialSecurityNumber;
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
    public String getFullname() {
        return fullName;
    }

    public void setFullname(String fullName) {
        this.fullName = fullName;
    }

    public company104_Agency getCompany104_agency() {
        return company104_agency;
    }

    public void setCompany104_agency(company104_Agency company104_agency) {
        this.company104_agency = company104_agency;
    }
    public company104_Workstation getCompany104_workstation() {
        return company104_workstation;
    }

    public void setCompany104_workstation(company104_Workstation company104_workstation) {
        this.company104_workstation = company104_workstation;
    }
    public company104_Workstation getCompany104_workstation() {
        return company104_workstation;
    }

    public void setCompany104_workstation(company104_Workstation company104_workstation) {
        this.company104_workstation = company104_workstation;
    }
    public company104_Room getCompany104_room() {
        return company104_room;
    }

    public void setCompany104_room(company104_Room company104_room) {
        this.company104_room = company104_room;
    }

}