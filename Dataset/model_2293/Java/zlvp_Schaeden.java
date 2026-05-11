




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class zlvp_Schaeden  {

    private LocalDate datum;
    private int id;
    private String bezeichnung;



    public zlvp_Schaeden(
        LocalDate datum,        int id,        String bezeichnung    ) {
        this.datum = datum;
        this.id = id;
        this.bezeichnung = bezeichnung;
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
    public String getBezeichnung() {
        return bezeichnung;
    }

    public void setBezeichnung(String bezeichnung) {
        this.bezeichnung = bezeichnung;
    }


}