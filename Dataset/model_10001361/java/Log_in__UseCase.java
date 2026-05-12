





import java.util.List;
import java.util.ArrayList;

public class Log_in__UseCase  {






    private Data_entry_employee__Actor data_entry_employee__actor;




    private Administrator__Actor administrator__actor;


    public Log_in__UseCase(
    ) {
    }



    public Data_entry_employee__Actor getData_entry_employee__actor() {
        return data_entry_employee__actor;
    }

    public void setData_entry_employee__actor(Data_entry_employee__Actor data_entry_employee__actor) {
        this.data_entry_employee__actor = data_entry_employee__actor;
    }
    public Administrator__Actor getAdministrator__actor() {
        return administrator__actor;
    }

    public void setAdministrator__actor(Administrator__Actor administrator__actor) {
        this.administrator__actor = administrator__actor;
    }

}