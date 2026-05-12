





import java.util.List;
import java.util.ArrayList;

public class bean_ProfessionBean  {

    private String profession;
    private String email;
    private String workIn;
    private String qualification;



    public bean_ProfessionBean(
        String profession,        String email,        String workIn,        String qualification    ) {
        this.profession = profession;
        this.email = email;
        this.workIn = workIn;
        this.qualification = qualification;
    }


    public String getProfession() {
        return profession;
    }

    public void setProfession(String profession) {
        this.profession = profession;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getWorkin() {
        return workIn;
    }

    public void setWorkin(String workIn) {
        this.workIn = workIn;
    }
    public String getQualification() {
        return qualification;
    }

    public void setQualification(String qualification) {
        this.qualification = qualification;
    }


}