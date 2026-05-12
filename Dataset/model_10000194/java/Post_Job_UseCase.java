





import java.util.List;
import java.util.ArrayList;

public class Post_Job_UseCase  {






    private Employer_Actor employer_actor;




    private Admin_Actor admin_actor;


    public Post_Job_UseCase(
    ) {
    }



    public Employer_Actor getEmployer_actor() {
        return employer_actor;
    }

    public void setEmployer_actor(Employer_Actor employer_actor) {
        this.employer_actor = employer_actor;
    }
    public Admin_Actor getAdmin_actor() {
        return admin_actor;
    }

    public void setAdmin_actor(Admin_Actor admin_actor) {
        this.admin_actor = admin_actor;
    }

}