





import java.util.List;
import java.util.ArrayList;

public class shr5_RiggerCommandConsole extends AbstractMatrixDevice {

    private int zugriffBasis;
    private int firewallBasis;
    private int rauschunterdrueckung;
    private int zugriff;
    private int datenverarbeitungBasis;





    private List<shr5_RiggerProgram> shr5_riggerprograms;




    private List<shr5_RiggerProgram> shr5_riggerprograms;


    public shr5_RiggerCommandConsole(
        int zugriffBasis,        int firewallBasis,        int rauschunterdrueckung,        int zugriff,        int datenverarbeitungBasis    ) {
        super(
        );
        this.zugriffBasis = zugriffBasis;
        this.firewallBasis = firewallBasis;
        this.rauschunterdrueckung = rauschunterdrueckung;
        this.zugriff = zugriff;
        this.datenverarbeitungBasis = datenverarbeitungBasis;
        this.shr5_riggerprograms = new ArrayList<>();
        this.shr5_riggerprograms = new ArrayList<>();
    }

    public shr5_RiggerCommandConsole(
        int zugriffBasis,        int firewallBasis,        int rauschunterdrueckung,        int zugriff,        int datenverarbeitungBasis        ArrayList<shr5_RiggerProgram> shr5_riggerprograms,        ArrayList<shr5_RiggerProgram> shr5_riggerprograms    ) {
        this.zugriffBasis = zugriffBasis;
        this.firewallBasis = firewallBasis;
        this.rauschunterdrueckung = rauschunterdrueckung;
        this.zugriff = zugriff;
        this.datenverarbeitungBasis = datenverarbeitungBasis;
        this.shr5_riggerprograms = shr5_riggerprograms;
        this.shr5_riggerprograms = shr5_riggerprograms;
    }

    public int getZugriffbasis() {
        return zugriffBasis;
    }

    public void setZugriffbasis(int zugriffBasis) {
        this.zugriffBasis = zugriffBasis;
    }
    public int getFirewallbasis() {
        return firewallBasis;
    }

    public void setFirewallbasis(int firewallBasis) {
        this.firewallBasis = firewallBasis;
    }
    public int getRauschunterdrueckung() {
        return rauschunterdrueckung;
    }

    public void setRauschunterdrueckung(int rauschunterdrueckung) {
        this.rauschunterdrueckung = rauschunterdrueckung;
    }
    public int getZugriff() {
        return zugriff;
    }

    public void setZugriff(int zugriff) {
        this.zugriff = zugriff;
    }
    public int getDatenverarbeitungbasis() {
        return datenverarbeitungBasis;
    }

    public void setDatenverarbeitungbasis(int datenverarbeitungBasis) {
        this.datenverarbeitungBasis = datenverarbeitungBasis;
    }

    public List<shr5_RiggerProgram> getShr5_riggerprograms() {
        return shr5_riggerprograms;
    }

    public void addShr5_riggerprogram(Shr5_riggerprogram shr5_riggerprogram) {
        this.shr5_riggerprograms.add(shr5_riggerprogram);
    }
    public List<shr5_RiggerProgram> getShr5_riggerprograms() {
        return shr5_riggerprograms;
    }

    public void addShr5_riggerprogram(Shr5_riggerprogram shr5_riggerprogram) {
        this.shr5_riggerprograms.add(shr5_riggerprogram);
    }

}