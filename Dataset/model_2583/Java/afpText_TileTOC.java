





import java.util.List;
import java.util.ArrayList;

public class afpText_TileTOC extends triplet {

    private String Reserved;





    private List<afpText_TileTOCRG> afptext_tiletocrgs;


    public afpText_TileTOC(
        String Reserved    ) {
        super(
        );
        this.Reserved = Reserved;
        this.afptext_tiletocrgs = new ArrayList<>();
    }

    public afpText_TileTOC(
        String Reserved        ArrayList<afpText_TileTOCRG> afptext_tiletocrgs    ) {
        this.Reserved = Reserved;
        this.afptext_tiletocrgs = afptext_tiletocrgs;
    }

    public String getReserved() {
        return Reserved;
    }

    public void setReserved(String Reserved) {
        this.Reserved = Reserved;
    }

    public List<afpText_TileTOCRG> getAfptext_tiletocrgs() {
        return afptext_tiletocrgs;
    }

    public void addAfptext_tiletocrg(Afptext_tiletocrg afptext_tiletocrg) {
        this.afptext_tiletocrgs.add(afptext_tiletocrg);
    }

}