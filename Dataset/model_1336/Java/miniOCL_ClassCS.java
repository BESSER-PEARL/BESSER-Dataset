





import java.util.List;
import java.util.ArrayList;

public class miniOCL_ClassCS  {

    private String name;





    private miniOCL_PackageCS miniocl_packagecs;


    public miniOCL_ClassCS(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public miniOCL_PackageCS getMiniocl_packagecs() {
        return miniocl_packagecs;
    }

    public void setMiniocl_packagecs(miniOCL_PackageCS miniocl_packagecs) {
        this.miniocl_packagecs = miniocl_packagecs;
    }

}