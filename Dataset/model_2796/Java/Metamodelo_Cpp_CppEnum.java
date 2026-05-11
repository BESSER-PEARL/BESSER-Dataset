





import java.util.List;
import java.util.ArrayList;

public class Metamodelo_Cpp_CppEnum extends CppType {






    private List<Metamodelo_Cpp_CppEnumConstructor> metamodelo_cpp_cppenumconstructors;


    public Metamodelo_Cpp_CppEnum(
    ) {
        super(
        );
        this.metamodelo_cpp_cppenumconstructors = new ArrayList<>();
    }

    public Metamodelo_Cpp_CppEnum(
        ArrayList<Metamodelo_Cpp_CppEnumConstructor> metamodelo_cpp_cppenumconstructors    ) {
        this.metamodelo_cpp_cppenumconstructors = metamodelo_cpp_cppenumconstructors;
    }


    public List<Metamodelo_Cpp_CppEnumConstructor> getMetamodelo_cpp_cppenumconstructors() {
        return metamodelo_cpp_cppenumconstructors;
    }

    public void addMetamodelo_cpp_cppenumconstructor(Metamodelo_cpp_cppenumconstructor metamodelo_cpp_cppenumconstructor) {
        this.metamodelo_cpp_cppenumconstructors.add(metamodelo_cpp_cppenumconstructor);
    }

}