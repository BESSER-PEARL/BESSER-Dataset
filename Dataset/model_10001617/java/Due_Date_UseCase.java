





import java.util.List;
import java.util.ArrayList;

public class Due_Date_UseCase  {






    private Library_Inventory_UseCase library_inventory_usecase;




    private Librarian_Actor librarian_actor;




    private User_Status_UseCase user_status_usecase;




    private Fine_Calculation_UseCase fine_calculation_usecase;


    public Due_Date_UseCase(
    ) {
    }



    public Library_Inventory_UseCase getLibrary_inventory_usecase() {
        return library_inventory_usecase;
    }

    public void setLibrary_inventory_usecase(Library_Inventory_UseCase library_inventory_usecase) {
        this.library_inventory_usecase = library_inventory_usecase;
    }
    public Librarian_Actor getLibrarian_actor() {
        return librarian_actor;
    }

    public void setLibrarian_actor(Librarian_Actor librarian_actor) {
        this.librarian_actor = librarian_actor;
    }
    public User_Status_UseCase getUser_status_usecase() {
        return user_status_usecase;
    }

    public void setUser_status_usecase(User_Status_UseCase user_status_usecase) {
        this.user_status_usecase = user_status_usecase;
    }
    public Fine_Calculation_UseCase getFine_calculation_usecase() {
        return fine_calculation_usecase;
    }

    public void setFine_calculation_usecase(Fine_Calculation_UseCase fine_calculation_usecase) {
        this.fine_calculation_usecase = fine_calculation_usecase;
    }

}