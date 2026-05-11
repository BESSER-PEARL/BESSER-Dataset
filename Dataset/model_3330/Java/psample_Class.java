





import java.util.List;
import java.util.ArrayList;

public class psample_Class extends TypedElement {






    private List<psample_PrimitiveTypeVariable> psample_primitivetypevariables;




    private List<psample_Member> psample_members;


    public psample_Class(
    ) {
        super(
        );
        this.psample_primitivetypevariables = new ArrayList<>();
        this.psample_members = new ArrayList<>();
    }

    public psample_Class(
        ArrayList<psample_PrimitiveTypeVariable> psample_primitivetypevariables,        ArrayList<psample_Member> psample_members    ) {
        this.psample_primitivetypevariables = psample_primitivetypevariables;
        this.psample_members = psample_members;
    }


    public List<psample_PrimitiveTypeVariable> getPsample_primitivetypevariables() {
        return psample_primitivetypevariables;
    }

    public void addPsample_primitivetypevariable(Psample_primitivetypevariable psample_primitivetypevariable) {
        this.psample_primitivetypevariables.add(psample_primitivetypevariable);
    }
    public List<psample_Member> getPsample_members() {
        return psample_members;
    }

    public void addPsample_member(Psample_member psample_member) {
        this.psample_members.add(psample_member);
    }

}