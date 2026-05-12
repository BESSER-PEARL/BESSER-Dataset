





import java.util.List;
import java.util.ArrayList;

public class Logout_UseCase  {






    private Job_Seeker_Actor job_seeker_actor;




    private Employer_Actor employer_actor;




    private Admin_Actor admin_actor;


    public Logout_UseCase(
    ) {
    }



    public Job_Seeker_Actor getJob_seeker_actor() {
        return job_seeker_actor;
    }

    public void setJob_seeker_actor(Job_Seeker_Actor job_seeker_actor) {
        this.job_seeker_actor = job_seeker_actor;
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