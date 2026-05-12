





import java.util.List;
import java.util.ArrayList;

public class reserve_UseCase  {






    private Librarian__Actor librarian__actor;




    private patron__Actor patron__actor;


    public reserve_UseCase(
    ) {
    }



    public Librarian__Actor getLibrarian__actor() {
        return librarian__actor;
    }

    public void setLibrarian__actor(Librarian__Actor librarian__actor) {
        this.librarian__actor = librarian__actor;
    }
    public patron__Actor getPatron__actor() {
        return patron__actor;
    }

    public void setPatron__actor(patron__Actor patron__actor) {
        this.patron__actor = patron__actor;
    }

}