





import java.util.List;
import java.util.ArrayList;

public class astm_DeclarationOrDefinition extends DefinitionObject {

    private boolean isRegister;
    private String linkageSpecifier;





    private astm_OtherSyntaxObject astm_othersyntaxobject;




    private astm_OtherSyntaxObject astm_othersyntaxobject;


    public astm_DeclarationOrDefinition(
        boolean isRegister,        String linkageSpecifier    ) {
        super(
        );
        this.isRegister = isRegister;
        this.linkageSpecifier = linkageSpecifier;
    }


    public boolean getIsregister() {
        return isRegister;
    }

    public void setIsregister(boolean isRegister) {
        this.isRegister = isRegister;
    }
    public String getLinkagespecifier() {
        return linkageSpecifier;
    }

    public void setLinkagespecifier(String linkageSpecifier) {
        this.linkageSpecifier = linkageSpecifier;
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