




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class zlvp_Verleih  {

    private String bemerkung;
    private String person;
    private LocalDate datum;
    private int id;



    public zlvp_Verleih(
        String bemerkung,        String person,        LocalDate datum,        int id    ) {
        this.bemerkung = bemerkung;
        this.person = person;
        this.datum = datum;
        this.id = id;
    }


    public String getBemerkung() {
        return bemerkung;
    }

    public void setBemerkung(String bemerkung) {
        this.bemerkung = bemerkung;
    }
    public String getPerson() {
        return person;
    }

    public void setPerson(String person) {
        this.person = person;
    }
    public LocalDate getDatum() {
        return datum;
    }

    public void setDatum(LocalDate datum) {
        this.datum = datum;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}