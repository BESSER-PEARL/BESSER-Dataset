





import java.util.List;
import java.util.ArrayList;

public class logout_UseCase  {






    private employer_Actor1 employer_actor1;




    private admin_Actor2 admin_actor2;




    private job_seeker_Actor2 job_seeker_actor2;


    public logout_UseCase(
    ) {
    }



    public employer_Actor1 getEmployer_actor1() {
        return employer_actor1;
    }

    public void setEmployer_actor1(employer_Actor1 employer_actor1) {
        this.employer_actor1 = employer_actor1;
    }
    public admin_Actor2 getAdmin_actor2() {
        return admin_actor2;
    }

    public void setAdmin_actor2(admin_Actor2 admin_actor2) {
        this.admin_actor2 = admin_actor2;
    }
    public job_seeker_Actor2 getJob_seeker_actor2() {
        return job_seeker_actor2;
    }

    public void setJob_seeker_actor2(job_seeker_Actor2 job_seeker_actor2) {
        this.job_seeker_actor2 = job_seeker_actor2;
    }

}