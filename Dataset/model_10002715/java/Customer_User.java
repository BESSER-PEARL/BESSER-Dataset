





import java.util.List;
import java.util.ArrayList;

public class Customer_User  {

    private String userid__;
    private String Addresschange__;



    public Customer_User(
        String userid__,        String Addresschange__    ) {
        this.userid__ = userid__;
        this.Addresschange__ = Addresschange__;
    }


    public String getUserid__() {
        return userid__;
    }

    public void setUserid__(String userid__) {
        this.userid__ = userid__;
    }
    public String getAddresschange__() {
        return Addresschange__;
    }

    public void setAddresschange__(String Addresschange__) {
        this.Addresschange__ = Addresschange__;
    }


}