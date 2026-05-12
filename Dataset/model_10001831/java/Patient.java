





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private int room;
    private int duration;
    private boolean hasroom;
    private String disease;
    private boolean hasdoc;





    private doctor doctor;


    public Patient(
        int room,        int duration,        boolean hasroom,        String disease,        boolean hasdoc    ) {
        this.room = room;
        this.duration = duration;
        this.hasroom = hasroom;
        this.disease = disease;
        this.hasdoc = hasdoc;
    }


    public int getRoom() {
        return room;
    }

    public void setRoom(int room) {
        this.room = room;
    }
    public int getDuration() {
        return duration;
    }

    public void setDuration(int duration) {
        this.duration = duration;
    }
    public boolean getHasroom() {
        return hasroom;
    }

    public void setHasroom(boolean hasroom) {
        this.hasroom = hasroom;
    }
    public String getDisease() {
        return disease;
    }

    public void setDisease(String disease) {
        this.disease = disease;
    }
    public boolean getHasdoc() {
        return hasdoc;
    }

    public void setHasdoc(boolean hasdoc) {
        this.hasdoc = hasdoc;
    }

    public doctor getDoctor() {
        return doctor;
    }

    public void setDoctor(doctor doctor) {
        this.doctor = doctor;
    }

}