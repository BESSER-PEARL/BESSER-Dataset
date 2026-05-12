





import java.util.List;
import java.util.ArrayList;

public class login_UseCase2  {






    private Job_Seeker_Actor job_seeker_actor;




    private Administrator_Actor1 administrator_actor1;




    private Employer_Actor employer_actor;


    public login_UseCase2(
    ) {
    }



    public Job_Seeker_Actor getJob_seeker_actor() {
        return job_seeker_actor;
    }

    public void setJob_seeker_actor(Job_Seeker_Actor job_seeker_actor) {
        this.job_seeker_actor = job_seeker_actor;
    }
    public Administrator_Actor1 getAdministrator_actor1() {
        return administrator_actor1;
    }

    public void setAdministrator_actor1(Administrator_Actor1 administrator_actor1) {
        this.administrator_actor1 = administrator_actor1;
    }
    public Employer_Actor getEmployer_actor() {
        return employer_actor;
    }

    public void setEmployer_actor(Employer_Actor employer_actor) {
        this.employer_actor = employer_actor;
    }

}