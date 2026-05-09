





import java.util.List;
import java.util.ArrayList;

public class kiamaas_Node  {

    private String height;
    private String depth;





    private kiamaas_Top kiamaas_top;


    public kiamaas_Node(
        String height,        String depth    ) {
        this.height = height;
        this.depth = depth;
    }


    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getDepth() {
        return depth;
    }

    public void setDepth(String depth) {
        this.depth = depth;
    }

    public kiamaas_Top getKiamaas_top() {
        return kiamaas_top;
    }

    public void setKiamaas_top(kiamaas_Top kiamaas_top) {
        this.kiamaas_top = kiamaas_top;
    }

}