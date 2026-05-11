





import java.util.List;
import java.util.ArrayList;

public class Metamodelo_Cpp_CppPackage extends CppPathReferentiable {






    private Metamodelo_Cpp_CppPathReferentiable metamodelo_cpp_cpppathreferentiable;




    private List<Metamodelo_Cpp_CppPackage> metamodelo_cpp_cpppackages;




    private List<Metamodelo_Cpp_CppType> metamodelo_cpp_cpptypes;




    private List<Metamodelo_Cpp_CppPathReferentiable> metamodelo_cpp_cpppathreferentiables;


    public Metamodelo_Cpp_CppPackage(
    ) {
        super(
        );
        this.metamodelo_cpp_cpppackages = new ArrayList<>();
        this.metamodelo_cpp_cpptypes = new ArrayList<>();
        this.metamodelo_cpp_cpppathreferentiables = new ArrayList<>();
    }

    public Metamodelo_Cpp_CppPackage(
        ArrayList<Metamodelo_Cpp_CppPackage> metamodelo_cpp_cpppackages,        ArrayList<Metamodelo_Cpp_CppType> metamodelo_cpp_cpptypes,        ArrayList<Metamodelo_Cpp_CppPathReferentiable> metamodelo_cpp_cpppathreferentiables    ) {
        this.metamodelo_cpp_cpppackages = metamodelo_cpp_cpppackages;
        this.metamodelo_cpp_cpptypes = metamodelo_cpp_cpptypes;
        this.metamodelo_cpp_cpppathreferentiables = metamodelo_cpp_cpppathreferentiables;
    }


    public Metamodelo_Cpp_CppPathReferentiable getMetamodelo_cpp_cpppathreferentiable() {
        return metamodelo_cpp_cpppathreferentiable;
    }

    public void setMetamodelo_cpp_cpppathreferentiable(Metamodelo_Cpp_CppPathReferentiable metamodelo_cpp_cpppathreferentiable) {
        this.metamodelo_cpp_cpppathreferentiable = metamodelo_cpp_cpppathreferentiable;
    }
    public List<Metamodelo_Cpp_CppPackage> getMetamodelo_cpp_cpppackages() {
        return metamodelo_cpp_cpppackages;
    }

    public void addMetamodelo_cpp_cpppackage(Metamodelo_cpp_cpppackage metamodelo_cpp_cpppackage) {
        this.metamodelo_cpp_cpppackages.add(metamodelo_cpp_cpppackage);
    }
    public List<Metamodelo_Cpp_CppType> getMetamodelo_cpp_cpptypes() {
        return metamodelo_cpp_cpptypes;
    }

    public void addMetamodelo_cpp_cpptype(Metamodelo_cpp_cpptype metamodelo_cpp_cpptype) {
        this.metamodelo_cpp_cpptypes.add(metamodelo_cpp_cpptype);
    }
    public List<Metamodelo_Cpp_CppPathReferentiable> getMetamodelo_cpp_cpppathreferentiables() {
        return metamodelo_cpp_cpppathreferentiables;
    }

    public void addMetamodelo_cpp_cpppathreferentiable(Metamodelo_cpp_cpppathreferentiable metamodelo_cpp_cpppathreferentiable) {
        this.metamodelo_cpp_cpppathreferentiables.add(metamodelo_cpp_cpppathreferentiable);
    }

}