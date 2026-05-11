





import java.util.List;
import java.util.ArrayList;

public class blorqueScript_BSMember extends BSSymbol {

    private boolean isArray;





    private blorqueScript_BSClass blorquescript_bsclass;


    public blorqueScript_BSMember(
        boolean isArray    ) {
        super(
        );
        this.isArray = isArray;
    }


    public boolean getIsarray() {
        return isArray;
    }

    public void setIsarray(boolean isArray) {
        this.isArray = isArray;
    }

    public blorqueScript_BSClass getBlorquescript_bsclass() {
        return blorquescript_bsclass;
    }

    public void setBlorquescript_bsclass(blorqueScript_BSClass blorquescript_bsclass) {
        this.blorquescript_bsclass = blorquescript_bsclass;
    }

}