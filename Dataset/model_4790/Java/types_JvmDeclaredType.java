





import java.util.List;
import java.util.ArrayList;

public class types_JvmDeclaredType extends JvmMember, JvmComponentType {

    private String packageName;
    private boolean static;
    private boolean abstract;
    private boolean final;





    private types_JvmMember types_jvmmember;




    private List<types_JvmTypeReference> types_jvmtypereferences;




    private List<types_JvmMember> types_jvmmembers;


    public types_JvmDeclaredType(
        String packageName,        boolean static,        boolean abstract,        boolean final    ) {
        super(
        );
        this.packageName = packageName;
        this.static = static;
        this.abstract = abstract;
        this.final = final;
        this.types_jvmtypereferences = new ArrayList<>();
        this.types_jvmmembers = new ArrayList<>();
    }

    public types_JvmDeclaredType(
        String packageName,        boolean static,        boolean abstract,        boolean final        ArrayList<types_JvmTypeReference> types_jvmtypereferences,        ArrayList<types_JvmMember> types_jvmmembers    ) {
        this.packageName = packageName;
        this.static = static;
        this.abstract = abstract;
        this.final = final;
        this.types_jvmtypereferences = types_jvmtypereferences;
        this.types_jvmmembers = types_jvmmembers;
    }

    public String getPackagename() {
        return packageName;
    }

    public void setPackagename(String packageName) {
        this.packageName = packageName;
    }
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }
    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }
    public boolean getFinal() {
        return final;
    }

    public void setFinal(boolean final) {
        this.final = final;
    }

    public types_JvmMember getTypes_jvmmember() {
        return types_jvmmember;
    }

    public void setTypes_jvmmember(types_JvmMember types_jvmmember) {
        this.types_jvmmember = types_jvmmember;
    }
    public List<types_JvmTypeReference> getTypes_jvmtypereferences() {
        return types_jvmtypereferences;
    }

    public void addTypes_jvmtypereference(Types_jvmtypereference types_jvmtypereference) {
        this.types_jvmtypereferences.add(types_jvmtypereference);
    }
    public List<types_JvmMember> getTypes_jvmmembers() {
        return types_jvmmembers;
    }

    public void addTypes_jvmmember(Types_jvmmember types_jvmmember) {
        this.types_jvmmembers.add(types_jvmmember);
    }

}