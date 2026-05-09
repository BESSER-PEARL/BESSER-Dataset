





import java.util.List;
import java.util.ArrayList;

public class HALL_Model  {






    private HALL_SystemComponent hall_systemcomponent;




    private List<HALL_SystemComponent> hall_systemcomponents;




    private List<HALL_UserProfile> hall_userprofiles;




    private HALL_UserProfile hall_userprofile;


    public HALL_Model(
    ) {
        this.hall_systemcomponents = new ArrayList<>();
        this.hall_userprofiles = new ArrayList<>();
    }

    public HALL_Model(
        ArrayList<HALL_SystemComponent> hall_systemcomponents,        ArrayList<HALL_UserProfile> hall_userprofiles    ) {
        this.hall_systemcomponents = hall_systemcomponents;
        this.hall_userprofiles = hall_userprofiles;
    }


    public HALL_SystemComponent getHall_systemcomponent() {
        return hall_systemcomponent;
    }

    public void setHall_systemcomponent(HALL_SystemComponent hall_systemcomponent) {
        this.hall_systemcomponent = hall_systemcomponent;
    }
    public List<HALL_SystemComponent> getHall_systemcomponents() {
        return hall_systemcomponents;
    }

    public void addHall_systemcomponent(Hall_systemcomponent hall_systemcomponent) {
        this.hall_systemcomponents.add(hall_systemcomponent);
    }
    public List<HALL_UserProfile> getHall_userprofiles() {
        return hall_userprofiles;
    }

    public void addHall_userprofile(Hall_userprofile hall_userprofile) {
        this.hall_userprofiles.add(hall_userprofile);
    }
    public HALL_UserProfile getHall_userprofile() {
        return hall_userprofile;
    }

    public void setHall_userprofile(HALL_UserProfile hall_userprofile) {
        this.hall_userprofile = hall_userprofile;
    }

}