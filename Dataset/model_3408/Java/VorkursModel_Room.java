





import java.util.List;
import java.util.ArrayList;

public class VorkursModel_Room  {

    private int roomNr;
    private int seats;
    private boolean hasComputers;
    private boolean sockets;





    private VorkursModel_TeachingAssistant vorkursmodel_teachingassistant;


    public VorkursModel_Room(
        int roomNr,        int seats,        boolean hasComputers,        boolean sockets    ) {
        this.roomNr = roomNr;
        this.seats = seats;
        this.hasComputers = hasComputers;
        this.sockets = sockets;
    }


    public int getRoomnr() {
        return roomNr;
    }

    public void setRoomnr(int roomNr) {
        this.roomNr = roomNr;
    }
    public int getSeats() {
        return seats;
    }

    public void setSeats(int seats) {
        this.seats = seats;
    }
    public boolean getHascomputers() {
        return hasComputers;
    }

    public void setHascomputers(boolean hasComputers) {
        this.hasComputers = hasComputers;
    }
    public boolean getSockets() {
        return sockets;
    }

    public void setSockets(boolean sockets) {
        this.sockets = sockets;
    }

    public VorkursModel_TeachingAssistant getVorkursmodel_teachingassistant() {
        return vorkursmodel_teachingassistant;
    }

    public void setVorkursmodel_teachingassistant(VorkursModel_TeachingAssistant vorkursmodel_teachingassistant) {
        this.vorkursmodel_teachingassistant = vorkursmodel_teachingassistant;
    }

}