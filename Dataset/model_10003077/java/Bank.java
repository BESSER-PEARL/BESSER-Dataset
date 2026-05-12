





import java.util.List;
import java.util.ArrayList;

public class Bank  {

    private String Name;
    private String Code;



    public Bank(
        String Name,        String Code    ) {
        this.Name = Name;
        this.Code = Code;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getCode() {
        return Code;
    }

    public void setCode(String Code) {
        this.Code = Code;
    }


}