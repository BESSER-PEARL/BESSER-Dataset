





import java.util.List;
import java.util.ArrayList;

public class company104_Workstation extends NamedElement {

    private String ProfileDescription;





    private company104_Room company104_room;


    public company104_Workstation(
        String ProfileDescription    ) {
        super(
        );
        this.ProfileDescription = ProfileDescription;
    }


    public String getProfiledescription() {
        return ProfileDescription;
    }

    public void setProfiledescription(String ProfileDescription) {
        this.ProfileDescription = ProfileDescription;
    }

    public company104_Room getCompany104_room() {
        return company104_room;
    }

    public void setCompany104_room(company104_Room company104_room) {
        this.company104_room = company104_room;
    }

}