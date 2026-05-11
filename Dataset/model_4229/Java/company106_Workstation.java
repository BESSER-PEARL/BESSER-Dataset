





import java.util.List;
import java.util.ArrayList;

public class company106_Workstation extends NamedElement {

    private String profileDescription;





    private company106_Room company106_room;


    public company106_Workstation(
        String profileDescription    ) {
        super(
        );
        this.profileDescription = profileDescription;
    }


    public String getProfiledescription() {
        return profileDescription;
    }

    public void setProfiledescription(String profileDescription) {
        this.profileDescription = profileDescription;
    }

    public company106_Room getCompany106_room() {
        return company106_room;
    }

    public void setCompany106_room(company106_Room company106_room) {
        this.company106_room = company106_room;
    }

}