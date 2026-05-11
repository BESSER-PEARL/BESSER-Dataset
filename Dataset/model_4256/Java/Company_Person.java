





import java.util.List;
import java.util.ArrayList;

public class Company_Person  {

    private String fullName;
    private String position;



    public Company_Person(
        String fullName,        String position    ) {
        this.fullName = fullName;
        this.position = position;
    }


    public String getFullname() {
        return fullName;
    }

    public void setFullname(String fullName) {
        this.fullName = fullName;
    }
    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }


}