





import java.util.List;
import java.util.ArrayList;

public class build_Contact  {

    private String name;
    private String email;





    private build_Contribution build_contribution;


    public build_Contact(
        String name,        String email    ) {
        this.name = name;
        this.email = email;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public build_Contribution getBuild_contribution() {
        return build_contribution;
    }

    public void setBuild_contribution(build_Contribution build_contribution) {
        this.build_contribution = build_contribution;
    }

}