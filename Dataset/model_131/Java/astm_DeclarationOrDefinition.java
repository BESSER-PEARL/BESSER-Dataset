





import java.util.List;
import java.util.ArrayList;

public class astm_DeclarationOrDefinition extends DefinitionObject {

    private String linkageSpecifier;
    private boolean isRegister;





    private astm_OtherSyntaxObject astm_othersyntaxobject;




    private astm_OtherSyntaxObject astm_othersyntaxobject;


    public astm_DeclarationOrDefinition(
        String linkageSpecifier,        boolean isRegister    ) {
        super(
        );
        this.linkageSpecifier = linkageSpecifier;
        this.isRegister = isRegister;
    }


    public String getLinkagespecifier() {
        return linkageSpecifier;
    }

    public void setLinkagespecifier(String linkageSpecifier) {
        this.linkageSpecifier = linkageSpecifier;
    }
    public boolean getIsregister() {
        return isRegister;
    }

    public void setIsregister(boolean isRegister) {
        this.isRegister = isRegister;
    }

    public astm_OtherSyntaxObject getAstm_othersyntaxobject() {
        return astm_othersyntaxobject;
    }

    public void setAstm_othersyntaxobject(astm_OtherSyntaxObject astm_othersyntaxobject) {
        this.astm_othersyntaxobject = astm_othersyntaxobject;
    }
    public astm_OtherSyntaxObject getAstm_othersyntaxobject() {
        return astm_othersyntaxobject;
    }

    public void setAstm_othersyntaxobject(astm_OtherSyntaxObject astm_othersyntaxobject) {
        this.astm_othersyntaxobject = astm_othersyntaxobject;
    }

}