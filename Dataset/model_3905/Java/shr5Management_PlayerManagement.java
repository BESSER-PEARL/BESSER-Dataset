





import java.util.List;
import java.util.ArrayList;

public class shr5Management_PlayerManagement extends Beschreibbar {






    private List<shr5Management_PlayerManagement> shr5management_playermanagements;




    private List<shr5Management_CharacterGroup> shr5management_charactergroups;


    public shr5Management_PlayerManagement(
    ) {
        super(
        );
        this.shr5management_playermanagements = new ArrayList<>();
        this.shr5management_charactergroups = new ArrayList<>();
    }

    public shr5Management_PlayerManagement(
        ArrayList<shr5Management_PlayerManagement> shr5management_playermanagements,        ArrayList<shr5Management_CharacterGroup> shr5management_charactergroups    ) {
        this.shr5management_playermanagements = shr5management_playermanagements;
        this.shr5management_charactergroups = shr5management_charactergroups;
    }


    public List<shr5Management_PlayerManagement> getShr5management_playermanagements() {
        return shr5management_playermanagements;
    }

    public void addShr5management_playermanagement(Shr5management_playermanagement shr5management_playermanagement) {
        this.shr5management_playermanagements.add(shr5management_playermanagement);
    }
    public List<shr5Management_CharacterGroup> getShr5management_charactergroups() {
        return shr5management_charactergroups;
    }

    public void addShr5management_charactergroup(Shr5management_charactergroup shr5management_charactergroup) {
        this.shr5management_charactergroups.add(shr5management_charactergroup);
    }

}