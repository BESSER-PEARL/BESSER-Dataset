





import java.util.List;
import java.util.ArrayList;

public class shr5_Kleidung extends AbstraktGegenstand, Capacity {

    private int ruestung;





    private List<shr5_KleindungsModifikator> shr5_kleindungsmodifikators;


    public shr5_Kleidung(
        int ruestung    ) {
        super(
        );
        this.ruestung = ruestung;
        this.shr5_kleindungsmodifikators = new ArrayList<>();
    }

    public shr5_Kleidung(
        int ruestung        ArrayList<shr5_KleindungsModifikator> shr5_kleindungsmodifikators    ) {
        this.ruestung = ruestung;
        this.shr5_kleindungsmodifikators = shr5_kleindungsmodifikators;
    }

    public int getRuestung() {
        return ruestung;
    }

    public void setRuestung(int ruestung) {
        this.ruestung = ruestung;
    }

    public List<shr5_KleindungsModifikator> getShr5_kleindungsmodifikators() {
        return shr5_kleindungsmodifikators;
    }

    public void addShr5_kleindungsmodifikator(Shr5_kleindungsmodifikator shr5_kleindungsmodifikator) {
        this.shr5_kleindungsmodifikators.add(shr5_kleindungsmodifikator);
    }

}