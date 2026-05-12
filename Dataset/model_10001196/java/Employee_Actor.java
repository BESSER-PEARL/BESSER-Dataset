





import java.util.List;
import java.util.ArrayList;

public class Employee_Actor  {






    private Approver_Jobs_UseCase approver_jobs_usecase;




    private Login_UseCase login_usecase;


    public Employee_Actor(
    ) {
    }



    public Approver_Jobs_UseCase getApprover_jobs_usecase() {
        return approver_jobs_usecase;
    }

    public void setApprover_jobs_usecase(Approver_Jobs_UseCase approver_jobs_usecase) {
        this.approver_jobs_usecase = approver_jobs_usecase;
    }
    public Login_UseCase getLogin_usecase() {
        return login_usecase;
    }

    public void setLogin_usecase(Login_UseCase login_usecase) {
        this.login_usecase = login_usecase;
    }

}