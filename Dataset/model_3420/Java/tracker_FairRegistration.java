





import java.util.List;
import java.util.ArrayList;

public class tracker_FairRegistration extends Event {

    private String address;
    private String participant;
    private String phone;
    private String club;
    private String parent;



    public tracker_FairRegistration(
        String address,        String participant,        String phone,        String club,        String parent    ) {
        super(
        );
        this.address = address;
        this.participant = participant;
        this.phone = phone;
        this.club = club;
        this.parent = parent;
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
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public String getClub() {
        return club;
    }

    public void setClub(String club) {
        this.club = club;
    }
    public String getParent() {
        return parent;
    }

    public void setParent(String parent) {
        this.parent = parent;
    }


}