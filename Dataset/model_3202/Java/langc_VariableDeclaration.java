





import java.util.List;
import java.util.ArrayList;

public class langc_VariableDeclaration extends NamedElement {

    private String linkage;





    private langc_VariableDeclarationStatement langc_variabledeclarationstatement;


    public langc_VariableDeclaration(
        String linkage    ) {
        super(
        );
        this.linkage = linkage;
    }


    public String getLinkage() {
        return linkage;
    }

    public void setLinkage(String linkage) {
        this.linkage = linkage;
    }

    public langc_VariableDeclarationStatement getLangc_variabledeclarationstatement() {
        return langc_variabledeclarationstatement;
    }

    public void setLangc_variabledeclarationstatement(langc_VariableDeclarationStatement langc_variabledeclarationstatement) {
        this.langc_variabledeclarationstatement = langc_variabledeclarationstatement;
    }

}