





import java.util.List;
import java.util.ArrayList;

public class uml2CD_RedefinableElement extends Element {

    private boolean isLeaf;





    private uml2CD_RedefinableElement uml2cd_redefinableelement;


    public uml2CD_RedefinableElement(
        boolean isLeaf    ) {
        super(
        );
        this.isLeaf = isLeaf;
    }


    public boolean getIsleaf() {
        return isLeaf;
    }

    public void setIsleaf(boolean isLeaf) {
        this.isLeaf = isLeaf;
    }

    public uml2CD_RedefinableElement getUml2cd_redefinableelement() {
        return uml2cd_redefinableelement;
    }

    public void setUml2cd_redefinableelement(uml2CD_RedefinableElement uml2cd_redefinableelement) {
        this.uml2cd_redefinableelement = uml2cd_redefinableelement;
    }

}