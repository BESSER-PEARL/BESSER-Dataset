




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class gametournament_Tournament  {

    private LocalDate startDate;
    private int prize;
    private String location;
    private String name;
    private LocalDate endDate;



    public gametournament_Tournament(
        LocalDate startDate,        int prize,        String location,        String name,        LocalDate endDate    ) {
        this.startDate = startDate;
        this.prize = prize;
        this.location = location;
        this.name = name;
        this.endDate = endDate;
    }


    public LocalDate getStartdate() {
        return startDate;
    }

    public void setStartdate(LocalDate startDate) {
        this.startDate = startDate;
    }
    public int getPrize() {
        return prize;
    }

    public void setPrize(int prize) {
        this.prize = prize;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public LocalDate getEnddate() {
        return endDate;
    }

    public void setEnddate(LocalDate endDate) {
        this.endDate = endDate;
    }


}