





import java.util.List;
import java.util.ArrayList;

public class ecvi_Contact  {

    private String premId;
    private String premName;





    private ecvi_Address ecvi_address;




    private List<ecvi_Person> ecvi_persons;


    public ecvi_Contact(
        String premId,        String premName    ) {
        this.premId = premId;
        this.premName = premName;
        this.ecvi_persons = new ArrayList<>();
    }

    public ecvi_Contact(
        String premId,        String premName        ArrayList<ecvi_Person> ecvi_persons    ) {
        this.premId = premId;
        this.premName = premName;
        this.ecvi_persons = ecvi_persons;
    }

    public String getPremid() {
        return premId;
    }

    public void setPremid(String premId) {
        this.premId = premId;
    }
    public String getPremname() {
        return premName;
    }

    public void setPremname(String premName) {
        this.premName = premName;
    }

    public ecvi_Address getEcvi_address() {
        return ecvi_address;
    }

    public void setEcvi_address(ecvi_Address ecvi_address) {
        this.ecvi_address = ecvi_address;
    }
    public List<ecvi_Person> getEcvi_persons() {
        return ecvi_persons;
    }

    public void addEcvi_person(Ecvi_person ecvi_person) {
        this.ecvi_persons.add(ecvi_person);
    }

}