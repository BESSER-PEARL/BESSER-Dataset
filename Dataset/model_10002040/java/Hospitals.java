





import java.util.List;
import java.util.ArrayList;

public class Hospitals  {

    private String name;
    private int no;
    private String address;
    private String type;





    private List<Personel> personels;




    private Personel personel;


    public Hospitals(
        String name,        int no,        String address,        String type    ) {
        this.name = name;
        this.no = no;
        this.address = address;
        this.type = type;
        this.personels = new ArrayList<>();
    }

    public Hospitals(
        String name,        int no,        String address,        String type        ArrayList<Personel> personels    ) {
        this.name = name;
        this.no = no;
        this.address = address;
        this.type = type;
        this.personels = personels;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getNo() {
        return no;
    }

    public void setNo(int no) {
        this.no = no;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<Personel> getPersonels() {
        return personels;
    }

    public void addPersonel(Personel personel) {
        this.personels.add(personel);
    }
    public Personel getPersonel() {
        return personel;
    }

    public void setPersonel(Personel personel) {
        this.personel = personel;
    }

}