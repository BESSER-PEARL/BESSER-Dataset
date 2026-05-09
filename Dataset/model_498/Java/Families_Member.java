





import java.util.List;
import java.util.ArrayList;

public class Families_Member extends LastNameElement {

    private String firstName;



    public Families_Member(
        String firstName    ) {
        super(
        );
        this.firstName = firstName;
    }


    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }


}