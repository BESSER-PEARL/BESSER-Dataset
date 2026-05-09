





import java.util.List;
import java.util.ArrayList;

public class helloworld150_Person extends NamedElement {

    private String birthDate;
    private String forName;





    private helloworld150_Own helloworld150_own;


    public helloworld150_Person(
        String birthDate,        String forName    ) {
        super(
        );
        this.birthDate = birthDate;
        this.forName = forName;
    }


    public String getBirthdate() {
        return birthDate;
    }

    public void setBirthdate(String birthDate) {
        this.birthDate = birthDate;
    }
    public String getForname() {
        return forName;
    }

    public void setForname(String forName) {
        this.forName = forName;
    }

    public helloworld150_Own getHelloworld150_own() {
        return helloworld150_own;
    }

    public void setHelloworld150_own(helloworld150_Own helloworld150_own) {
        this.helloworld150_own = helloworld150_own;
    }

}