





import java.util.List;
import java.util.ArrayList;

public class xtend_JvmEnumAnnotationValue extends JvmAnnotationValue {






    private List<xtend_JvmEnumerationLiteral> xtend_jvmenumerationliterals;


    public xtend_JvmEnumAnnotationValue(
    ) {
        super(
        );
        this.xtend_jvmenumerationliterals = new ArrayList<>();
    }

    public xtend_JvmEnumAnnotationValue(
        ArrayList<xtend_JvmEnumerationLiteral> xtend_jvmenumerationliterals    ) {
        this.xtend_jvmenumerationliterals = xtend_jvmenumerationliterals;
    }


    public List<xtend_JvmEnumerationLiteral> getXtend_jvmenumerationliterals() {
        return xtend_jvmenumerationliterals;
    }

    public void addXtend_jvmenumerationliteral(Xtend_jvmenumerationliteral xtend_jvmenumerationliteral) {
        this.xtend_jvmenumerationliterals.add(xtend_jvmenumerationliteral);
    }

}