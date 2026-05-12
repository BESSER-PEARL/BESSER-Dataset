





import java.util.List;
import java.util.ArrayList;

public class Delivery_Management_UseCase  {






    private Cleaning_Management_UseCase cleaning_management_usecase;


    public Delivery_Management_UseCase(
    ) {
    }



    public Cleaning_Management_UseCase getCleaning_management_usecase() {
        return cleaning_management_usecase;
    }

    public void setCleaning_management_usecase(Cleaning_Management_UseCase cleaning_management_usecase) {
        this.cleaning_management_usecase = cleaning_management_usecase;
    }

}