




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String name;
    private LocalDate dateOfBirth;
    private String address;
    private String emailAddress;
    private String phoneNumber;





    private List<Native_App_Activity___ViewController___WmMediaPagerEvents> native_app_activity___viewcontroller___wmmediapagereventss;


    public Customer(
        String name,        LocalDate dateOfBirth,        String address,        String emailAddress,        String phoneNumber    ) {
        this.name = name;
        this.dateOfBirth = dateOfBirth;
        this.address = address;
        this.emailAddress = emailAddress;
        this.phoneNumber = phoneNumber;
        this.native_app_activity___viewcontroller___wmmediapagereventss = new ArrayList<>();
    }

    public Customer(
        String name,        LocalDate dateOfBirth,        String address,        String emailAddress,        String phoneNumber        ArrayList<Native_App_Activity___ViewController___WmMediaPagerEvents> native_app_activity___viewcontroller___wmmediapagereventss    ) {
        this.name = name;
        this.dateOfBirth = dateOfBirth;
        this.address = address;
        this.emailAddress = emailAddress;
        this.phoneNumber = phoneNumber;
        this.native_app_activity___viewcontroller___wmmediapagereventss = native_app_activity___viewcontroller___wmmediapagereventss;
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
    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public List<Native_App_Activity___ViewController___WmMediaPagerEvents> getNative_app_activity___viewcontroller___wmmediapagereventss() {
        return native_app_activity___viewcontroller___wmmediapagereventss;
    }

    public void addNative_app_activity___viewcontroller___wmmediapagerevents(Native_app_activity___viewcontroller___wmmediapagerevents native_app_activity___viewcontroller___wmmediapagerevents) {
        this.native_app_activity___viewcontroller___wmmediapagereventss.add(native_app_activity___viewcontroller___wmmediapagerevents);
    }

}