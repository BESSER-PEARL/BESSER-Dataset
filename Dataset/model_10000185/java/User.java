





import java.util.List;
import java.util.ArrayList;

public class User  {

    private int Phone_number;
    private String Name_;
    private String Address_;
    private int Phone_number1;
    private String Email_;



    public User(
        int Phone_number,        String Name_,        String Address_,        int Phone_number1,        String Email_    ) {
        this.Phone_number = Phone_number;
        this.Name_ = Name_;
        this.Address_ = Address_;
        this.Phone_number1 = Phone_number1;
        this.Email_ = Email_;
    }


    public int getPhone_number() {
        return Phone_number;
    }

    public void setPhone_number(int Phone_number) {
        this.Phone_number = Phone_number;
    }
    public String getName_() {
        return Name_;
    }

    public void setName_(String Name_) {
        this.Name_ = Name_;
    }
    public String getAddress_() {
        return Address_;
    }

    public void setAddress_(String Address_) {
        this.Address_ = Address_;
    }
    public int getPhone_number1() {
        return Phone_number1;
    }

    public void setPhone_number1(int Phone_number1) {
        this.Phone_number1 = Phone_number1;
    }
    public String getEmail_() {
        return Email_;
    }

    public void setEmail_(String Email_) {
        this.Email_ = Email_;
    }


}