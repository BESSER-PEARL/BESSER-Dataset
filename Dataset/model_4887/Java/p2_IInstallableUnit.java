





import java.util.List;
import java.util.ArrayList;

public class p2_IInstallableUnit  {

    private boolean singleton;
    private boolean resolved;
    private String filter;





    private p2_ICopyright p2_icopyright;




    private List<p2_IArtifactKey> p2_iartifactkeys;


    public p2_IInstallableUnit(
        boolean singleton,        boolean resolved,        String filter    ) {
        this.singleton = singleton;
        this.resolved = resolved;
        this.filter = filter;
        this.p2_iartifactkeys = new ArrayList<>();
    }

    public p2_IInstallableUnit(
        boolean singleton,        boolean resolved,        String filter        ArrayList<p2_IArtifactKey> p2_iartifactkeys    ) {
        this.singleton = singleton;
        this.resolved = resolved;
        this.filter = filter;
        this.p2_iartifactkeys = p2_iartifactkeys;
    }

    public boolean getSingleton() {
        return singleton;
    }

    public void setSingleton(boolean singleton) {
        this.singleton = singleton;
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

    public p2_ICopyright getP2_icopyright() {
        return p2_icopyright;
    }

    public void setP2_icopyright(p2_ICopyright p2_icopyright) {
        this.p2_icopyright = p2_icopyright;
    }
    public List<p2_IArtifactKey> getP2_iartifactkeys() {
        return p2_iartifactkeys;
    }

    public void addP2_iartifactkey(P2_iartifactkey p2_iartifactkey) {
        this.p2_iartifactkeys.add(p2_iartifactkey);
    }

}