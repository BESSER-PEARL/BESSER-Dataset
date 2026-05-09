





import java.util.List;
import java.util.ArrayList;

public class extlibraryprofile_Person extends Addressable {

    private String lastName;
    private String firstName;





    private extlibraryprofile_Class extlibraryprofile_class;


    public extlibraryprofile_Person(
        String lastName,        String firstName    ) {
        super(
        );
        this.lastName = lastName;
        this.firstName = firstName;
    }


    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }

    public extlibraryprofile_Class getExtlibraryprofile_class() {
        return extlibraryprofile_class;
    }

    public void setExtlibraryprofile_class(extlibraryprofile_Class extlibraryprofile_class) {
        this.extlibraryprofile_class = extlibraryprofile_class;
    }

}