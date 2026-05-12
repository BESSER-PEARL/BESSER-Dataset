





import java.util.List;
import java.util.ArrayList;

public class opf_Spine  {

    private String toc;





    private opf_Package opf_package;


    public opf_Spine(
        String toc    ) {
        this.toc = toc;
    }


    public String getToc() {
        return toc;
    }

    public void setToc(String toc) {
        this.toc = toc;
    }

    public opf_Package getOpf_package() {
        return opf_package;
    }

    public void setOpf_package(opf_Package opf_package) {
        this.opf_package = opf_package;
    }

}