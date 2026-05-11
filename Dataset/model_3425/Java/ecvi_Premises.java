





import java.util.List;
import java.util.ArrayList;

public class ecvi_Premises  {

    private String premId;
    private String premName;





    private ecvi_Ecvi ecvi_ecvi;




    private ecvi_Ecvi ecvi_ecvi;




    private List<ecvi_Person> ecvi_persons;




    private ecvi_Address ecvi_address;


    public ecvi_Premises(
        String premId,        String premName    ) {
        this.premId = premId;
        this.premName = premName;
        this.ecvi_persons = new ArrayList<>();
    }

    public ecvi_Premises(
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

    public ecvi_Ecvi getEcvi_ecvi() {
        return ecvi_ecvi;
    }

    public void setEcvi_ecvi(ecvi_Ecvi ecvi_ecvi) {
        this.ecvi_ecvi = ecvi_ecvi;
    }
    public ecvi_Ecvi getEcvi_ecvi() {
        return ecvi_ecvi;
    }

    public void setEcvi_ecvi(ecvi_Ecvi ecvi_ecvi) {
        this.ecvi_ecvi = ecvi_ecvi;
    }
    public List<ecvi_Person> getEcvi_persons() {
        return ecvi_persons;
    }

    public void addEcvi_person(Ecvi_person ecvi_person) {
        this.ecvi_persons.add(ecvi_person);
    }
    public ecvi_Address getEcvi_address() {
        return ecvi_address;
    }

    public void setEcvi_address(ecvi_Address ecvi_address) {
        this.ecvi_address = ecvi_address;
    }

}