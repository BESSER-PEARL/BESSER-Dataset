





import java.util.List;
import java.util.ArrayList;

public class afpText_GRLINE extends triplet {

    private String XPOS;
    private String YPOS;





    private List<afpText_GRLINERG> afptext_grlinergs;


    public afpText_GRLINE(
        String XPOS,        String YPOS    ) {
        super(
        );
        this.XPOS = XPOS;
        this.YPOS = YPOS;
        this.afptext_grlinergs = new ArrayList<>();
    }

    public afpText_GRLINE(
        String XPOS,        String YPOS        ArrayList<afpText_GRLINERG> afptext_grlinergs    ) {
        this.XPOS = XPOS;
        this.YPOS = YPOS;
        this.afptext_grlinergs = afptext_grlinergs;
    }

    public String getXpos() {
        return XPOS;
    }

    public void setXpos(String XPOS) {
        this.XPOS = XPOS;
    }
    public String getYpos() {
        return YPOS;
    }

    public void setYpos(String YPOS) {
        this.YPOS = YPOS;
    }

    public List<afpText_GRLINERG> getAfptext_grlinergs() {
        return afptext_grlinergs;
    }

    public void addAfptext_grlinerg(Afptext_grlinerg afptext_grlinerg) {
        this.afptext_grlinergs.add(afptext_grlinerg);
    }

}