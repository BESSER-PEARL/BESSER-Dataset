





import java.util.List;
import java.util.ArrayList;

public class teig  {

    private String zutaten;
    private String attribute;
    private String name;
    private None form;
    private String menge;





    private lager lager;


    public teig(
        String zutaten,        String attribute,        String name,        None form,        String menge    ) {
        this.zutaten = zutaten;
        this.attribute = attribute;
        this.name = name;
        this.form = form;
        this.menge = menge;
    }


    public String getZutaten() {
        return zutaten;
    }

    public void setZutaten(String zutaten) {
        this.zutaten = zutaten;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public None getForm() {
        return form;
    }

    public void setForm(None form) {
        this.form = form;
    }
    public String getMenge() {
        return menge;
    }

    public void setMenge(String menge) {
        this.menge = menge;
    }

    public lager getLager() {
        return lager;
    }

    public void setLager(lager lager) {
        this.lager = lager;
    }

}