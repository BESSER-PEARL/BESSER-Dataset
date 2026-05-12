





import java.util.List;
import java.util.ArrayList;

public class Cleaning_Management_UseCase  {






    private Cleaner_Actor cleaner_actor;




    private Info_UseCase info_usecase;


    public Cleaning_Management_UseCase(
    ) {
    }



    public Cleaner_Actor getCleaner_actor() {
        return cleaner_actor;
    }

    public void setCleaner_actor(Cleaner_Actor cleaner_actor) {
        this.cleaner_actor = cleaner_actor;
    }
    public Info_UseCase getInfo_usecase() {
        return info_usecase;
    }

    public void setInfo_usecase(Info_UseCase info_usecase) {
        this.info_usecase = info_usecase;
    }

}