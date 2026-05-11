





import java.util.List;
import java.util.ArrayList;

public class sipme_CompanyMember extends EnterpriseResource, Stakeholder {

    private int socialSecurityNumber;
    private String address;
    private String fullName;



    public sipme_CompanyMember(
        int socialSecurityNumber,        String address,        String fullName    ) {
        super(
        );
        this.socialSecurityNumber = socialSecurityNumber;
        this.address = address;
        this.fullName = fullName;
    }


    public int getSocialsecuritynumber() {
        return socialSecurityNumber;
    }

    public void setSocialsecuritynumber(int socialSecurityNumber) {
        this.socialSecurityNumber = socialSecurityNumber;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getFullname() {
        return fullName;
    }

    public void setFullname(String fullName) {
        this.fullName = fullName;
    }


}