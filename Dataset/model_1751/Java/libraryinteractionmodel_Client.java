





import java.util.List;
import java.util.ArrayList;

public class libraryinteractionmodel_Client  {

    private String email;
    private String name;





    private libraryinteractionmodel_Clients libraryinteractionmodel_clients;




    private libraryinteractionmodel_Client libraryinteractionmodel_client;




    private libraryinteractionmodel_Reservation libraryinteractionmodel_reservation;


    public libraryinteractionmodel_Client(
        String email,        String name    ) {
        this.email = email;
        this.name = name;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public libraryinteractionmodel_Clients getLibraryinteractionmodel_clients() {
        return libraryinteractionmodel_clients;
    }

    public void setLibraryinteractionmodel_clients(libraryinteractionmodel_Clients libraryinteractionmodel_clients) {
        this.libraryinteractionmodel_clients = libraryinteractionmodel_clients;
    }
    public libraryinteractionmodel_Client getLibraryinteractionmodel_client() {
        return libraryinteractionmodel_client;
    }

    public void setLibraryinteractionmodel_client(libraryinteractionmodel_Client libraryinteractionmodel_client) {
        this.libraryinteractionmodel_client = libraryinteractionmodel_client;
    }
    public libraryinteractionmodel_Reservation getLibraryinteractionmodel_reservation() {
        return libraryinteractionmodel_reservation;
    }

    public void setLibraryinteractionmodel_reservation(libraryinteractionmodel_Reservation libraryinteractionmodel_reservation) {
        this.libraryinteractionmodel_reservation = libraryinteractionmodel_reservation;
    }

}