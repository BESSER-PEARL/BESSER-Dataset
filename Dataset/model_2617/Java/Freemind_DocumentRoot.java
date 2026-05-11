





import java.util.List;
import java.util.ArrayList;

public class Freemind_DocumentRoot  {

    private String mixed;





    private List<Freemind_ArrowlinkType> freemind_arrowlinktypes;


    public Freemind_DocumentRoot(
        String mixed    ) {
        this.mixed = mixed;
        this.freemind_arrowlinktypes = new ArrayList<>();
    }

    public Freemind_DocumentRoot(
        String mixed        ArrayList<Freemind_ArrowlinkType> freemind_arrowlinktypes    ) {
        this.mixed = mixed;
        this.freemind_arrowlinktypes = freemind_arrowlinktypes;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<Freemind_ArrowlinkType> getFreemind_arrowlinktypes() {
        return freemind_arrowlinktypes;
    }

    public void addFreemind_arrowlinktype(Freemind_arrowlinktype freemind_arrowlinktype) {
        this.freemind_arrowlinktypes.add(freemind_arrowlinktype);
    }

}