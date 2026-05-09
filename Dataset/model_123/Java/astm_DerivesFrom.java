





import java.util.List;
import java.util.ArrayList;

public class astm_DerivesFrom extends OtherSyntaxObject {

    private boolean isVirtual;





    private astm_OtherSyntaxObject astm_othersyntaxobject;


    public astm_DerivesFrom(
        boolean isVirtual    ) {
        super(
        );
        this.isVirtual = isVirtual;
    }


    public boolean getIsvirtual() {
        return isVirtual;
    }

    public void setIsvirtual(boolean isVirtual) {
        this.isVirtual = isVirtual;
    }

    public astm_OtherSyntaxObject getAstm_othersyntaxobject() {
        return astm_othersyntaxobject;
    }

    public void setAstm_othersyntaxobject(astm_OtherSyntaxObject astm_othersyntaxobject) {
        this.astm_othersyntaxobject = astm_othersyntaxobject;
    }

}