




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class reservationsystem_SpecificFlight  {

    private int status;
    private LocalDate realArriTime;
    private int id;
    private LocalDate realDepTime;
    private LocalDate date;





    private List<reservationsystem_Crew> reservationsystem_crews;




    private reservationsystem_Crew reservationsystem_crew;


    public reservationsystem_SpecificFlight(
        int status,        LocalDate realArriTime,        int id,        LocalDate realDepTime,        LocalDate date    ) {
        this.status = status;
        this.realArriTime = realArriTime;
        this.id = id;
        this.realDepTime = realDepTime;
        this.date = date;
        this.reservationsystem_crews = new ArrayList<>();
    }

    public reservationsystem_SpecificFlight(
        int status,        LocalDate realArriTime,        int id,        LocalDate realDepTime,        LocalDate date        ArrayList<reservationsystem_Crew> reservationsystem_crews    ) {
        this.status = status;
        this.realArriTime = realArriTime;
        this.id = id;
        this.realDepTime = realDepTime;
        this.date = date;
        this.reservationsystem_crews = reservationsystem_crews;
    }

    public int getStatus() {
        return status;
    }

    public void setStatus(int status) {
        this.status = status;
    }
    public LocalDate getRealarritime() {
        return realArriTime;
    }

    public void setRealarritime(LocalDate realArriTime) {
        this.realArriTime = realArriTime;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public LocalDate getRealdeptime() {
        return realDepTime;
    }

    public void setRealdeptime(LocalDate realDepTime) {
        this.realDepTime = realDepTime;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }

    public List<reservationsystem_Crew> getReservationsystem_crews() {
        return reservationsystem_crews;
    }

    public void addReservationsystem_crew(Reservationsystem_crew reservationsystem_crew) {
        this.reservationsystem_crews.add(reservationsystem_crew);
    }
    public reservationsystem_Crew getReservationsystem_crew() {
        return reservationsystem_crew;
    }

    public void setReservationsystem_crew(reservationsystem_Crew reservationsystem_crew) {
        this.reservationsystem_crew = reservationsystem_crew;
    }

}