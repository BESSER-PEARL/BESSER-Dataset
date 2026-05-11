





import java.util.List;
import java.util.ArrayList;

public class bank_MobilePhone extends Device {

    private String key;
    private String number;



    public bank_MobilePhone(
        String key,        String number    ) {
        super(
        );
        this.key = key;
        this.number = number;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }


}