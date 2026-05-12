





import java.util.List;
import java.util.ArrayList;

public class plaetzchenForm  {

    private None form;
    private None groesse;





    private auftrag auftrag;


    public plaetzchenForm(
        None form,        None groesse    ) {
        this.form = form;
        this.groesse = groesse;
    }


    public None getForm() {
        return form;
    }

    public void setForm(None form) {
        this.form = form;
    }
    public None getGroesse() {
        return groesse;
    }

    public void setGroesse(None groesse) {
        this.groesse = groesse;
    }

    public auftrag getAuftrag() {
        return auftrag;
    }

    public void setAuftrag(auftrag auftrag) {
        this.auftrag = auftrag;
    }

}