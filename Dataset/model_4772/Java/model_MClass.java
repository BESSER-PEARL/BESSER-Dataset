





import java.util.List;
import java.util.ArrayList;

public class model_MClass extends MModelElementEx {






    private model_MModel model_mmodel;




    private List<model_MAttribute> model_mattributes;




    private model_MAssociationEnd model_massociationend;




    private List<model_MClass> model_mclasss;




    private List<model_MClass> model_mclasss;




    private model_MOperation model_moperation;




    private List<model_MOperation> model_moperations;




    private model_MAttribute model_mattribute;




    private List<model_MAssociation> model_massociations;


    public model_MClass(
    ) {
        super(
        );
        this.model_mattributes = new ArrayList<>();
        this.model_mclasss = new ArrayList<>();
        this.model_mclasss = new ArrayList<>();
        this.model_moperations = new ArrayList<>();
        this.model_massociations = new ArrayList<>();
    }

    public model_MClass(
        ArrayList<model_MAttribute> model_mattributes,        ArrayList<model_MClass> model_mclasss,        ArrayList<model_MClass> model_mclasss,        ArrayList<model_MOperation> model_moperations,        ArrayList<model_MAssociation> model_massociations    ) {
        this.model_mattributes = model_mattributes;
        this.model_mclasss = model_mclasss;
        this.model_mclasss = model_mclasss;
        this.model_moperations = model_moperations;
        this.model_massociations = model_massociations;
    }


    public model_MModel getModel_mmodel() {
        return model_mmodel;
    }

    public void setModel_mmodel(model_MModel model_mmodel) {
        this.model_mmodel = model_mmodel;
    }
    public List<model_MAttribute> getModel_mattributes() {
        return model_mattributes;
    }

    public void addModel_mattribute(Model_mattribute model_mattribute) {
        this.model_mattributes.add(model_mattribute);
    }
    public model_MAssociationEnd getModel_massociationend() {
        return model_massociationend;
    }

    public void setModel_massociationend(model_MAssociationEnd model_massociationend) {
        this.model_massociationend = model_massociationend;
    }
    public List<model_MClass> getModel_mclasss() {
        return model_mclasss;
    }

    public void addModel_mclass(Model_mclass model_mclass) {
        this.model_mclasss.add(model_mclass);
    }
    public List<model_MClass> getModel_mclasss() {
        return model_mclasss;
    }

    public void addModel_mclass(Model_mclass model_mclass) {
        this.model_mclasss.add(model_mclass);
    }
    public model_MOperation getModel_moperation() {
        return model_moperation;
    }

    public void setModel_moperation(model_MOperation model_moperation) {
        this.model_moperation = model_moperation;
    }
    public List<model_MOperation> getModel_moperations() {
        return model_moperations;
    }

    public void addModel_moperation(Model_moperation model_moperation) {
        this.model_moperations.add(model_moperation);
    }
    public model_MAttribute getModel_mattribute() {
        return model_mattribute;
    }

    public void setModel_mattribute(model_MAttribute model_mattribute) {
        this.model_mattribute = model_mattribute;
    }
    public List<model_MAssociation> getModel_massociations() {
        return model_massociations;
    }

    public void addModel_massociation(Model_massociation model_massociation) {
        this.model_massociations.add(model_massociation);
    }

}