





import java.util.List;
import java.util.ArrayList;

public class Implementation_RoomComponent_ConferenceRoom extends RoomComponent_Room {

    private boolean projector;
    private boolean conferencePhone;
    private int numberOfSeats;





    private Implementation_RoomComponent_RoomHandler implementation_roomcomponent_roomhandler;


    public Implementation_RoomComponent_ConferenceRoom(
        boolean projector,        boolean conferencePhone,        int numberOfSeats    ) {
        super(
        );
        this.projector = projector;
        this.conferencePhone = conferencePhone;
        this.numberOfSeats = numberOfSeats;
    }


    public boolean getProjector() {
        return projector;
    }

    public void setProjector(boolean projector) {
        this.projector = projector;
    }
    public boolean getConferencephone() {
        return conferencePhone;
    }

    public void setConferencephone(boolean conferencePhone) {
        this.conferencePhone = conferencePhone;
    }
    public int getNumberofseats() {
        return numberOfSeats;
    }

    public void setNumberofseats(int numberOfSeats) {
        this.numberOfSeats = numberOfSeats;
    }

    public Implementation_RoomComponent_RoomHandler getImplementation_roomcomponent_roomhandler() {
        return implementation_roomcomponent_roomhandler;
    }

    public void setImplementation_roomcomponent_roomhandler(Implementation_RoomComponent_RoomHandler implementation_roomcomponent_roomhandler) {
        this.implementation_roomcomponent_roomhandler = implementation_roomcomponent_roomhandler;
    }

}