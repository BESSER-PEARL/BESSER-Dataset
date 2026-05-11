





import java.util.List;
import java.util.ArrayList;

public class mitra_RuleDeclaration  {

    private String visibility;
    private boolean multi;
    private boolean virtual;
    private String exec;
    private boolean traced;
    private String name;
    private boolean stealth;





    private List<mitra_Annotation> mitra_annotations;




    private mitra_Module mitra_module;




    private List<mitra_FormalParameter> mitra_formalparameters;


    public mitra_RuleDeclaration(
        String visibility,        boolean multi,        boolean virtual,        String exec,        boolean traced,        String name,        boolean stealth    ) {
        this.visibility = visibility;
        this.multi = multi;
        this.virtual = virtual;
        this.exec = exec;
        this.traced = traced;
        this.name = name;
        this.stealth = stealth;
        this.mitra_annotations = new ArrayList<>();
        this.mitra_formalparameters = new ArrayList<>();
    }

    public mitra_RuleDeclaration(
        String visibility,        boolean multi,        boolean virtual,        String exec,        boolean traced,        String name,        boolean stealth        ArrayList<mitra_Annotation> mitra_annotations,        ArrayList<mitra_FormalParameter> mitra_formalparameters    ) {
        this.visibility = visibility;
        this.multi = multi;
        this.virtual = virtual;
        this.exec = exec;
        this.traced = traced;
        this.name = name;
        this.stealth = stealth;
        this.mitra_annotations = mitra_annotations;
        this.mitra_formalparameters = mitra_formalparameters;
    }

    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public boolean getMulti() {
        return multi;
    }

    public void setMulti(boolean multi) {
        this.multi = multi;
    }
    public boolean getVirtual() {
        return virtual;
    }

    public void setVirtual(boolean virtual) {
        this.virtual = virtual;
    }
    public String getExec() {
        return exec;
    }

    public void setExec(String exec) {
        this.exec = exec;
    }
    public boolean getTraced() {
        return traced;
    }

    public void setTraced(boolean traced) {
        this.traced = traced;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getStealth() {
        return stealth;
    }

    public void setStealth(boolean stealth) {
        this.stealth = stealth;
    }

    public List<mitra_Annotation> getMitra_annotations() {
        return mitra_annotations;
    }

    public void addMitra_annotation(Mitra_annotation mitra_annotation) {
        this.mitra_annotations.add(mitra_annotation);
    }
    public mitra_Module getMitra_module() {
        return mitra_module;
    }

    public void setMitra_module(mitra_Module mitra_module) {
        this.mitra_module = mitra_module;
    }
    public List<mitra_FormalParameter> getMitra_formalparameters() {
        return mitra_formalparameters;
    }

    public void addMitra_formalparameter(Mitra_formalparameter mitra_formalparameter) {
        this.mitra_formalparameters.add(mitra_formalparameter);
    }

}