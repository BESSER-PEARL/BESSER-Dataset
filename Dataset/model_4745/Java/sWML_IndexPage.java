





import java.util.List;
import java.util.ArrayList;

public class sWML_IndexPage  {

    private int size;
    private String name;





    private sWML_HypertextLayer swml_hypertextlayer;


    public sWML_IndexPage(
        int size,        String name    ) {
        this.size = size;
        this.name = name;
    }


    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sWML_HypertextLayer getSwml_hypertextlayer() {
        return swml_hypertextlayer;
    }

    public void setSwml_hypertextlayer(sWML_HypertextLayer swml_hypertextlayer) {
        this.swml_hypertextlayer = swml_hypertextlayer;
    }

}