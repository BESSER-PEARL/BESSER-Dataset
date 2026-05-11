





import java.util.List;
import java.util.ArrayList;

public class Kasu11_ClassB  {

    private String Name;





    private Kasu11_ClassA kasu11_classa;




    private Kasu11_ClassA kasu11_classa;




    private List<Kasu11_ClassC> kasu11_classcs;




    private Kasu11_ClassC kasu11_classc;


    public Kasu11_ClassB(
        String Name    ) {
        this.Name = Name;
        this.kasu11_classcs = new ArrayList<>();
    }

    public Kasu11_ClassB(
        String Name        ArrayList<Kasu11_ClassC> kasu11_classcs    ) {
        this.Name = Name;
        this.kasu11_classcs = kasu11_classcs;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public Kasu11_ClassA getKasu11_classa() {
        return kasu11_classa;
    }

    public void setKasu11_classa(Kasu11_ClassA kasu11_classa) {
        this.kasu11_classa = kasu11_classa;
    }
    public Kasu11_ClassA getKasu11_classa() {
        return kasu11_classa;
    }

    public void setKasu11_classa(Kasu11_ClassA kasu11_classa) {
        this.kasu11_classa = kasu11_classa;
    }
    public List<Kasu11_ClassC> getKasu11_classcs() {
        return kasu11_classcs;
    }

    public void addKasu11_classc(Kasu11_classc kasu11_classc) {
        this.kasu11_classcs.add(kasu11_classc);
    }
    public Kasu11_ClassC getKasu11_classc() {
        return kasu11_classc;
    }

    public void setKasu11_classc(Kasu11_ClassC kasu11_classc) {
        this.kasu11_classc = kasu11_classc;
    }

}