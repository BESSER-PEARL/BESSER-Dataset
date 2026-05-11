





import java.util.List;
import java.util.ArrayList;

public class JavaSimplified_JavaModel  {






    private List<JavaSimplified_Type> javasimplified_types;




    private List<JavaSimplified_JavaClass> javasimplified_javaclasss;


    public JavaSimplified_JavaModel(
    ) {
        this.javasimplified_types = new ArrayList<>();
        this.javasimplified_javaclasss = new ArrayList<>();
    }

    public JavaSimplified_JavaModel(
        ArrayList<JavaSimplified_Type> javasimplified_types,        ArrayList<JavaSimplified_JavaClass> javasimplified_javaclasss    ) {
        this.javasimplified_types = javasimplified_types;
        this.javasimplified_javaclasss = javasimplified_javaclasss;
    }


    public List<JavaSimplified_Type> getJavasimplified_types() {
        return javasimplified_types;
    }

    public void addJavasimplified_type(Javasimplified_type javasimplified_type) {
        this.javasimplified_types.add(javasimplified_type);
    }
    public List<JavaSimplified_JavaClass> getJavasimplified_javaclasss() {
        return javasimplified_javaclasss;
    }

    public void addJavasimplified_javaclass(Javasimplified_javaclass javasimplified_javaclass) {
        this.javasimplified_javaclasss.add(javasimplified_javaclass);
    }

}