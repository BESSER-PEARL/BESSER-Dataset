





import java.util.List;
import java.util.ArrayList;

public class ansic_declaration  {






    private List<ansic_declaration_specifiers> ansic_declaration_specifierss;




    private ansic_external_declaration ansic_external_declaration;


    public ansic_declaration(
    ) {
        this.ansic_declaration_specifierss = new ArrayList<>();
    }

    public ansic_declaration(
        ArrayList<ansic_declaration_specifiers> ansic_declaration_specifierss    ) {
        this.ansic_declaration_specifierss = ansic_declaration_specifierss;
    }


    public List<ansic_declaration_specifiers> getAnsic_declaration_specifierss() {
        return ansic_declaration_specifierss;
    }

    public void addAnsic_declaration_specifiers(Ansic_declaration_specifiers ansic_declaration_specifiers) {
        this.ansic_declaration_specifierss.add(ansic_declaration_specifiers);
    }
    public ansic_external_declaration getAnsic_external_declaration() {
        return ansic_external_declaration;
    }

    public void setAnsic_external_declaration(ansic_external_declaration ansic_external_declaration) {
        this.ansic_external_declaration = ansic_external_declaration;
    }

}