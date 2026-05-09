





import java.util.List;
import java.util.ArrayList;

public class ir_EFPackage  {






    private ir_EFMetamodel ir_efmetamodel;




    private List<ir_EFClass> ir_efclasss;


    public ir_EFPackage(
    ) {
        this.ir_efclasss = new ArrayList<>();
    }

    public ir_EFPackage(
        ArrayList<ir_EFClass> ir_efclasss    ) {
        this.ir_efclasss = ir_efclasss;
    }


    public ir_EFMetamodel getIr_efmetamodel() {
        return ir_efmetamodel;
    }

    public void setIr_efmetamodel(ir_EFMetamodel ir_efmetamodel) {
        this.ir_efmetamodel = ir_efmetamodel;
    }
    public List<ir_EFClass> getIr_efclasss() {
        return ir_efclasss;
    }

    public void addIr_efclass(Ir_efclass ir_efclass) {
        this.ir_efclasss.add(ir_efclass);
    }

}