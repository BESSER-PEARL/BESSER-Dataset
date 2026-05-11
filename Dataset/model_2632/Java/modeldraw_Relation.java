





import java.util.List;
import java.util.ArrayList;

public class modeldraw_Relation extends NamedItem {

    private String tar_decoration;
    private String src_decoration;



    public modeldraw_Relation(
        String tar_decoration,        String src_decoration    ) {
        super(
        );
        this.tar_decoration = tar_decoration;
        this.src_decoration = src_decoration;
    }


    public String getTar_decoration() {
        return tar_decoration;
    }

    public void setTar_decoration(String tar_decoration) {
        this.tar_decoration = tar_decoration;
    }
    public String getSrc_decoration() {
        return src_decoration;
    }

    public void setSrc_decoration(String src_decoration) {
        this.src_decoration = src_decoration;
    }


}