





import java.util.List;
import java.util.ArrayList;

public class kbuild_ShellCmd  {

    private String name;





    private List<kbuild_ShellPart> kbuild_shellparts;




    private kbuild_If kbuild_if;




    private kbuild_ShellPart kbuild_shellpart;


    public kbuild_ShellCmd(
        String name    ) {
        this.name = name;
        this.kbuild_shellparts = new ArrayList<>();
    }

    public kbuild_ShellCmd(
        String name        ArrayList<kbuild_ShellPart> kbuild_shellparts    ) {
        this.name = name;
        this.kbuild_shellparts = kbuild_shellparts;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<kbuild_ShellPart> getKbuild_shellparts() {
        return kbuild_shellparts;
    }

    public void addKbuild_shellpart(Kbuild_shellpart kbuild_shellpart) {
        this.kbuild_shellparts.add(kbuild_shellpart);
    }
    public kbuild_If getKbuild_if() {
        return kbuild_if;
    }

    public void setKbuild_if(kbuild_If kbuild_if) {
        this.kbuild_if = kbuild_if;
    }
    public kbuild_ShellPart getKbuild_shellpart() {
        return kbuild_shellpart;
    }

    public void setKbuild_shellpart(kbuild_ShellPart kbuild_shellpart) {
        this.kbuild_shellpart = kbuild_shellpart;
    }

}