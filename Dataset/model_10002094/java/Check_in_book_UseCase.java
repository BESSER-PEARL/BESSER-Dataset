





import java.util.List;
import java.util.ArrayList;

public class Check_in_book_UseCase  {






    private Return_book_UseCase return_book_usecase;




    private Library_Actor library_actor;


    public Check_in_book_UseCase(
    ) {
    }



    public Return_book_UseCase getReturn_book_usecase() {
        return return_book_usecase;
    }

    public void setReturn_book_usecase(Return_book_UseCase return_book_usecase) {
        this.return_book_usecase = return_book_usecase;
    }
    public Library_Actor getLibrary_actor() {
        return library_actor;
    }

    public void setLibrary_actor(Library_Actor library_actor) {
        this.library_actor = library_actor;
    }

}