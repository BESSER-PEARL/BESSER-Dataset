





import java.util.List;
import java.util.ArrayList;

public class company106_Department extends Function {






    private company106_Agency company106_agency;




    private List<company106_Room> company106_rooms;


    public company106_Department(
    ) {
        super(
        );
        this.company106_rooms = new ArrayList<>();
    }

    public company106_Department(
        ArrayList<company106_Room> company106_rooms    ) {
        this.company106_rooms = company106_rooms;
    }


    public company106_Agency getCompany106_agency() {
        return company106_agency;
    }

    public void setCompany106_agency(company106_Agency company106_agency) {
        this.company106_agency = company106_agency;
    }
    public List<company106_Room> getCompany106_rooms() {
        return company106_rooms;
    }

    public void addCompany106_room(Company106_room company106_room) {
        this.company106_rooms.add(company106_room);
    }

}