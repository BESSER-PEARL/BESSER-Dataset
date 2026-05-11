





import java.util.List;
import java.util.ArrayList;

public class basic_TMethodDefinition extends TMember {






    private basic_TMethodSignature basic_tmethodsignature;




    private basic_TMethodDefinition basic_tmethoddefinition;




    private List<basic_TMethodDefinition> basic_tmethoddefinitions;




    private basic_TAbstractType basic_tabstracttype;




    private basic_TMethodDefinition basic_tmethoddefinition;




    private basic_TMethodSignature basic_tmethodsignature;




    private basic_TMethodDefinition basic_tmethoddefinition;


    public basic_TMethodDefinition(
    ) {
        super(
        );
        this.basic_tmethoddefinitions = new ArrayList<>();
    }

    public basic_TMethodDefinition(
        ArrayList<basic_TMethodDefinition> basic_tmethoddefinitions    ) {
        this.basic_tmethoddefinitions = basic_tmethoddefinitions;
    }


    public basic_TMethodSignature getBasic_tmethodsignature() {
        return basic_tmethodsignature;
    }

    public void setBasic_tmethodsignature(basic_TMethodSignature basic_tmethodsignature) {
        this.basic_tmethodsignature = basic_tmethodsignature;
    }
    public basic_TMethodDefinition getBasic_tmethoddefinition() {
        return basic_tmethoddefinition;
    }

    public void setBasic_tmethoddefinition(basic_TMethodDefinition basic_tmethoddefinition) {
        this.basic_tmethoddefinition = basic_tmethoddefinition;
    }
    public List<basic_TMethodDefinition> getBasic_tmethoddefinitions() {
        return basic_tmethoddefinitions;
    }

    public void addBasic_tmethoddefinition(Basic_tmethoddefinition basic_tmethoddefinition) {
        this.basic_tmethoddefinitions.add(basic_tmethoddefinition);
    }
    public basic_TAbstractType getBasic_tabstracttype() {
        return basic_tabstracttype;
    }

    public void setBasic_tabstracttype(basic_TAbstractType basic_tabstracttype) {
        this.basic_tabstracttype = basic_tabstracttype;
    }
    public basic_TMethodDefinition getBasic_tmethoddefinition() {
        return basic_tmethoddefinition;
    }

    public void setBasic_tmethoddefinition(basic_TMethodDefinition basic_tmethoddefinition) {
        this.basic_tmethoddefinition = basic_tmethoddefinition;
    }
    public basic_TMethodSignature getBasic_tmethodsignature() {
        return basic_tmethodsignature;
    }

    public void setBasic_tmethodsignature(basic_TMethodSignature basic_tmethodsignature) {
        this.basic_tmethodsignature = basic_tmethodsignature;
    }
    public basic_TMethodDefinition getBasic_tmethoddefinition() {
        return basic_tmethoddefinition;
    }

    public void setBasic_tmethoddefinition(basic_TMethodDefinition basic_tmethoddefinition) {
        this.basic_tmethoddefinition = basic_tmethoddefinition;
    }

}