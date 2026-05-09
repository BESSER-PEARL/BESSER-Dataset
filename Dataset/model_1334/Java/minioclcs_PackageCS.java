





import java.util.List;
import java.util.ArrayList;

public class minioclcs_PackageCS extends CSTrace {

    private String name;





    private List<minioclcs_PackageCS> minioclcs_packagecss;




    private List<minioclcs_ClassCS> minioclcs_classcss;




    private minioclcs_RootCS minioclcs_rootcs;


    public minioclcs_PackageCS(
        String name    ) {
        super(
        );
        this.name = name;
        this.minioclcs_packagecss = new ArrayList<>();
        this.minioclcs_classcss = new ArrayList<>();
    }

    public minioclcs_PackageCS(
        String name        ArrayList<minioclcs_PackageCS> minioclcs_packagecss,        ArrayList<minioclcs_ClassCS> minioclcs_classcss    ) {
        this.name = name;
        this.minioclcs_packagecss = minioclcs_packagecss;
        this.minioclcs_classcss = minioclcs_classcss;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<minioclcs_PackageCS> getMinioclcs_packagecss() {
        return minioclcs_packagecss;
    }

    public void addMinioclcs_packagecs(Minioclcs_packagecs minioclcs_packagecs) {
        this.minioclcs_packagecss.add(minioclcs_packagecs);
    }
    public List<minioclcs_ClassCS> getMinioclcs_classcss() {
        return minioclcs_classcss;
    }

    public void addMinioclcs_classcs(Minioclcs_classcs minioclcs_classcs) {
        this.minioclcs_classcss.add(minioclcs_classcs);
    }
    public minioclcs_RootCS getMinioclcs_rootcs() {
        return minioclcs_rootcs;
    }

    public void setMinioclcs_rootcs(minioclcs_RootCS minioclcs_rootcs) {
        this.minioclcs_rootcs = minioclcs_rootcs;
    }

}