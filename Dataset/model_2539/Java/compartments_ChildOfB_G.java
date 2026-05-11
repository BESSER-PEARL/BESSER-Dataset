





import java.util.List;
import java.util.ArrayList;

public class compartments_ChildOfB_G  {

    private int number;





    private compartments_TopNodeB compartments_topnodeb;




    private List<compartments_ChildOfAffixed> compartments_childofaffixeds;


    public compartments_ChildOfB_G(
        int number    ) {
        this.number = number;
        this.compartments_childofaffixeds = new ArrayList<>();
    }

    public compartments_ChildOfB_G(
        int number        ArrayList<compartments_ChildOfAffixed> compartments_childofaffixeds    ) {
        this.number = number;
        this.compartments_childofaffixeds = compartments_childofaffixeds;
    }

    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    public compartments_TopNodeB getCompartments_topnodeb() {
        return compartments_topnodeb;
    }

    public void setCompartments_topnodeb(compartments_TopNodeB compartments_topnodeb) {
        this.compartments_topnodeb = compartments_topnodeb;
    }
    public List<compartments_ChildOfAffixed> getCompartments_childofaffixeds() {
        return compartments_childofaffixeds;
    }

    public void addCompartments_childofaffixed(Compartments_childofaffixed compartments_childofaffixed) {
        this.compartments_childofaffixeds.add(compartments_childofaffixed);
    }

}