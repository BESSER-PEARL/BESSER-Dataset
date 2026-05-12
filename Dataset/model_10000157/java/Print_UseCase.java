





import java.util.List;
import java.util.ArrayList;

public class Print_UseCase  {






    private Employee_Actor employee_actor;




    private Administrator_Actor administrator_actor;


    public Print_UseCase(
    ) {
    }



    public Employee_Actor getEmployee_actor() {
        return employee_actor;
    }

    public void setEmployee_actor(Employee_Actor employee_actor) {
        this.employee_actor = employee_actor;
    }
    public Administrator_Actor getAdministrator_actor() {
        return administrator_actor;
    }

    public void setAdministrator_actor(Administrator_Actor administrator_actor) {
        this.administrator_actor = administrator_actor;
    }

}