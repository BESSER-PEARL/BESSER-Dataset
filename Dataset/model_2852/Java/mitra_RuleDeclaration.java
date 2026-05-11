





import java.util.List;
import java.util.ArrayList;

public class mitra_RuleDeclaration  {

    private String name;
    private String visibility;
    private boolean stealth;
    private String exec;
    private boolean multi;
    private boolean traced;
    private boolean virtual;





    private mitra_Module mitra_module;




    private mitra_RuleReference mitra_rulereference;




    private List<mitra_FormalParameter> mitra_formalparameters;




    private mitra_SimpleRuleReference mitra_simplerulereference;




    private mitra_JavaSpec mitra_javaspec;




    private List<mitra_SimpleRuleReference> mitra_simplerulereferences;




    private List<mitra_ReturnParameter> mitra_returnparameters;




    private List<mitra_SimpleRuleReference> mitra_simplerulereferences;




    private mitra_Block mitra_block;


    public mitra_RuleDeclaration(
        String name,        String visibility,        boolean stealth,        String exec,        boolean multi,        boolean traced,        boolean virtual    ) {
        this.name = name;
        this.visibility = visibility;
        this.stealth = stealth;
        this.exec = exec;
        this.multi = multi;
        this.traced = traced;
        this.virtual = virtual;
        this.mitra_formalparameters = new ArrayList<>();
        this.mitra_simplerulereferences = new ArrayList<>();
        this.mitra_returnparameters = new ArrayList<>();
        this.mitra_simplerulereferences = new ArrayList<>();
    }

    public mitra_RuleDeclaration(
        String name,        String visibility,        boolean stealth,        String exec,        boolean multi,        boolean traced,        boolean virtual        ArrayList<mitra_FormalParameter> mitra_formalparameters,        ArrayList<mitra_SimpleRuleReference> mitra_simplerulereferences,        ArrayList<mitra_ReturnParameter> mitra_returnparameters,        ArrayList<mitra_SimpleRuleReference> mitra_simplerulereferences    ) {
        this.name = name;
        this.visibility = visibility;
        this.stealth = stealth;
        this.exec = exec;
        this.multi = multi;
        this.traced = traced;
        this.virtual = virtual;
        this.mitra_formalparameters = mitra_formalparameters;
        this.mitra_simplerulereferences = mitra_simplerulereferences;
        this.mitra_returnparameters = mitra_returnparameters;
        this.mitra_simplerulereferences = mitra_simplerulereferences;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public boolean getStealth() {
        return stealth;
    }

    public void setStealth(boolean stealth) {
        this.stealth = stealth;
    }
    public String getExec() {
        return exec;
    }

    public void setExec(String exec) {
        this.exec = exec;
    }
    public boolean getMulti() {
        return multi;
    }

    public void setMulti(boolean multi) {
        this.multi = multi;
    }
    public boolean getTraced() {
        return traced;
    }

    public void setTraced(boolean traced) {
        this.traced = traced;
    }
    public boolean getVirtual() {
        return virtual;
    }

    public void setVirtual(boolean virtual) {
        this.virtual = virtual;
    }

    public mitra_Module getMitra_module() {
        return mitra_module;
    }

    public void setMitra_module(mitra_Module mitra_module) {
        this.mitra_module = mitra_module;
    }
    public mitra_RuleReference getMitra_rulereference() {
        return mitra_rulereference;
    }

    public void setMitra_rulereference(mitra_RuleReference mitra_rulereference) {
        this.mitra_rulereference = mitra_rulereference;
    }
    public List<mitra_FormalParameter> getMitra_formalparameters() {
        return mitra_formalparameters;
    }

    public void addMitra_formalparameter(Mitra_formalparameter mitra_formalparameter) {
        this.mitra_formalparameters.add(mitra_formalparameter);
    }
    public mitra_SimpleRuleReference getMitra_simplerulereference() {
        return mitra_simplerulereference;
    }

    public void setMitra_simplerulereference(mitra_SimpleRuleReference mitra_simplerulereference) {
        this.mitra_simplerulereference = mitra_simplerulereference;
    }
    public mitra_JavaSpec getMitra_javaspec() {
        return mitra_javaspec;
    }

    public void setMitra_javaspec(mitra_JavaSpec mitra_javaspec) {
        this.mitra_javaspec = mitra_javaspec;
    }
    public List<mitra_SimpleRuleReference> getMitra_simplerulereferences() {
        return mitra_simplerulereferences;
    }

    public void addMitra_simplerulereference(Mitra_simplerulereference mitra_simplerulereference) {
        this.mitra_simplerulereferences.add(mitra_simplerulereference);
    }
    public List<mitra_ReturnParameter> getMitra_returnparameters() {
        return mitra_returnparameters;
    }

    public void addMitra_returnparameter(Mitra_returnparameter mitra_returnparameter) {
        this.mitra_returnparameters.add(mitra_returnparameter);
    }
    public List<mitra_SimpleRuleReference> getMitra_simplerulereferences() {
        return mitra_simplerulereferences;
    }

    public void addMitra_simplerulereference(Mitra_simplerulereference mitra_simplerulereference) {
        this.mitra_simplerulereferences.add(mitra_simplerulereference);
    }
    public mitra_Block getMitra_block() {
        return mitra_block;
    }

    public void setMitra_block(mitra_Block mitra_block) {
        this.mitra_block = mitra_block;
    }

}