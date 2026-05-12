





import java.util.List;
import java.util.ArrayList;

public class Check_In_Book_UseCase  {






    private Librarian_Actor librarian_actor;




    private Patron_Actor patron_actor;


    public Check_In_Book_UseCase(
    ) {
    }



    public Librarian_Actor getLibrarian_actor() {
        return librarian_actor;
    }

    public void setLibrarian_actor(Librarian_Actor librarian_actor) {
        this.librarian_actor = librarian_actor;
    }
    public Patron_Actor getPatron_actor() {
        return patron_actor;
    }

    public void setPatron_actor(Patron_Actor patron_actor) {
        this.patron_actor = patron_actor;
    }

}