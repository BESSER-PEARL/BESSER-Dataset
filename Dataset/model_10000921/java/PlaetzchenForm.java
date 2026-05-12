





import java.util.List;
import java.util.ArrayList;

public class PlaetzchenForm  {

    private None pl_form;
    private String faktor;
    private None pl_groesse;



    public PlaetzchenForm(
        None pl_form,        String faktor,        None pl_groesse    ) {
        this.pl_form = pl_form;
        this.faktor = faktor;
        this.pl_groesse = pl_groesse;
    }


    public None getPl_form() {
        return pl_form;
    }

    public void setPl_form(None pl_form) {
        this.pl_form = pl_form;
    }
    public String getFaktor() {
        return faktor;
    }

    public void setFaktor(String faktor) {
        this.faktor = faktor;
    }
    public None getPl_groesse() {
        return pl_groesse;
    }

    public void setPl_groesse(None pl_groesse) {
        this.pl_groesse = pl_groesse;
    }


}