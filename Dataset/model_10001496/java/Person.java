





import java.util.List;
import java.util.ArrayList;

public class Person  {

    private int Telefonnummer;
    private String Name1;
    private String E_mail;
    private String Name;



    public Person(
        int Telefonnummer,        String Name1,        String E_mail,        String Name    ) {
        this.Telefonnummer = Telefonnummer;
        this.Name1 = Name1;
        this.E_mail = E_mail;
        this.Name = Name;
    }


    public int getTelefonnummer() {
        return Telefonnummer;
    }

    public void setTelefonnummer(int Telefonnummer) {
        this.Telefonnummer = Telefonnummer;
    }
    public String getName1() {
        return Name1;
    }

    public void setName1(String Name1) {
        this.Name1 = Name1;
    }
    public String getE_mail() {
        return E_mail;
    }

    public void setE_mail(String E_mail) {
        this.E_mail = E_mail;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}