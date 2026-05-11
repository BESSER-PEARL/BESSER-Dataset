





import java.util.List;
import java.util.ArrayList;

public class mitra_JavaSpec  {






    private mitra_RuleDeclaration mitra_ruledeclaration;




    private List<mitra_Property> mitra_propertys;


    public mitra_JavaSpec(
    ) {
        this.mitra_propertys = new ArrayList<>();
    }

    public mitra_JavaSpec(
        ArrayList<mitra_Property> mitra_propertys    ) {
        this.mitra_propertys = mitra_propertys;
    }


    public mitra_RuleDeclaration getMitra_ruledeclaration() {
        return mitra_ruledeclaration;
    }

    public void setMitra_ruledeclaration(mitra_RuleDeclaration mitra_ruledeclaration) {
        this.mitra_ruledeclaration = mitra_ruledeclaration;
    }
    public List<mitra_Property> getMitra_propertys() {
        return mitra_propertys;
    }

    public void addMitra_property(Mitra_property mitra_property) {
        this.mitra_propertys.add(mitra_property);
    }

}