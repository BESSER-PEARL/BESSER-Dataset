





import java.util.List;
import java.util.ArrayList;

public class Families_Family extends uncertainty_ModelElement, uncertainty_aFamily {

    private String lastName;
    private String address;





    private aMember amember;




    private List<aMember> amembers;




    private List<aFamily> afamilys;




    private aMember amember;




    private List<aMember> amembers;


    public Families_Family(
        String lastName,        String address    ) {
        super(
        );
        this.lastName = lastName;
        this.address = address;
        this.amembers = new ArrayList<>();
        this.afamilys = new ArrayList<>();
        this.amembers = new ArrayList<>();
    }

    public Families_Family(
        String lastName,        String address        ArrayList<aMember> amembers,        ArrayList<aFamily> afamilys,        ArrayList<aMember> amembers    ) {
        this.lastName = lastName;
        this.address = address;
        this.amembers = amembers;
        this.afamilys = afamilys;
        this.amembers = amembers;
    }

    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public aMember getAmember() {
        return amember;
    }

    public void setAmember(aMember amember) {
        this.amember = amember;
    }
    public List<aMember> getAmembers() {
        return amembers;
    }

    public void addAmember(Amember amember) {
        this.amembers.add(amember);
    }
    public List<aFamily> getAfamilys() {
        return afamilys;
    }

    public void addAfamily(Afamily afamily) {
        this.afamilys.add(afamily);
    }
    public aMember getAmember() {
        return amember;
    }

    public void setAmember(aMember amember) {
        this.amember = amember;
    }
    public List<aMember> getAmembers() {
        return amembers;
    }

    public void addAmember(Amember amember) {
        this.amembers.add(amember);
    }

}