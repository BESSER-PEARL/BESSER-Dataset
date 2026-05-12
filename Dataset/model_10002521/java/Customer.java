





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String address;
    private String loginName;
    private int mobileNo;



    public Customer(
        String address,        String loginName,        int mobileNo    ) {
        this.address = address;
        this.loginName = loginName;
        this.mobileNo = mobileNo;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getLoginname() {
        return loginName;
    }

    public void setLoginname(String loginName) {
        this.loginName = loginName;
    }
    public int getMobileno() {
        return mobileNo;
    }

    public void setMobileno(int mobileNo) {
        this.mobileNo = mobileNo;
    }


}