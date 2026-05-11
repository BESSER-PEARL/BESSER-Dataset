





import java.util.List;
import java.util.ArrayList;

public class delphi_methodList extends CSTrace {






    private delphi_objectType delphi_objecttype;




    private List<delphi_directive> delphi_directives;


    public delphi_methodList(
    ) {
        super(
        );
        this.delphi_directives = new ArrayList<>();
    }

    public delphi_methodList(
        ArrayList<delphi_directive> delphi_directives    ) {
        this.delphi_directives = delphi_directives;
    }


    public delphi_objectType getDelphi_objecttype() {
        return delphi_objecttype;
    }

    public void setDelphi_objecttype(delphi_objectType delphi_objecttype) {
        this.delphi_objecttype = delphi_objecttype;
    }
    public List<delphi_directive> getDelphi_directives() {
        return delphi_directives;
    }

    public void addDelphi_directive(Delphi_directive delphi_directive) {
        this.delphi_directives.add(delphi_directive);
    }

}