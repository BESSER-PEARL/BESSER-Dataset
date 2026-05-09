





import java.util.List;
import java.util.ArrayList;

public class libraryElement_ECC  {






    private List<libraryElement_ECState> libraryelement_ecstates;




    private libraryElement_ECState libraryelement_ecstate;




    private libraryElement_BasicFBType libraryelement_basicfbtype;


    public libraryElement_ECC(
    ) {
        this.libraryelement_ecstates = new ArrayList<>();
    }

    public libraryElement_ECC(
        ArrayList<libraryElement_ECState> libraryelement_ecstates    ) {
        this.libraryelement_ecstates = libraryelement_ecstates;
    }


    public List<libraryElement_ECState> getLibraryelement_ecstates() {
        return libraryelement_ecstates;
    }

    public void addLibraryelement_ecstate(Libraryelement_ecstate libraryelement_ecstate) {
        this.libraryelement_ecstates.add(libraryelement_ecstate);
    }
    public libraryElement_ECState getLibraryelement_ecstate() {
        return libraryelement_ecstate;
    }

    public void setLibraryelement_ecstate(libraryElement_ECState libraryelement_ecstate) {
        this.libraryelement_ecstate = libraryelement_ecstate;
    }
    public libraryElement_BasicFBType getLibraryelement_basicfbtype() {
        return libraryelement_basicfbtype;
    }

    public void setLibraryelement_basicfbtype(libraryElement_BasicFBType libraryelement_basicfbtype) {
        this.libraryelement_basicfbtype = libraryelement_basicfbtype;
    }

}