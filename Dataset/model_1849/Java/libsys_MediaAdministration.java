





import java.util.List;
import java.util.ArrayList;

public class libsys_MediaAdministration  {






    private List<libsys_Medium> libsys_mediums;


    public libsys_MediaAdministration(
    ) {
        this.libsys_mediums = new ArrayList<>();
    }

    public libsys_MediaAdministration(
        ArrayList<libsys_Medium> libsys_mediums    ) {
        this.libsys_mediums = libsys_mediums;
    }


    public List<libsys_Medium> getLibsys_mediums() {
        return libsys_mediums;
    }

    public void addLibsys_medium(Libsys_medium libsys_medium) {
        this.libsys_mediums.add(libsys_medium);
    }

}