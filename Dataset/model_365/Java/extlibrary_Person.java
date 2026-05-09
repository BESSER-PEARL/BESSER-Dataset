





import java.util.List;
import java.util.ArrayList;

public class extlibrary_Person extends Addressable {

    private String lastName;
    private String firstName;





    private extlibrary_VideoCassette extlibrary_videocassette;


    public extlibrary_Person(
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

    public extlibrary_VideoCassette getExtlibrary_videocassette() {
        return extlibrary_videocassette;
    }

    public void setExtlibrary_videocassette(extlibrary_VideoCassette extlibrary_videocassette) {
        this.extlibrary_videocassette = extlibrary_videocassette;
    }

}