





import java.util.List;
import java.util.ArrayList;

public class ecdarText_ETSelect  {

    private String name;





    private ecdarText_ETType ecdartext_ettype;




    private ecdarText_ETEdge ecdartext_etedge;


    public ecdarText_ETSelect(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ecdarText_ETType getEcdartext_ettype() {
        return ecdartext_ettype;
    }

    public void setEcdartext_ettype(ecdarText_ETType ecdartext_ettype) {
        this.ecdartext_ettype = ecdartext_ettype;
    }
    public ecdarText_ETEdge getEcdartext_etedge() {
        return ecdartext_etedge;
    }

    public void setEcdartext_etedge(ecdarText_ETEdge ecdartext_etedge) {
        this.ecdartext_etedge = ecdartext_etedge;
    }

}