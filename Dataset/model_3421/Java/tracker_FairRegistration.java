





import java.util.List;
import java.util.ArrayList;

public class tracker_FairRegistration extends Event {

    private String parent;
    private String phone;
    private String address;
    private String participant;
    private String club;



    public tracker_FairRegistration(
        String parent,        String phone,        String address,        String participant,        String club    ) {
        super(
        );
        this.parent = parent;
        this.phone = phone;
        this.address = address;
        this.participant = participant;
        this.club = club;
    }


    public String getParent() {
        return parent;
    }

    public void setParent(String parent) {
        this.parent = parent;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getParticipant() {
        return participant;
    }

    public void setParticipant(String participant) {
        this.participant = participant;
    }
    public String getClub() {
        return club;
    }

    public void setClub(String club) {
        this.club = club;
    }


}