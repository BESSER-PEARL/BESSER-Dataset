





import java.util.List;
import java.util.ArrayList;

public class Plaetzchen  {

    private None deko;
    private None name;
    private int menge;
    private String rezeptDeko;
    private None form;
    private None teig;
    private None rezeptTeig;
    private None guss;
    private String rezeptGuss;





    private PlaetzchenForm plaetzchenform;


    public Plaetzchen(
        None deko,        None name,        int menge,        String rezeptDeko,        None form,        None teig,        None rezeptTeig,        None guss,        String rezeptGuss    ) {
        this.deko = deko;
        this.name = name;
        this.menge = menge;
        this.rezeptDeko = rezeptDeko;
        this.form = form;
        this.teig = teig;
        this.rezeptTeig = rezeptTeig;
        this.guss = guss;
        this.rezeptGuss = rezeptGuss;
    }


    public None getDeko() {
        return deko;
    }

    public void setDeko(None deko) {
        this.deko = deko;
    }
    public None getName() {
        return name;
    }

    public void setName(None name) {
        this.name = name;
    }
    public int getMenge() {
        return menge;
    }

    public void setMenge(int menge) {
        this.menge = menge;
    }
    public String getRezeptdeko() {
        return rezeptDeko;
    }

    public void setRezeptdeko(String rezeptDeko) {
        this.rezeptDeko = rezeptDeko;
    }
    public None getForm() {
        return form;
    }

    public void setForm(None form) {
        this.form = form;
    }
    public None getTeig() {
        return teig;
    }

    public void setTeig(None teig) {
        this.teig = teig;
    }
    public None getRezeptteig() {
        return rezeptTeig;
    }

    public void setRezeptteig(None rezeptTeig) {
        this.rezeptTeig = rezeptTeig;
    }
    public None getGuss() {
        return guss;
    }

    public void setGuss(None guss) {
        this.guss = guss;
    }
    public String getRezeptguss() {
        return rezeptGuss;
    }

    public void setRezeptguss(String rezeptGuss) {
        this.rezeptGuss = rezeptGuss;
    }

    public PlaetzchenForm getPlaetzchenform() {
        return plaetzchenform;
    }

    public void setPlaetzchenform(PlaetzchenForm plaetzchenform) {
        this.plaetzchenform = plaetzchenform;
    }

}