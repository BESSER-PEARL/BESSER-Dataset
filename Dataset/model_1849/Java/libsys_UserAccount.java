




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class libsys_UserAccount  {

    private String telephoneNumber;
    private String emailAddress;
    private String userClassification;
    private String userData;
    private String postallAddress;
    private LocalDate validUntilDate;
    private boolean lockIndication;
    private int unpaidFeeAmount;
    private String userName;
    private int userNumber;





    private List<libsys_Instance> libsys_instances;




    private libsys_User libsys_user;




    private libsys_UserAdministration libsys_useradministration;




    private List<libsys_Instance> libsys_instances;


    public libsys_UserAccount(
        String telephoneNumber,        String emailAddress,        String userClassification,        String userData,        String postallAddress,        LocalDate validUntilDate,        boolean lockIndication,        int unpaidFeeAmount,        String userName,        int userNumber    ) {
        this.telephoneNumber = telephoneNumber;
        this.emailAddress = emailAddress;
        this.userClassification = userClassification;
        this.userData = userData;
        this.postallAddress = postallAddress;
        this.validUntilDate = validUntilDate;
        this.lockIndication = lockIndication;
        this.unpaidFeeAmount = unpaidFeeAmount;
        this.userName = userName;
        this.userNumber = userNumber;
        this.libsys_instances = new ArrayList<>();
        this.libsys_instances = new ArrayList<>();
    }

    public libsys_UserAccount(
        String telephoneNumber,        String emailAddress,        String userClassification,        String userData,        String postallAddress,        LocalDate validUntilDate,        boolean lockIndication,        int unpaidFeeAmount,        String userName,        int userNumber        ArrayList<libsys_Instance> libsys_instances,        ArrayList<libsys_Instance> libsys_instances    ) {
        this.telephoneNumber = telephoneNumber;
        this.emailAddress = emailAddress;
        this.userClassification = userClassification;
        this.userData = userData;
        this.postallAddress = postallAddress;
        this.validUntilDate = validUntilDate;
        this.lockIndication = lockIndication;
        this.unpaidFeeAmount = unpaidFeeAmount;
        this.userName = userName;
        this.userNumber = userNumber;
        this.libsys_instances = libsys_instances;
        this.libsys_instances = libsys_instances;
    }

    public String getTelephonenumber() {
        return telephoneNumber;
    }

    public void setTelephonenumber(String telephoneNumber) {
        this.telephoneNumber = telephoneNumber;
    }
    public String getEmailaddress() {
        return emailAddress;
    }

    public void setEmailaddress(String emailAddress) {
        this.emailAddress = emailAddress;
    }
    public String getUserclassification() {
        return userClassification;
    }

    public void setUserclassification(String userClassification) {
        this.userClassification = userClassification;
    }
    public String getUserdata() {
        return userData;
    }

    public void setUserdata(String userData) {
        this.userData = userData;
    }
    public String getPostalladdress() {
        return postallAddress;
    }

    public void setPostalladdress(String postallAddress) {
        this.postallAddress = postallAddress;
    }
    public LocalDate getValiduntildate() {
        return validUntilDate;
    }

    public void setValiduntildate(LocalDate validUntilDate) {
        this.validUntilDate = validUntilDate;
    }
    public boolean getLockindication() {
        return lockIndication;
    }

    public void setLockindication(boolean lockIndication) {
        this.lockIndication = lockIndication;
    }
    public int getUnpaidfeeamount() {
        return unpaidFeeAmount;
    }

    public void setUnpaidfeeamount(int unpaidFeeAmount) {
        this.unpaidFeeAmount = unpaidFeeAmount;
    }
    public String getUsername() {
        return userName;
    }

    public void setUsername(String userName) {
        this.userName = userName;
    }
    public int getUsernumber() {
        return userNumber;
    }

    public void setUsernumber(int userNumber) {
        this.userNumber = userNumber;
    }

    public List<libsys_Instance> getLibsys_instances() {
        return libsys_instances;
    }

    public void addLibsys_instance(Libsys_instance libsys_instance) {
        this.libsys_instances.add(libsys_instance);
    }
    public libsys_User getLibsys_user() {
        return libsys_user;
    }

    public void setLibsys_user(libsys_User libsys_user) {
        this.libsys_user = libsys_user;
    }
    public libsys_UserAdministration getLibsys_useradministration() {
        return libsys_useradministration;
    }

    public void setLibsys_useradministration(libsys_UserAdministration libsys_useradministration) {
        this.libsys_useradministration = libsys_useradministration;
    }
    public List<libsys_Instance> getLibsys_instances() {
        return libsys_instances;
    }

    public void addLibsys_instance(Libsys_instance libsys_instance) {
        this.libsys_instances.add(libsys_instance);
    }

}