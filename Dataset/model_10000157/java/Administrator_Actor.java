





import java.util.List;
import java.util.ArrayList;

public class Administrator_Actor  {






    private Log_In_UseCase log_in_usecase;




    private Log_Out_UseCase log_out_usecase;




    private Notes___Comments_UseCase notes___comments_usecase;


    public Administrator_Actor(
    ) {
    }



    public Log_In_UseCase getLog_in_usecase() {
        return log_in_usecase;
    }

    public void setLog_in_usecase(Log_In_UseCase log_in_usecase) {
        this.log_in_usecase = log_in_usecase;
    }
    public Log_Out_UseCase getLog_out_usecase() {
        return log_out_usecase;
    }

    public void setLog_out_usecase(Log_Out_UseCase log_out_usecase) {
        this.log_out_usecase = log_out_usecase;
    }
    public Notes___Comments_UseCase getNotes___comments_usecase() {
        return notes___comments_usecase;
    }

    public void setNotes___comments_usecase(Notes___Comments_UseCase notes___comments_usecase) {
        this.notes___comments_usecase = notes___comments_usecase;
    }

}