





import java.util.List;
import java.util.ArrayList;

public class oogen_OOModel  {






    private List<oogen_OOVariable> oogen_oovariables;




    private List<oogen_OOPackage> oogen_oopackages;




    private oogen_OOPackage oogen_oopackage;




    private List<oogen_OOMethod> oogen_oomethods;


    public oogen_OOModel(
    ) {
        this.oogen_oovariables = new ArrayList<>();
        this.oogen_oopackages = new ArrayList<>();
        this.oogen_oomethods = new ArrayList<>();
    }

    public oogen_OOModel(
        ArrayList<oogen_OOVariable> oogen_oovariables,        ArrayList<oogen_OOPackage> oogen_oopackages,        ArrayList<oogen_OOMethod> oogen_oomethods    ) {
        this.oogen_oovariables = oogen_oovariables;
        this.oogen_oopackages = oogen_oopackages;
        this.oogen_oomethods = oogen_oomethods;
    }


    public List<oogen_OOVariable> getOogen_oovariables() {
        return oogen_oovariables;
    }

    public void addOogen_oovariable(Oogen_oovariable oogen_oovariable) {
        this.oogen_oovariables.add(oogen_oovariable);
    }
    public List<oogen_OOPackage> getOogen_oopackages() {
        return oogen_oopackages;
    }

    public void addOogen_oopackage(Oogen_oopackage oogen_oopackage) {
        this.oogen_oopackages.add(oogen_oopackage);
    }
    public oogen_OOPackage getOogen_oopackage() {
        return oogen_oopackage;
    }

    public void setOogen_oopackage(oogen_OOPackage oogen_oopackage) {
        this.oogen_oopackage = oogen_oopackage;
    }
    public List<oogen_OOMethod> getOogen_oomethods() {
        return oogen_oomethods;
    }

    public void addOogen_oomethod(Oogen_oomethod oogen_oomethod) {
        this.oogen_oomethods.add(oogen_oomethod);
    }

}