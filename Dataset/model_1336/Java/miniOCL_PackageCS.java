





import java.util.List;
import java.util.ArrayList;

public class miniOCL_PackageCS  {

    private String name;





    private miniOCL_RootCS miniocl_rootcs;




    private List<miniOCL_PackageCS> miniocl_packagecss;


    public miniOCL_PackageCS(
        String name    ) {
        this.name = name;
        this.miniocl_packagecss = new ArrayList<>();
    }

    public miniOCL_PackageCS(
        String name        ArrayList<miniOCL_PackageCS> miniocl_packagecss    ) {
        this.name = name;
        this.miniocl_packagecss = miniocl_packagecss;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public miniOCL_RootCS getMiniocl_rootcs() {
        return miniocl_rootcs;
    }

    public void setMiniocl_rootcs(miniOCL_RootCS miniocl_rootcs) {
        this.miniocl_rootcs = miniocl_rootcs;
    }
    public List<miniOCL_PackageCS> getMiniocl_packagecss() {
        return miniocl_packagecss;
    }

    public void addMiniocl_packagecs(Miniocl_packagecs miniocl_packagecs) {
        this.miniocl_packagecss.add(miniocl_packagecs);
    }

}