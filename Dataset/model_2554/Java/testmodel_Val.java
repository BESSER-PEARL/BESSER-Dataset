





import java.util.List;
import java.util.ArrayList;

public class testmodel_Val  {

    private String valname;
    private int intlist;
    private int intvl;





    private testmodel_cont testmodel_cont;




    private testmodel_Node testmodel_node;


    public testmodel_Val(
        String valname,        int intlist,        int intvl    ) {
        this.valname = valname;
        this.intlist = intlist;
        this.intvl = intvl;
    }


    public String getValname() {
        return valname;
    }

    public void setValname(String valname) {
        this.valname = valname;
    }
    public int getIntlist() {
        return intlist;
    }

    public void setIntlist(int intlist) {
        this.intlist = intlist;
    }
    public int getIntvl() {
        return intvl;
    }

    public void setIntvl(int intvl) {
        this.intvl = intvl;
    }

    public testmodel_cont getTestmodel_cont() {
        return testmodel_cont;
    }

    public void setTestmodel_cont(testmodel_cont testmodel_cont) {
        this.testmodel_cont = testmodel_cont;
    }
    public testmodel_Node getTestmodel_node() {
        return testmodel_node;
    }

    public void setTestmodel_node(testmodel_Node testmodel_node) {
        this.testmodel_node = testmodel_node;
    }

}