





import java.util.List;
import java.util.ArrayList;

public class gastm_DeclarationOrDefinition extends DefinitionObject {

    private String linkageSpecifier;
    private boolean isRegister;





    private OtherSyntaxObject othersyntaxobject;




    private OtherSyntaxObject othersyntaxobject;


    public gastm_DeclarationOrDefinition(
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

    public OtherSyntaxObject getOthersyntaxobject() {
        return othersyntaxobject;
    }

    public void setOthersyntaxobject(OtherSyntaxObject othersyntaxobject) {
        this.othersyntaxobject = othersyntaxobject;
    }
    public OtherSyntaxObject getOthersyntaxobject() {
        return othersyntaxobject;
    }

    public void setOthersyntaxobject(OtherSyntaxObject othersyntaxobject) {
        this.othersyntaxobject = othersyntaxobject;
    }

}