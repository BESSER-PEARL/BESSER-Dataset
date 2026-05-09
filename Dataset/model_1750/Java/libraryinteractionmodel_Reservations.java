





import java.util.List;
import java.util.ArrayList;

public class libraryinteractionmodel_Reservations  {






    private libraryinteractionmodel_Book libraryinteractionmodel_book;




    private List<libraryinteractionmodel_Reservation> libraryinteractionmodel_reservations;


    public libraryinteractionmodel_Reservations(
    ) {
        this.libraryinteractionmodel_reservations = new ArrayList<>();
    }

    public libraryinteractionmodel_Reservations(
        ArrayList<libraryinteractionmodel_Reservation> libraryinteractionmodel_reservations    ) {
        this.libraryinteractionmodel_reservations = libraryinteractionmodel_reservations;
    }


    public libraryinteractionmodel_Book getLibraryinteractionmodel_book() {
        return libraryinteractionmodel_book;
    }

    public void setLibraryinteractionmodel_book(libraryinteractionmodel_Book libraryinteractionmodel_book) {
        this.libraryinteractionmodel_book = libraryinteractionmodel_book;
    }
    public List<libraryinteractionmodel_Reservation> getLibraryinteractionmodel_reservations() {
        return libraryinteractionmodel_reservations;
    }

    public void addLibraryinteractionmodel_reservation(Libraryinteractionmodel_reservation libraryinteractionmodel_reservation) {
        this.libraryinteractionmodel_reservations.add(libraryinteractionmodel_reservation);
    }

}