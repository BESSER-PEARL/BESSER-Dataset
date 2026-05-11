





import java.util.List;
import java.util.ArrayList;

public class simplejava_SimpleJava  {






    private simplejava_ClassDeclaration simplejava_classdeclaration;




    private List<simplejava_Import> simplejava_imports;


    public simplejava_SimpleJava(
    ) {
        this.simplejava_imports = new ArrayList<>();
    }

    public simplejava_SimpleJava(
        ArrayList<simplejava_Import> simplejava_imports    ) {
        this.simplejava_imports = simplejava_imports;
    }


    public simplejava_ClassDeclaration getSimplejava_classdeclaration() {
        return simplejava_classdeclaration;
    }

    public void setSimplejava_classdeclaration(simplejava_ClassDeclaration simplejava_classdeclaration) {
        this.simplejava_classdeclaration = simplejava_classdeclaration;
    }
    public List<simplejava_Import> getSimplejava_imports() {
        return simplejava_imports;
    }

    public void addSimplejava_import(Simplejava_import simplejava_import) {
        this.simplejava_imports.add(simplejava_import);
    }

}