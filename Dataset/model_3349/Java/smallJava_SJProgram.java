





import java.util.List;
import java.util.ArrayList;

public class smallJava_SJProgram  {

    private String name;





    private List<smallJava_SJImport> smalljava_sjimports;




    private List<smallJava_SJClass> smalljava_sjclasss;


    public smallJava_SJProgram(
        String name    ) {
        this.name = name;
        this.smalljava_sjimports = new ArrayList<>();
        this.smalljava_sjclasss = new ArrayList<>();
    }

    public smallJava_SJProgram(
        String name        ArrayList<smallJava_SJImport> smalljava_sjimports,        ArrayList<smallJava_SJClass> smalljava_sjclasss    ) {
        this.name = name;
        this.smalljava_sjimports = smalljava_sjimports;
        this.smalljava_sjclasss = smalljava_sjclasss;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<smallJava_SJImport> getSmalljava_sjimports() {
        return smalljava_sjimports;
    }

    public void addSmalljava_sjimport(Smalljava_sjimport smalljava_sjimport) {
        this.smalljava_sjimports.add(smalljava_sjimport);
    }
    public List<smallJava_SJClass> getSmalljava_sjclasss() {
        return smalljava_sjclasss;
    }

    public void addSmalljava_sjclass(Smalljava_sjclass smalljava_sjclass) {
        this.smalljava_sjclasss.add(smalljava_sjclass);
    }

}