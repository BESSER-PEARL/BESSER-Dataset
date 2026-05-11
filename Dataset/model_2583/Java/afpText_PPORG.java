





import java.util.List;
import java.util.ArrayList;

public class afpText_PPORG  {

    private String ProcFlgs;
    private String YocaOset;
    private String RGLength;
    private String ObjType;
    private String XocaOset;





    private afpText_PPO afptext_ppo;




    private List<afpText_triplet> afptext_triplets;


    public afpText_PPORG(
        String ProcFlgs,        String YocaOset,        String RGLength,        String ObjType,        String XocaOset    ) {
        this.ProcFlgs = ProcFlgs;
        this.YocaOset = YocaOset;
        this.RGLength = RGLength;
        this.ObjType = ObjType;
        this.XocaOset = XocaOset;
        this.afptext_triplets = new ArrayList<>();
    }

    public afpText_PPORG(
        String ProcFlgs,        String YocaOset,        String RGLength,        String ObjType,        String XocaOset        ArrayList<afpText_triplet> afptext_triplets    ) {
        this.ProcFlgs = ProcFlgs;
        this.YocaOset = YocaOset;
        this.RGLength = RGLength;
        this.ObjType = ObjType;
        this.XocaOset = XocaOset;
        this.afptext_triplets = afptext_triplets;
    }

    public String getProcflgs() {
        return ProcFlgs;
    }

    public void setProcflgs(String ProcFlgs) {
        this.ProcFlgs = ProcFlgs;
    }
    public String getYocaoset() {
        return YocaOset;
    }

    public void setYocaoset(String YocaOset) {
        this.YocaOset = YocaOset;
    }
    public String getRglength() {
        return RGLength;
    }

    public void setRglength(String RGLength) {
        this.RGLength = RGLength;
    }
    public String getObjtype() {
        return ObjType;
    }

    public void setObjtype(String ObjType) {
        this.ObjType = ObjType;
    }
    public String getXocaoset() {
        return XocaOset;
    }

    public void setXocaoset(String XocaOset) {
        this.XocaOset = XocaOset;
    }

    public afpText_PPO getAfptext_ppo() {
        return afptext_ppo;
    }

    public void setAfptext_ppo(afpText_PPO afptext_ppo) {
        this.afptext_ppo = afptext_ppo;
    }
    public List<afpText_triplet> getAfptext_triplets() {
        return afptext_triplets;
    }

    public void addAfptext_triplet(Afptext_triplet afptext_triplet) {
        this.afptext_triplets.add(afptext_triplet);
    }

}