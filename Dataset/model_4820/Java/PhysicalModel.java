





import java.util.List;
import java.util.ArrayList;

public class PhysicalModel  {






    private model_business_BusinessModel model_business_businessmodel;




    private model_physical_PhysicalForeignKey model_physical_physicalforeignkey;




    private model_Model model_model;




    private model_physical_PhysicalPrimaryKey model_physical_physicalprimarykey;




    private model_physical_PhysicalTable model_physical_physicaltable;


    public PhysicalModel(
    ) {
    }



    public model_business_BusinessModel getModel_business_businessmodel() {
        return model_business_businessmodel;
    }

    public void setModel_business_businessmodel(model_business_BusinessModel model_business_businessmodel) {
        this.model_business_businessmodel = model_business_businessmodel;
    }
    public model_physical_PhysicalForeignKey getModel_physical_physicalforeignkey() {
        return model_physical_physicalforeignkey;
    }

    public void setModel_physical_physicalforeignkey(model_physical_PhysicalForeignKey model_physical_physicalforeignkey) {
        this.model_physical_physicalforeignkey = model_physical_physicalforeignkey;
    }
    public model_Model getModel_model() {
        return model_model;
    }

    public void setModel_model(model_Model model_model) {
        this.model_model = model_model;
    }
    public model_physical_PhysicalPrimaryKey getModel_physical_physicalprimarykey() {
        return model_physical_physicalprimarykey;
    }

    public void setModel_physical_physicalprimarykey(model_physical_PhysicalPrimaryKey model_physical_physicalprimarykey) {
        this.model_physical_physicalprimarykey = model_physical_physicalprimarykey;
    }
    public model_physical_PhysicalTable getModel_physical_physicaltable() {
        return model_physical_physicaltable;
    }

    public void setModel_physical_physicaltable(model_physical_PhysicalTable model_physical_physicaltable) {
        this.model_physical_physicaltable = model_physical_physicaltable;
    }

}