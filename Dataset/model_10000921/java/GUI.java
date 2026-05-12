





import java.util.List;
import java.util.ArrayList;

public class GUI  {

    private None gussList;
    private None groesse;
    private None dekorList;
    private String plaetzchenname;
    private None deko;
    private None zutatenList;
    private String dateiname;
    private None teigsorte;
    private String stueckzahl;
    private None plaetzchen;
    private None teigList;
    private None guss;
    private String attribute;
    private None plformList;
    private None datei;
    private None form;





    private Zutat zutat;




    private PlaetzchenForm plaetzchenform;


    public GUI(
        None gussList,        None groesse,        None dekorList,        String plaetzchenname,        None deko,        None zutatenList,        String dateiname,        None teigsorte,        String stueckzahl,        None plaetzchen,        None teigList,        None guss,        String attribute,        None plformList,        None datei,        None form    ) {
        this.gussList = gussList;
        this.groesse = groesse;
        this.dekorList = dekorList;
        this.plaetzchenname = plaetzchenname;
        this.deko = deko;
        this.zutatenList = zutatenList;
        this.dateiname = dateiname;
        this.teigsorte = teigsorte;
        this.stueckzahl = stueckzahl;
        this.plaetzchen = plaetzchen;
        this.teigList = teigList;
        this.guss = guss;
        this.attribute = attribute;
        this.plformList = plformList;
        this.datei = datei;
        this.form = form;
    }


    public None getGusslist() {
        return gussList;
    }

    public void setGusslist(None gussList) {
        this.gussList = gussList;
    }
    public None getGroesse() {
        return groesse;
    }

    public void setGroesse(None groesse) {
        this.groesse = groesse;
    }
    public None getDekorlist() {
        return dekorList;
    }

    public void setDekorlist(None dekorList) {
        this.dekorList = dekorList;
    }
    public String getPlaetzchenname() {
        return plaetzchenname;
    }

    public void setPlaetzchenname(String plaetzchenname) {
        this.plaetzchenname = plaetzchenname;
    }
    public None getDeko() {
        return deko;
    }

    public void setDeko(None deko) {
        this.deko = deko;
    }
    public None getZutatenlist() {
        return zutatenList;
    }

    public void setZutatenlist(None zutatenList) {
        this.zutatenList = zutatenList;
    }
    public String getDateiname() {
        return dateiname;
    }

    public void setDateiname(String dateiname) {
        this.dateiname = dateiname;
    }
    public None getTeigsorte() {
        return teigsorte;
    }

    public void setTeigsorte(None teigsorte) {
        this.teigsorte = teigsorte;
    }
    public String getStueckzahl() {
        return stueckzahl;
    }

    public void setStueckzahl(String stueckzahl) {
        this.stueckzahl = stueckzahl;
    }
    public None getPlaetzchen() {
        return plaetzchen;
    }

    public void setPlaetzchen(None plaetzchen) {
        this.plaetzchen = plaetzchen;
    }
    public None getTeiglist() {
        return teigList;
    }

    public void setTeiglist(None teigList) {
        this.teigList = teigList;
    }
    public None getGuss() {
        return guss;
    }

    public void setGuss(None guss) {
        this.guss = guss;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public None getPlformlist() {
        return plformList;
    }

    public void setPlformlist(None plformList) {
        this.plformList = plformList;
    }
    public None getDatei() {
        return datei;
    }

    public void setDatei(None datei) {
        this.datei = datei;
    }
    public None getForm() {
        return form;
    }

    public void setForm(None form) {
        this.form = form;
    }

    public Zutat getZutat() {
        return zutat;
    }

    public void setZutat(Zutat zutat) {
        this.zutat = zutat;
    }
    public PlaetzchenForm getPlaetzchenform() {
        return plaetzchenform;
    }

    public void setPlaetzchenform(PlaetzchenForm plaetzchenform) {
        this.plaetzchenform = plaetzchenform;
    }

}