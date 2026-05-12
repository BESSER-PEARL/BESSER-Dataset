





import java.util.List;
import java.util.ArrayList;

public class pragmacpndefinition_OntologyMember  {






    private List<pragmacpndefinition_Pragma> pragmacpndefinition_pragmas;


    public pragmacpndefinition_OntologyMember(
    ) {
        this.pragmacpndefinition_pragmas = new ArrayList<>();
    }

    public pragmacpndefinition_OntologyMember(
        ArrayList<pragmacpndefinition_Pragma> pragmacpndefinition_pragmas    ) {
        this.pragmacpndefinition_pragmas = pragmacpndefinition_pragmas;
    }


    public List<pragmacpndefinition_Pragma> getPragmacpndefinition_pragmas() {
        return pragmacpndefinition_pragmas;
    }

    public void addPragmacpndefinition_pragma(Pragmacpndefinition_pragma pragmacpndefinition_pragma) {
        this.pragmacpndefinition_pragmas.add(pragmacpndefinition_pragma);
    }

}