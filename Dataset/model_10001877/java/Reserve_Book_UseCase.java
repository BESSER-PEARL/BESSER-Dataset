





import java.util.List;
import java.util.ArrayList;

public class Reserve_Book_UseCase  {






    private Patron_Actor patron_actor;




    private Librarian_Actor librarian_actor;


    public Reserve_Book_UseCase(
    ) {
    }



    public Patron_Actor getPatron_actor() {
        return patron_actor;
    }

    public void setPatron_actor(Patron_Actor patron_actor) {
        this.patron_actor = patron_actor;
    }
    public Librarian_Actor getLibrarian_actor() {
        return librarian_actor;
    }

    public void setLibrarian_actor(Librarian_Actor librarian_actor) {
        this.librarian_actor = librarian_actor;
    }

}