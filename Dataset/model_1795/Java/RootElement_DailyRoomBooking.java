





import java.util.List;
import java.util.ArrayList;

public class RootElement_DailyRoomBooking extends RoomBooking {

    private String nbrOfGuests;



    public RootElement_DailyRoomBooking(
        String nbrOfGuests    ) {
        super(
        );
        this.nbrOfGuests = nbrOfGuests;
    }


    public String getNbrofguests() {
        return nbrOfGuests;
    }

    public void setNbrofguests(String nbrOfGuests) {
        this.nbrOfGuests = nbrOfGuests;
    }


}