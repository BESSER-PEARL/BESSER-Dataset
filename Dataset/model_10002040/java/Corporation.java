





import java.util.List;
import java.util.ArrayList;

public class Corporation  {

    private String address;
    private int no;
    private String name;





    private List<Personel> personels;




    private List<Personel> personels;


    public Corporation(
        String address,        int no,        String name    ) {
        this.address = address;
        this.no = no;
        this.name = name;
        this.personels = new ArrayList<>();
        this.personels = new ArrayList<>();
    }

    public Corporation(
        String address,        int no,        String name        ArrayList<Personel> personels,        ArrayList<Personel> personels    ) {
        this.address = address;
        this.no = no;
        this.name = name;
        this.personels = personels;
        this.personels = personels;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public int getNo() {
        return no;
    }

    public void setNo(int no) {
        this.no = no;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Personel> getPersonels() {
        return personels;
    }

    public void addPersonel(Personel personel) {
        this.personels.add(personel);
    }
    public List<Personel> getPersonels() {
        return personels;
    }

    public void addPersonel(Personel personel) {
        this.personels.add(personel);
    }

}