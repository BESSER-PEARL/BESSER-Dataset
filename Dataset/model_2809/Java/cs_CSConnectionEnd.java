





import java.util.List;
import java.util.ArrayList;

public class cs_CSConnectionEnd  {

    private int tipType;





    private cs_CSNode cs_csnode;




    private cs_CSConnection cs_csconnection;


    public cs_CSConnectionEnd(
        int tipType    ) {
        this.tipType = tipType;
    }


    public int getTiptype() {
        return tipType;
    }

    public void setTiptype(int tipType) {
        this.tipType = tipType;
    }

    public cs_CSNode getCs_csnode() {
        return cs_csnode;
    }

    public void setCs_csnode(cs_CSNode cs_csnode) {
        this.cs_csnode = cs_csnode;
    }
    public cs_CSConnection getCs_csconnection() {
        return cs_csconnection;
    }

    public void setCs_csconnection(cs_CSConnection cs_csconnection) {
        this.cs_csconnection = cs_csconnection;
    }

}