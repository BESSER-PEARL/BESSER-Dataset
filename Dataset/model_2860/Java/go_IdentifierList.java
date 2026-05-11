





import java.util.List;
import java.util.ArrayList;

public class go_IdentifierList  {






    private go_ParameterDecl go_parameterdecl;




    private List<go_identifier> go_identifiers;




    private go_FieldDecl go_fielddecl;


    public go_IdentifierList(
    ) {
        this.go_identifiers = new ArrayList<>();
    }

    public go_IdentifierList(
        ArrayList<go_identifier> go_identifiers    ) {
        this.go_identifiers = go_identifiers;
    }


    public go_ParameterDecl getGo_parameterdecl() {
        return go_parameterdecl;
    }

    public void setGo_parameterdecl(go_ParameterDecl go_parameterdecl) {
        this.go_parameterdecl = go_parameterdecl;
    }
    public List<go_identifier> getGo_identifiers() {
        return go_identifiers;
    }

    public void addGo_identifier(Go_identifier go_identifier) {
        this.go_identifiers.add(go_identifier);
    }
    public go_FieldDecl getGo_fielddecl() {
        return go_fielddecl;
    }

    public void setGo_fielddecl(go_FieldDecl go_fielddecl) {
        this.go_fielddecl = go_fielddecl;
    }

}