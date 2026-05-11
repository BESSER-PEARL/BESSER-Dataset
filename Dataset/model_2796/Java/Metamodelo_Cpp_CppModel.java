





import java.util.List;
import java.util.ArrayList;

public class Metamodelo_Cpp_CppModel  {

    private String targetFolder;
    private String name;
    private String sourceFolder;





    private List<Metamodelo_Cpp_CppType> metamodelo_cpp_cpptypes;




    private List<Metamodelo_Cpp_CppClassFile> metamodelo_cpp_cppclassfiles;




    private List<Metamodelo_Cpp_CppPathReferentiable> metamodelo_cpp_cpppathreferentiables;


    public Metamodelo_Cpp_CppModel(
        String targetFolder,        String name,        String sourceFolder    ) {
        this.targetFolder = targetFolder;
        this.name = name;
        this.sourceFolder = sourceFolder;
        this.metamodelo_cpp_cpptypes = new ArrayList<>();
        this.metamodelo_cpp_cppclassfiles = new ArrayList<>();
        this.metamodelo_cpp_cpppathreferentiables = new ArrayList<>();
    }

    public Metamodelo_Cpp_CppModel(
        String targetFolder,        String name,        String sourceFolder        ArrayList<Metamodelo_Cpp_CppType> metamodelo_cpp_cpptypes,        ArrayList<Metamodelo_Cpp_CppClassFile> metamodelo_cpp_cppclassfiles,        ArrayList<Metamodelo_Cpp_CppPathReferentiable> metamodelo_cpp_cpppathreferentiables    ) {
        this.targetFolder = targetFolder;
        this.name = name;
        this.sourceFolder = sourceFolder;
        this.metamodelo_cpp_cpptypes = metamodelo_cpp_cpptypes;
        this.metamodelo_cpp_cppclassfiles = metamodelo_cpp_cppclassfiles;
        this.metamodelo_cpp_cpppathreferentiables = metamodelo_cpp_cpppathreferentiables;
    }

    public String getTargetfolder() {
        return targetFolder;
    }

    public void setTargetfolder(String targetFolder) {
        this.targetFolder = targetFolder;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSourcefolder() {
        return sourceFolder;
    }

    public void setSourcefolder(String sourceFolder) {
        this.sourceFolder = sourceFolder;
    }

    public List<Metamodelo_Cpp_CppType> getMetamodelo_cpp_cpptypes() {
        return metamodelo_cpp_cpptypes;
    }

    public void addMetamodelo_cpp_cpptype(Metamodelo_cpp_cpptype metamodelo_cpp_cpptype) {
        this.metamodelo_cpp_cpptypes.add(metamodelo_cpp_cpptype);
    }
    public List<Metamodelo_Cpp_CppClassFile> getMetamodelo_cpp_cppclassfiles() {
        return metamodelo_cpp_cppclassfiles;
    }

    public void addMetamodelo_cpp_cppclassfile(Metamodelo_cpp_cppclassfile metamodelo_cpp_cppclassfile) {
        this.metamodelo_cpp_cppclassfiles.add(metamodelo_cpp_cppclassfile);
    }
    public List<Metamodelo_Cpp_CppPathReferentiable> getMetamodelo_cpp_cpppathreferentiables() {
        return metamodelo_cpp_cpppathreferentiables;
    }

    public void addMetamodelo_cpp_cpppathreferentiable(Metamodelo_cpp_cpppathreferentiable metamodelo_cpp_cpppathreferentiable) {
        this.metamodelo_cpp_cpppathreferentiables.add(metamodelo_cpp_cpppathreferentiable);
    }

}