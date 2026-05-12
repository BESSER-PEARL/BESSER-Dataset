





import java.util.List;
import java.util.ArrayList;

public class xtend_JvmDeclaredType extends JvmComponentType, JvmMember {

    private String packageName;
    private boolean abstract;
    private boolean final;
    private boolean static;





    private xtend_JvmMember xtend_jvmmember;




    private List<xtend_JvmTypeReference> xtend_jvmtypereferences;




    private List<xtend_JvmMember> xtend_jvmmembers;




    private xtend_XFeatureCall xtend_xfeaturecall;


    public xtend_JvmDeclaredType(
        String packageName,        boolean abstract,        boolean final,        boolean static    ) {
        super(
        );
        this.packageName = packageName;
        this.abstract = abstract;
        this.final = final;
        this.static = static;
        this.xtend_jvmtypereferences = new ArrayList<>();
        this.xtend_jvmmembers = new ArrayList<>();
    }

    public xtend_JvmDeclaredType(
        String packageName,        boolean abstract,        boolean final,        boolean static        ArrayList<xtend_JvmTypeReference> xtend_jvmtypereferences,        ArrayList<xtend_JvmMember> xtend_jvmmembers    ) {
        this.packageName = packageName;
        this.abstract = abstract;
        this.final = final;
        this.static = static;
        this.xtend_jvmtypereferences = xtend_jvmtypereferences;
        this.xtend_jvmmembers = xtend_jvmmembers;
    }

    public String getPackagename() {
        return packageName;
    }

    public void setPackagename(String packageName) {
        this.packageName = packageName;
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
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }

    public xtend_JvmMember getXtend_jvmmember() {
        return xtend_jvmmember;
    }

    public void setXtend_jvmmember(xtend_JvmMember xtend_jvmmember) {
        this.xtend_jvmmember = xtend_jvmmember;
    }
    public List<xtend_JvmTypeReference> getXtend_jvmtypereferences() {
        return xtend_jvmtypereferences;
    }

    public void addXtend_jvmtypereference(Xtend_jvmtypereference xtend_jvmtypereference) {
        this.xtend_jvmtypereferences.add(xtend_jvmtypereference);
    }
    public List<xtend_JvmMember> getXtend_jvmmembers() {
        return xtend_jvmmembers;
    }

    public void addXtend_jvmmember(Xtend_jvmmember xtend_jvmmember) {
        this.xtend_jvmmembers.add(xtend_jvmmember);
    }
    public xtend_XFeatureCall getXtend_xfeaturecall() {
        return xtend_xfeaturecall;
    }

    public void setXtend_xfeaturecall(xtend_XFeatureCall xtend_xfeaturecall) {
        this.xtend_xfeaturecall = xtend_xfeaturecall;
    }

}