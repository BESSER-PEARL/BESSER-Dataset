





import java.util.List;
import java.util.ArrayList;

public class YasperEPNML114_DocumentRoot  {

    private String mixed;





    private List<YasperEPNML114_EStringToStringMapEntry> yasperepnml114_estringtostringmapentrys;




    private List<YasperEPNML114_Pnml> yasperepnml114_pnmls;




    private List<YasperEPNML114_EStringToStringMapEntry> yasperepnml114_estringtostringmapentrys;


    public YasperEPNML114_DocumentRoot(
        String mixed    ) {
        this.mixed = mixed;
        this.yasperepnml114_estringtostringmapentrys = new ArrayList<>();
        this.yasperepnml114_pnmls = new ArrayList<>();
        this.yasperepnml114_estringtostringmapentrys = new ArrayList<>();
    }

    public YasperEPNML114_DocumentRoot(
        String mixed        ArrayList<YasperEPNML114_EStringToStringMapEntry> yasperepnml114_estringtostringmapentrys,        ArrayList<YasperEPNML114_Pnml> yasperepnml114_pnmls,        ArrayList<YasperEPNML114_EStringToStringMapEntry> yasperepnml114_estringtostringmapentrys    ) {
        this.mixed = mixed;
        this.yasperepnml114_estringtostringmapentrys = yasperepnml114_estringtostringmapentrys;
        this.yasperepnml114_pnmls = yasperepnml114_pnmls;
        this.yasperepnml114_estringtostringmapentrys = yasperepnml114_estringtostringmapentrys;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<YasperEPNML114_EStringToStringMapEntry> getYasperepnml114_estringtostringmapentrys() {
        return yasperepnml114_estringtostringmapentrys;
    }

    public void addYasperepnml114_estringtostringmapentry(Yasperepnml114_estringtostringmapentry yasperepnml114_estringtostringmapentry) {
        this.yasperepnml114_estringtostringmapentrys.add(yasperepnml114_estringtostringmapentry);
    }
    public List<YasperEPNML114_Pnml> getYasperepnml114_pnmls() {
        return yasperepnml114_pnmls;
    }

    public void addYasperepnml114_pnml(Yasperepnml114_pnml yasperepnml114_pnml) {
        this.yasperepnml114_pnmls.add(yasperepnml114_pnml);
    }
    public List<YasperEPNML114_EStringToStringMapEntry> getYasperepnml114_estringtostringmapentrys() {
        return yasperepnml114_estringtostringmapentrys;
    }

    public void addYasperepnml114_estringtostringmapentry(Yasperepnml114_estringtostringmapentry yasperepnml114_estringtostringmapentry) {
        this.yasperepnml114_estringtostringmapentrys.add(yasperepnml114_estringtostringmapentry);
    }

}