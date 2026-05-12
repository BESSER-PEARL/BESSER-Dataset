





import java.util.List;
import java.util.ArrayList;

public class Student  {

    private int Durchschnittsnote;
    private int Martikelnummer;



    public Student(
        int Durchschnittsnote,        int Martikelnummer    ) {
        this.Durchschnittsnote = Durchschnittsnote;
        this.Martikelnummer = Martikelnummer;
    }


    public int getDurchschnittsnote() {
        return Durchschnittsnote;
    }

    public void setDurchschnittsnote(int Durchschnittsnote) {
        this.Durchschnittsnote = Durchschnittsnote;
    }
    public int getMartikelnummer() {
        return Martikelnummer;
    }

    public void setMartikelnummer(int Martikelnummer) {
        this.Martikelnummer = Martikelnummer;
    }


}