





import java.util.List;
import java.util.ArrayList;

public class etrace_CompositeLink extends AbstractLink {






    private List<etrace_AbstractLink> etrace_abstractlinks;


    public etrace_CompositeLink(
    ) {
        super(
        );
        this.etrace_abstractlinks = new ArrayList<>();
    }

    public etrace_CompositeLink(
        ArrayList<etrace_AbstractLink> etrace_abstractlinks    ) {
        this.etrace_abstractlinks = etrace_abstractlinks;
    }


    public List<etrace_AbstractLink> getEtrace_abstractlinks() {
        return etrace_abstractlinks;
    }

    public void addEtrace_abstractlink(Etrace_abstractlink etrace_abstractlink) {
        this.etrace_abstractlinks.add(etrace_abstractlink);
    }

}