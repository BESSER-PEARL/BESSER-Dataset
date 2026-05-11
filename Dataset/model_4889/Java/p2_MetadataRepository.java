





import java.util.List;
import java.util.ArrayList;

public class p2_MetadataRepository  {






    private List<p2_IInstallableUnit> p2_iinstallableunits;




    private List<p2_IRepositoryReference> p2_irepositoryreferences;


    public p2_MetadataRepository(
    ) {
        this.p2_iinstallableunits = new ArrayList<>();
        this.p2_irepositoryreferences = new ArrayList<>();
    }

    public p2_MetadataRepository(
        ArrayList<p2_IInstallableUnit> p2_iinstallableunits,        ArrayList<p2_IRepositoryReference> p2_irepositoryreferences    ) {
        this.p2_iinstallableunits = p2_iinstallableunits;
        this.p2_irepositoryreferences = p2_irepositoryreferences;
    }


    public List<p2_IInstallableUnit> getP2_iinstallableunits() {
        return p2_iinstallableunits;
    }

    public void addP2_iinstallableunit(P2_iinstallableunit p2_iinstallableunit) {
        this.p2_iinstallableunits.add(p2_iinstallableunit);
    }
    public List<p2_IRepositoryReference> getP2_irepositoryreferences() {
        return p2_irepositoryreferences;
    }

    public void addP2_irepositoryreference(P2_irepositoryreference p2_irepositoryreference) {
        this.p2_irepositoryreferences.add(p2_irepositoryreference);
    }

}