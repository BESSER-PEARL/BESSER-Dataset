





import java.util.List;
import java.util.ArrayList;

public class Food  {

    private int foodID;
    private String name;





    private List<Chef> chefs;




    private List<Guest> guests;


    public Food(
        int foodID,        String name    ) {
        this.foodID = foodID;
        this.name = name;
        this.chefs = new ArrayList<>();
        this.guests = new ArrayList<>();
    }

    public Food(
        int foodID,        String name        ArrayList<Chef> chefs,        ArrayList<Guest> guests    ) {
        this.foodID = foodID;
        this.name = name;
        this.chefs = chefs;
        this.guests = guests;
    }

    public int getFoodid() {
        return foodID;
    }

    public void setFoodid(int foodID) {
        this.foodID = foodID;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Chef> getChefs() {
        return chefs;
    }

    public void addChef(Chef chef) {
        this.chefs.add(chef);
    }
    public List<Guest> getGuests() {
        return guests;
    }

    public void addGuest(Guest guest) {
        this.guests.add(guest);
    }

}