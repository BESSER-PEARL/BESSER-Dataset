





import java.util.List;
import java.util.ArrayList;

public class mitra_Trigger  {






    private mitra_Block mitra_block;




    private List<mitra_QualifiedRuleReference> mitra_qualifiedrulereferences;




    private mitra_RuleDeclaration mitra_ruledeclaration;


    public mitra_Trigger(
    ) {
        this.mitra_qualifiedrulereferences = new ArrayList<>();
    }

    public mitra_Trigger(
        ArrayList<mitra_QualifiedRuleReference> mitra_qualifiedrulereferences    ) {
        this.mitra_qualifiedrulereferences = mitra_qualifiedrulereferences;
    }


    public mitra_Block getMitra_block() {
        return mitra_block;
    }

    public void setMitra_block(mitra_Block mitra_block) {
        this.mitra_block = mitra_block;
    }
    public List<mitra_QualifiedRuleReference> getMitra_qualifiedrulereferences() {
        return mitra_qualifiedrulereferences;
    }

    public void addMitra_qualifiedrulereference(Mitra_qualifiedrulereference mitra_qualifiedrulereference) {
        this.mitra_qualifiedrulereferences.add(mitra_qualifiedrulereference);
    }
    public mitra_RuleDeclaration getMitra_ruledeclaration() {
        return mitra_ruledeclaration;
    }

    public void setMitra_ruledeclaration(mitra_RuleDeclaration mitra_ruledeclaration) {
        this.mitra_ruledeclaration = mitra_ruledeclaration;
    }

}