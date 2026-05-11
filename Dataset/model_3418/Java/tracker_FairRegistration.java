





import java.util.List;
import java.util.ArrayList;

public class tracker_FairRegistration extends Event {

    private String participant;
    private String parent;
    private String club;
    private String address;
    private String phone;



    public tracker_FairRegistration(
        String participant,        String parent,        String club,        String address,        String phone    ) {
        super(
        );
        this.participant = participant;
        this.parent = parent;
        this.club = club;
        this.address = address;
        this.phone = phone;
    }


    public String getParticipant() {
        return participant;
    }

    public void setParticipant(String participant) {
        this.participant = participant;
    }
    public String getParent() {
        return parent;
    }

    public void setParent(String parent) {
        this.parent = parent;
    }
    public String getClub() {
        return club;
    }

    public void setClub(String club) {
        this.club = club;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }


}