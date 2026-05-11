





import java.util.List;
import java.util.ArrayList;

public class oclstdlibcs_LibPackageCS extends PackageCS {






    private List<oclstdlibcs_PrecedenceCS> oclstdlibcs_precedencecss;


    public oclstdlibcs_LibPackageCS(
    ) {
        super(
        );
        this.oclstdlibcs_precedencecss = new ArrayList<>();
    }

    public oclstdlibcs_LibPackageCS(
        ArrayList<oclstdlibcs_PrecedenceCS> oclstdlibcs_precedencecss    ) {
        this.oclstdlibcs_precedencecss = oclstdlibcs_precedencecss;
    }


    public List<oclstdlibcs_PrecedenceCS> getOclstdlibcs_precedencecss() {
        return oclstdlibcs_precedencecss;
    }

    public void addOclstdlibcs_precedencecs(Oclstdlibcs_precedencecs oclstdlibcs_precedencecs) {
        this.oclstdlibcs_precedencecss.add(oclstdlibcs_precedencecs);
    }

}