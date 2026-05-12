





import java.util.List;
import java.util.ArrayList;

public class Search_UseCase  {






    private Patron_Actor patron_actor;




    private Reserve_UseCase reserve_usecase;




    private Library_Inventory_UseCase library_inventory_usecase;


    public Search_UseCase(
    ) {
    }



    public Patron_Actor getPatron_actor() {
        return patron_actor;
    }

    public void setPatron_actor(Patron_Actor patron_actor) {
        this.patron_actor = patron_actor;
    }
    public Reserve_UseCase getReserve_usecase() {
        return reserve_usecase;
    }

    public void setReserve_usecase(Reserve_UseCase reserve_usecase) {
        this.reserve_usecase = reserve_usecase;
    }
    public Library_Inventory_UseCase getLibrary_inventory_usecase() {
        return library_inventory_usecase;
    }

    public void setLibrary_inventory_usecase(Library_Inventory_UseCase library_inventory_usecase) {
        this.library_inventory_usecase = library_inventory_usecase;
    }

}