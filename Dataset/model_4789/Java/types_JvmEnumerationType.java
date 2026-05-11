





import java.util.List;
import java.util.ArrayList;

public class types_JvmEnumerationType extends JvmDeclaredType {






    private List<types_JvmEnumerationLiteral> types_jvmenumerationliterals;


    public types_JvmEnumerationType(
    ) {
        super(
        );
        this.types_jvmenumerationliterals = new ArrayList<>();
    }

    public types_JvmEnumerationType(
        ArrayList<types_JvmEnumerationLiteral> types_jvmenumerationliterals    ) {
        this.types_jvmenumerationliterals = types_jvmenumerationliterals;
    }


    public List<types_JvmEnumerationLiteral> getTypes_jvmenumerationliterals() {
        return types_jvmenumerationliterals;
    }

    public void addTypes_jvmenumerationliteral(Types_jvmenumerationliteral types_jvmenumerationliteral) {
        this.types_jvmenumerationliterals.add(types_jvmenumerationliteral);
    }

}