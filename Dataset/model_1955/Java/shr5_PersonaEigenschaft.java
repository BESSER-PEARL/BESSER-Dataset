





import java.util.List;
import java.util.ArrayList;

public class shr5_PersonaEigenschaft extends AbstraktModifikatoren, Erlernbar {

    private int karmaKosten;



    public shr5_PersonaEigenschaft(
        int karmaKosten    ) {
        super(
        );
        this.karmaKosten = karmaKosten;
    }


    public int getKarmakosten() {
        return karmaKosten;
    }

    public void setKarmakosten(int karmaKosten) {
        this.karmaKosten = karmaKosten;
    }


}