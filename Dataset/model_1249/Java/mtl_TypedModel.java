





import java.util.List;
import java.util.ArrayList;

public class mtl_TypedModel  {






    private List<mtl_EPackage> mtl_epackages;




    private mtl_Module mtl_module;


    public mtl_TypedModel(
    ) {
        this.mtl_epackages = new ArrayList<>();
    }

    public mtl_TypedModel(
        ArrayList<mtl_EPackage> mtl_epackages    ) {
        this.mtl_epackages = mtl_epackages;
    }


    public List<mtl_EPackage> getMtl_epackages() {
        return mtl_epackages;
    }

    public void addMtl_epackage(Mtl_epackage mtl_epackage) {
        this.mtl_epackages.add(mtl_epackage);
    }
    public mtl_Module getMtl_module() {
        return mtl_module;
    }

    public void setMtl_module(mtl_Module mtl_module) {
        this.mtl_module = mtl_module;
    }

}