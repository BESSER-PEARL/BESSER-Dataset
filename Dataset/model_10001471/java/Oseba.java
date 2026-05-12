





import java.util.List;
import java.util.ArrayList;

public class Oseba  {

    private String ime;
    private String priimek;
    private String spol;
    private None datumRojstva;



    public Oseba(
        String ime,        String priimek,        String spol,        None datumRojstva    ) {
        this.ime = ime;
        this.priimek = priimek;
        this.spol = spol;
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
    public String getSpol() {
        return spol;
    }

    public void setSpol(String spol) {
        this.spol = spol;
    }
    public None getDatumrojstva() {
        return datumRojstva;
    }

    public void setDatumrojstva(None datumRojstva) {
        this.datumRojstva = datumRojstva;
    }


}