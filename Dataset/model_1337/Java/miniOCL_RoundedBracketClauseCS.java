





import java.util.List;
import java.util.ArrayList;

public class miniOCL_RoundedBracketClauseCS  {






    private List<miniOCL_ExpCS> miniocl_expcss;




    private miniOCL_NameExpCS miniocl_nameexpcs;




    private miniOCL_NavigationNameExpCS miniocl_navigationnameexpcs;


    public miniOCL_RoundedBracketClauseCS(
    ) {
        this.miniocl_expcss = new ArrayList<>();
    }

    public miniOCL_RoundedBracketClauseCS(
        ArrayList<miniOCL_ExpCS> miniocl_expcss    ) {
        this.miniocl_expcss = miniocl_expcss;
    }


    public List<miniOCL_ExpCS> getMiniocl_expcss() {
        return miniocl_expcss;
    }

    public void addMiniocl_expcs(Miniocl_expcs miniocl_expcs) {
        this.miniocl_expcss.add(miniocl_expcs);
    }
    public miniOCL_NameExpCS getMiniocl_nameexpcs() {
        return miniocl_nameexpcs;
    }

    public void setMiniocl_nameexpcs(miniOCL_NameExpCS miniocl_nameexpcs) {
        this.miniocl_nameexpcs = miniocl_nameexpcs;
    }
    public miniOCL_NavigationNameExpCS getMiniocl_navigationnameexpcs() {
        return miniocl_navigationnameexpcs;
    }

    public void setMiniocl_navigationnameexpcs(miniOCL_NavigationNameExpCS miniocl_navigationnameexpcs) {
        this.miniocl_navigationnameexpcs = miniocl_navigationnameexpcs;
    }

}