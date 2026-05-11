





import java.util.List;
import java.util.ArrayList;

public class ecdarText_ETFieldDeclaration  {






    private ecdarText_ETStructType ecdartext_etstructtype;




    private ecdarText_ETType ecdartext_ettype;




    private List<ecdarText_ETFieldID> ecdartext_etfieldids;


    public ecdarText_ETFieldDeclaration(
    ) {
        this.ecdartext_etfieldids = new ArrayList<>();
    }

    public ecdarText_ETFieldDeclaration(
        ArrayList<ecdarText_ETFieldID> ecdartext_etfieldids    ) {
        this.ecdartext_etfieldids = ecdartext_etfieldids;
    }


    public ecdarText_ETStructType getEcdartext_etstructtype() {
        return ecdartext_etstructtype;
    }

    public void setEcdartext_etstructtype(ecdarText_ETStructType ecdartext_etstructtype) {
        this.ecdartext_etstructtype = ecdartext_etstructtype;
    }
    public ecdarText_ETType getEcdartext_ettype() {
        return ecdartext_ettype;
    }

    public void setEcdartext_ettype(ecdarText_ETType ecdartext_ettype) {
        this.ecdartext_ettype = ecdartext_ettype;
    }
    public List<ecdarText_ETFieldID> getEcdartext_etfieldids() {
        return ecdartext_etfieldids;
    }

    public void addEcdartext_etfieldid(Ecdartext_etfieldid ecdartext_etfieldid) {
        this.ecdartext_etfieldids.add(ecdartext_etfieldid);
    }

}