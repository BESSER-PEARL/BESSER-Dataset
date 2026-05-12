





import java.util.List;
import java.util.ArrayList;

public class Registration_UseCase  {






    private Employer_Actor employer_actor;




    private Job_Seeker_Actor job_seeker_actor;


    public Registration_UseCase(
    ) {
    }



    public Employer_Actor getEmployer_actor() {
        return employer_actor;
    }

    public void setEmployer_actor(Employer_Actor employer_actor) {
        this.employer_actor = employer_actor;
    }
    public Job_Seeker_Actor getJob_seeker_actor() {
        return job_seeker_actor;
    }

    public void setJob_seeker_actor(Job_Seeker_Actor job_seeker_actor) {
        this.job_seeker_actor = job_seeker_actor;
    }

}