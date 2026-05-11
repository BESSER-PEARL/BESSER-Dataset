





import java.util.List;
import java.util.ArrayList;

public class codetaginfo_DocumentRoot  {

    private String mixed;





    private List<codetaginfo_CodeTagInfo> codetaginfo_codetaginfos;


    public codetaginfo_DocumentRoot(
        String mixed    ) {
        this.mixed = mixed;
        this.codetaginfo_codetaginfos = new ArrayList<>();
    }

    public codetaginfo_DocumentRoot(
        String mixed        ArrayList<codetaginfo_CodeTagInfo> codetaginfo_codetaginfos    ) {
        this.mixed = mixed;
        this.codetaginfo_codetaginfos = codetaginfo_codetaginfos;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<codetaginfo_CodeTagInfo> getCodetaginfo_codetaginfos() {
        return codetaginfo_codetaginfos;
    }

    public void addCodetaginfo_codetaginfo(Codetaginfo_codetaginfo codetaginfo_codetaginfo) {
        this.codetaginfo_codetaginfos.add(codetaginfo_codetaginfo);
    }

}