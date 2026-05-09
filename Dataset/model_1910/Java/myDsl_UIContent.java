





import java.util.List;
import java.util.ArrayList;

public class myDsl_UIContent  {

    private String name;





    private myDsl_ComponentsUI mydsl_componentsui;




    private List<myDsl_ComponentClass> mydsl_componentclasss;


    public myDsl_UIContent(
        String name    ) {
        this.name = name;
        this.mydsl_componentclasss = new ArrayList<>();
    }

    public myDsl_UIContent(
        String name        ArrayList<myDsl_ComponentClass> mydsl_componentclasss    ) {
        this.name = name;
        this.mydsl_componentclasss = mydsl_componentclasss;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_ComponentsUI getMydsl_componentsui() {
        return mydsl_componentsui;
    }

    public void setMydsl_componentsui(myDsl_ComponentsUI mydsl_componentsui) {
        this.mydsl_componentsui = mydsl_componentsui;
    }
    public List<myDsl_ComponentClass> getMydsl_componentclasss() {
        return mydsl_componentclasss;
    }

    public void addMydsl_componentclass(Mydsl_componentclass mydsl_componentclass) {
        this.mydsl_componentclasss.add(mydsl_componentclass);
    }

}