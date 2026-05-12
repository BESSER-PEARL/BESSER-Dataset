




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Oseba2  {

    private LocalDate datumRojstva;
    private String ime;
    private String priimek;



    public Oseba2(
        LocalDate datumRojstva,        String ime,        String priimek    ) {
        this.datumRojstva = datumRojstva;
        this.ime = ime;
        this.priimek = priimek;
    }


    public LocalDate getDatumrojstva() {
        return datumRojstva;
    }

    public void setDatumrojstva(LocalDate datumRojstva) {
        this.datumRojstva = datumRojstva;
    }
    public String getIme() {
        return ime;
    }

    public void setIme(String ime) {
        this.ime = ime;
    }
    public String getPriimek() {
        return priimek;
    }

    public void setPriimek(String priimek) {
        this.priimek = priimek;
    }


}