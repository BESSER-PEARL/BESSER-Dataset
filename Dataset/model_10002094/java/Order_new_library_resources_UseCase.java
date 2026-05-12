





import java.util.List;
import java.util.ArrayList;

public class Order_new_library_resources_UseCase  {






    private Library_staff_Actor library_staff_actor;




    private Library_Actor library_actor;


    public Order_new_library_resources_UseCase(
    ) {
    }



    public Library_staff_Actor getLibrary_staff_actor() {
        return library_staff_actor;
    }

    public void setLibrary_staff_actor(Library_staff_Actor library_staff_actor) {
        this.library_staff_actor = library_staff_actor;
    }
    public Library_Actor getLibrary_actor() {
        return library_actor;
    }

    public void setLibrary_actor(Library_Actor library_actor) {
        this.library_actor = library_actor;
    }

}