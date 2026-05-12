





import java.util.List;
import java.util.ArrayList;

public class User_Status_UseCase  {






    private Check_In_UseCase check_in_usecase;




    private Library_Inventory_UseCase library_inventory_usecase;




    private Check_out_UseCase check_out_usecase;


    public User_Status_UseCase(
    ) {
    }



    public Check_In_UseCase getCheck_in_usecase() {
        return check_in_usecase;
    }

    public void setCheck_in_usecase(Check_In_UseCase check_in_usecase) {
        this.check_in_usecase = check_in_usecase;
    }
    public Library_Inventory_UseCase getLibrary_inventory_usecase() {
        return library_inventory_usecase;
    }

    public void setLibrary_inventory_usecase(Library_Inventory_UseCase library_inventory_usecase) {
        this.library_inventory_usecase = library_inventory_usecase;
    }
    public Check_out_UseCase getCheck_out_usecase() {
        return check_out_usecase;
    }

    public void setCheck_out_usecase(Check_out_UseCase check_out_usecase) {
        this.check_out_usecase = check_out_usecase;
    }

}