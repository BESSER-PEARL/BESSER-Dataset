





import java.util.List;
import java.util.ArrayList;

public class JavaSimplified_JavaClass extends CommentedElement, NamedElement {

    private String imports;





    private List<JavaSimplified_Method> javasimplified_methods;




    private List<JavaSimplified_Field> javasimplified_fields;


    public JavaSimplified_JavaClass(
        String imports    ) {
        super(
        );
        this.imports = imports;
        this.javasimplified_methods = new ArrayList<>();
        this.javasimplified_fields = new ArrayList<>();
    }

    public JavaSimplified_JavaClass(
        String imports        ArrayList<JavaSimplified_Method> javasimplified_methods,        ArrayList<JavaSimplified_Field> javasimplified_fields    ) {
        this.imports = imports;
        this.javasimplified_methods = javasimplified_methods;
        this.javasimplified_fields = javasimplified_fields;
    }

    public String getImports() {
        return imports;
    }

    public void setImports(String imports) {
        this.imports = imports;
    }

    public List<JavaSimplified_Method> getJavasimplified_methods() {
        return javasimplified_methods;
    }

    public void addJavasimplified_method(Javasimplified_method javasimplified_method) {
        this.javasimplified_methods.add(javasimplified_method);
    }
    public List<JavaSimplified_Field> getJavasimplified_fields() {
        return javasimplified_fields;
    }

    public void addJavasimplified_field(Javasimplified_field javasimplified_field) {
        this.javasimplified_fields.add(javasimplified_field);
    }

}