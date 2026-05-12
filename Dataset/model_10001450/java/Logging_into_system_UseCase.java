





import java.util.List;
import java.util.ArrayList;

public class Logging_into_system_UseCase  {






    private Patient_Actor patient_actor;




    private Employee_Actor employee_actor;


    public Logging_into_system_UseCase(
    ) {
    }



    public Patient_Actor getPatient_actor() {
        return patient_actor;
    }

    public void setPatient_actor(Patient_Actor patient_actor) {
        this.patient_actor = patient_actor;
    }
    public Employee_Actor getEmployee_actor() {
        return employee_actor;
    }

    public void setEmployee_actor(Employee_Actor employee_actor) {
        this.employee_actor = employee_actor;
    }

}