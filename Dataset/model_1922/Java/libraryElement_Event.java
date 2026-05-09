





import java.util.List;
import java.util.ArrayList;

public class libraryElement_Event extends IInterfaceElement {






    private libraryElement_ECTransition libraryelement_ectransition;




    private libraryElement_ECAction libraryelement_ecaction;


    public libraryElement_Event(
    ) {
        super(
        );
    }



    public libraryElement_ECTransition getLibraryelement_ectransition() {
        return libraryelement_ectransition;
    }

    public void setLibraryelement_ectransition(libraryElement_ECTransition libraryelement_ectransition) {
        this.libraryelement_ectransition = libraryelement_ectransition;
    }
    public libraryElement_ECAction getLibraryelement_ecaction() {
        return libraryelement_ecaction;
    }

    public void setLibraryelement_ecaction(libraryElement_ECAction libraryelement_ecaction) {
        this.libraryelement_ecaction = libraryelement_ecaction;
    }

}