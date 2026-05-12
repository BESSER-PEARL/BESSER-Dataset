





import java.util.List;
import java.util.ArrayList;

public class Retire_Old_Inventory_UseCase  {






    private Library_Inventory_UseCase library_inventory_usecase;




    private Librarian_Actor librarian_actor;


    public Retire_Old_Inventory_UseCase(
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

}