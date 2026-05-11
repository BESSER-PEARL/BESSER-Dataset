





import java.util.List;
import java.util.ArrayList;

public class sWML_IndexPage  {

    private String name;
    private int size;





    private sWML_HypertextLayer swml_hypertextlayer;




    private sWML_Class swml_class;


    public sWML_IndexPage(
        String name,        int size    ) {
        this.name = name;
        this.size = size;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }

    public sWML_HypertextLayer getSwml_hypertextlayer() {
        return swml_hypertextlayer;
    }

    public void setSwml_hypertextlayer(sWML_HypertextLayer swml_hypertextlayer) {
        this.swml_hypertextlayer = swml_hypertextlayer;
    }
    public sWML_Class getSwml_class() {
        return swml_class;
    }

    public void setSwml_class(sWML_Class swml_class) {
        this.swml_class = swml_class;
    }

}