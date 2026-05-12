





import java.util.List;
import java.util.ArrayList;

public class kbuild_VarSlashSym  {

    private String name;





    private kbuild_ShellPart kbuild_shellpart;


    public kbuild_VarSlashSym(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public kbuild_ShellPart getKbuild_shellpart() {
        return kbuild_shellpart;
    }

    public void setKbuild_shellpart(kbuild_ShellPart kbuild_shellpart) {
        this.kbuild_shellpart = kbuild_shellpart;
    }

}