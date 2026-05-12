





import java.util.List;
import java.util.ArrayList;

public class Ward  {

    private String location;
    private String name;
    private None staff;
    private int num;
    private None responsable;
    private int telephone_extension;





    private WaitingList waitinglist;




    private ChargeNurse chargenurse;




    private List<RegularDoctor> regulardoctors;


    public Ward(
        String location,        String name,        None staff,        int num,        None responsable,        int telephone_extension    ) {
        this.location = location;
        this.name = name;
        this.staff = staff;
        this.num = num;
        this.responsable = responsable;
        this.telephone_extension = telephone_extension;
        this.regulardoctors = new ArrayList<>();
    }

    public Ward(
        String location,        String name,        None staff,        int num,        None responsable,        int telephone_extension        ArrayList<RegularDoctor> regulardoctors    ) {
        this.location = location;
        this.name = name;
        this.staff = staff;
        this.num = num;
        this.responsable = responsable;
        this.telephone_extension = telephone_extension;
        this.regulardoctors = regulardoctors;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public None getStaff() {
        return staff;
    }

    public void setStaff(None staff) {
        this.staff = staff;
    }
    public int getNum() {
        return num;
    }

    public void setNum(int num) {
        this.num = num;
    }
    public None getResponsable() {
        return responsable;
    }

    public void setResponsable(None responsable) {
        this.responsable = responsable;
    }
    public int getTelephone_extension() {
        return telephone_extension;
    }

    public void setTelephone_extension(int telephone_extension) {
        this.telephone_extension = telephone_extension;
    }

    public WaitingList getWaitinglist() {
        return waitinglist;
    }

    public void setWaitinglist(WaitingList waitinglist) {
        this.waitinglist = waitinglist;
    }
    public ChargeNurse getChargenurse() {
        return chargenurse;
    }

    public void setChargenurse(ChargeNurse chargenurse) {
        this.chargenurse = chargenurse;
    }
    public List<RegularDoctor> getRegulardoctors() {
        return regulardoctors;
    }

    public void addRegulardoctor(Regulardoctor regulardoctor) {
        this.regulardoctors.add(regulardoctor);
    }

}