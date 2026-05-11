





import java.util.List;
import java.util.ArrayList;

public class VorkursModel_Room  {

    private boolean sockets;
    private int seats;
    private boolean hasComputers;
    private int roomNr;





    private VorkursModel_TeachingAssistant vorkursmodel_teachingassistant;


    public VorkursModel_Room(
        boolean sockets,        int seats,        boolean hasComputers,        int roomNr    ) {
        this.sockets = sockets;
        this.seats = seats;
        this.hasComputers = hasComputers;
        this.roomNr = roomNr;
    }


    public boolean getSockets() {
        return sockets;
    }

    public void setSockets(boolean sockets) {
        this.sockets = sockets;
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
    public int getRoomnr() {
        return roomNr;
    }

    public void setRoomnr(int roomNr) {
        this.roomNr = roomNr;
    }

    public VorkursModel_TeachingAssistant getVorkursmodel_teachingassistant() {
        return vorkursmodel_teachingassistant;
    }

    public void setVorkursmodel_teachingassistant(VorkursModel_TeachingAssistant vorkursmodel_teachingassistant) {
        this.vorkursmodel_teachingassistant = vorkursmodel_teachingassistant;
    }

}