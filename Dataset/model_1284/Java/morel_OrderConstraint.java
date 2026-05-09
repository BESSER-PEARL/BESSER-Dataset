





import java.util.List;
import java.util.ArrayList;

public class morel_OrderConstraint extends AdditionalConstraint {






    private List<morel_EClass> morel_eclasss;




    private List<morel_EReference> morel_ereferences;




    private morel_ObjectVariable morel_objectvariable;


    public morel_OrderConstraint(
    ) {
        super(
        );
        this.morel_eclasss = new ArrayList<>();
        this.morel_ereferences = new ArrayList<>();
    }

    public morel_OrderConstraint(
        ArrayList<morel_EClass> morel_eclasss,        ArrayList<morel_EReference> morel_ereferences    ) {
        this.morel_eclasss = morel_eclasss;
        this.morel_ereferences = morel_ereferences;
    }


    public List<morel_EClass> getMorel_eclasss() {
        return morel_eclasss;
    }

    public void addMorel_eclass(Morel_eclass morel_eclass) {
        this.morel_eclasss.add(morel_eclass);
    }
    public List<morel_EReference> getMorel_ereferences() {
        return morel_ereferences;
    }

    public void addMorel_ereference(Morel_ereference morel_ereference) {
        this.morel_ereferences.add(morel_ereference);
    }
    public morel_ObjectVariable getMorel_objectvariable() {
        return morel_objectvariable;
    }

    public void setMorel_objectvariable(morel_ObjectVariable morel_objectvariable) {
        this.morel_objectvariable = morel_objectvariable;
    }

}