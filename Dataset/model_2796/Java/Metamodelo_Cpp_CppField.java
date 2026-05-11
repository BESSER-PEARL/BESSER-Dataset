





import java.util.List;
import java.util.ArrayList;

public class Metamodelo_Cpp_CppField extends CppNamedElement {

    private String accessSpecifier;



    public Metamodelo_Cpp_CppField(
        String accessSpecifier    ) {
        super(
        );
        this.accessSpecifier = accessSpecifier;
    }


    public String getAccessspecifier() {
        return accessSpecifier;
    }

    public void setAccessspecifier(String accessSpecifier) {
        this.accessSpecifier = accessSpecifier;
    }


}