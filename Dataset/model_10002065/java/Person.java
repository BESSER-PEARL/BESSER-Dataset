





import java.util.List;
import java.util.ArrayList;

public class Person  {

    private String PhoneNum;
    private String Id;



    public Person(
        String PhoneNum,        String Id    ) {
        this.PhoneNum = PhoneNum;
        this.Id = Id;
    }


    public String getPhonenum() {
        return PhoneNum;
    }

    public void setPhonenum(String PhoneNum) {
        this.PhoneNum = PhoneNum;
    }
    public String getId() {
        return Id;
    }

    public void setId(String Id) {
        this.Id = Id;
    }


}