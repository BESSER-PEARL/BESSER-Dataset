





import java.util.List;
import java.util.ArrayList;

public class afpText_BandImage extends triplet {

    private String BCOUNT;





    private List<afpText_BandImageRG> afptext_bandimagergs;


    public afpText_BandImage(
        String BCOUNT    ) {
        super(
        );
        this.BCOUNT = BCOUNT;
        this.afptext_bandimagergs = new ArrayList<>();
    }

    public afpText_BandImage(
        String BCOUNT        ArrayList<afpText_BandImageRG> afptext_bandimagergs    ) {
        this.BCOUNT = BCOUNT;
        this.afptext_bandimagergs = afptext_bandimagergs;
    }

    public String getBcount() {
        return BCOUNT;
    }

    public void setBcount(String BCOUNT) {
        this.BCOUNT = BCOUNT;
    }

    public List<afpText_BandImageRG> getAfptext_bandimagergs() {
        return afptext_bandimagergs;
    }

    public void addAfptext_bandimagerg(Afptext_bandimagerg afptext_bandimagerg) {
        this.afptext_bandimagergs.add(afptext_bandimagerg);
    }

}