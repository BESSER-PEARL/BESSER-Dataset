





import java.util.List;
import java.util.ArrayList;

public class p2_IInstallableUnit  {

    private boolean resolved;
    private String filter;
    private boolean singleton;





    private List<p2_IArtifactKey> p2_iartifactkeys;


    public p2_IInstallableUnit(
        boolean resolved,        String filter,        boolean singleton    ) {
        this.resolved = resolved;
        this.filter = filter;
        this.singleton = singleton;
        this.p2_iartifactkeys = new ArrayList<>();
    }

    public p2_IInstallableUnit(
        boolean resolved,        String filter,        boolean singleton        ArrayList<p2_IArtifactKey> p2_iartifactkeys    ) {
        this.resolved = resolved;
        this.filter = filter;
        this.singleton = singleton;
        this.p2_iartifactkeys = p2_iartifactkeys;
    }

    public boolean getResolved() {
        return resolved;
    }

    public void setResolved(boolean resolved) {
        this.resolved = resolved;
    }
    public String getFilter() {
        return filter;
    }

    public void setFilter(String filter) {
        this.filter = filter;
    }
    public boolean getSingleton() {
        return singleton;
    }

    public void setSingleton(boolean singleton) {
        this.singleton = singleton;
    }

    public List<p2_IArtifactKey> getP2_iartifactkeys() {
        return p2_iartifactkeys;
    }

    public void addP2_iartifactkey(P2_iartifactkey p2_iartifactkey) {
        this.p2_iartifactkeys.add(p2_iartifactkey);
    }

}