





import java.util.List;
import java.util.ArrayList;

public class myAtl_Module  {

    private String name;





    private myAtl_NameExpCS myatl_nameexpcs;




    private List<myAtl_NameExpCS> myatl_nameexpcss;




    private List<myAtl_NameExpCS> myatl_nameexpcss;


    public myAtl_Module(
        String name    ) {
        this.name = name;
        this.myatl_nameexpcss = new ArrayList<>();
        this.myatl_nameexpcss = new ArrayList<>();
    }

    public myAtl_Module(
        String name        ArrayList<myAtl_NameExpCS> myatl_nameexpcss,        ArrayList<myAtl_NameExpCS> myatl_nameexpcss    ) {
        this.name = name;
        this.myatl_nameexpcss = myatl_nameexpcss;
        this.myatl_nameexpcss = myatl_nameexpcss;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myAtl_NameExpCS getMyatl_nameexpcs() {
        return myatl_nameexpcs;
    }

    public void setMyatl_nameexpcs(myAtl_NameExpCS myatl_nameexpcs) {
        this.myatl_nameexpcs = myatl_nameexpcs;
    }
    public List<myAtl_NameExpCS> getMyatl_nameexpcss() {
        return myatl_nameexpcss;
    }

    public void addMyatl_nameexpcs(Myatl_nameexpcs myatl_nameexpcs) {
        this.myatl_nameexpcss.add(myatl_nameexpcs);
    }
    public List<myAtl_NameExpCS> getMyatl_nameexpcss() {
        return myatl_nameexpcss;
    }

    public void addMyatl_nameexpcs(Myatl_nameexpcs myatl_nameexpcs) {
        this.myatl_nameexpcss.add(myatl_nameexpcs);
    }

}