





import java.util.List;
import java.util.ArrayList;

public class auftrag  {

    private String name;
    private String backzeit;
    private None pteig;
    private None backofen;
    private String attribute;
    private None pteigmaschine;
    private String menge;
    private None pform;
    private None belagmaschine;
    private None pguss;
    private None pdeko;
    private String backtemp;





    private plaetzchen plaetzchen;




    private lager lager;




    private teig teig;


    public auftrag(
        String name,        String backzeit,        None pteig,        None backofen,        String attribute,        None pteigmaschine,        String menge,        None pform,        None belagmaschine,        None pguss,        None pdeko,        String backtemp    ) {
        this.name = name;
        this.backzeit = backzeit;
        this.pteig = pteig;
        this.backofen = backofen;
        this.attribute = attribute;
        this.pteigmaschine = pteigmaschine;
        this.menge = menge;
        this.pform = pform;
        this.belagmaschine = belagmaschine;
        this.pguss = pguss;
        this.pdeko = pdeko;
        this.backtemp = backtemp;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getBackzeit() {
        return backzeit;
    }

    public void setBackzeit(String backzeit) {
        this.backzeit = backzeit;
    }
    public None getPteig() {
        return pteig;
    }

    public void setPteig(None pteig) {
        this.pteig = pteig;
    }
    public None getBackofen() {
        return backofen;
    }

    public void setBackofen(None backofen) {
        this.backofen = backofen;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public None getPteigmaschine() {
        return pteigmaschine;
    }

    public void setPteigmaschine(None pteigmaschine) {
        this.pteigmaschine = pteigmaschine;
    }
    public String getMenge() {
        return menge;
    }

    public void setMenge(String menge) {
        this.menge = menge;
    }
    public None getPform() {
        return pform;
    }

    public void setPform(None pform) {
        this.pform = pform;
    }
    public None getBelagmaschine() {
        return belagmaschine;
    }

    public void setBelagmaschine(None belagmaschine) {
        this.belagmaschine = belagmaschine;
    }
    public None getPguss() {
        return pguss;
    }

    public void setPguss(None pguss) {
        this.pguss = pguss;
    }
    public None getPdeko() {
        return pdeko;
    }

    public void setPdeko(None pdeko) {
        this.pdeko = pdeko;
    }
    public String getBacktemp() {
        return backtemp;
    }

    public void setBacktemp(String backtemp) {
        this.backtemp = backtemp;
    }

    public plaetzchen getPlaetzchen() {
        return plaetzchen;
    }

    public void setPlaetzchen(plaetzchen plaetzchen) {
        this.plaetzchen = plaetzchen;
    }
    public lager getLager() {
        return lager;
    }

    public void setLager(lager lager) {
        this.lager = lager;
    }
    public teig getTeig() {
        return teig;
    }

    public void setTeig(teig teig) {
        this.teig = teig;
    }

}