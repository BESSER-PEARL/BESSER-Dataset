





import java.util.List;
import java.util.ArrayList;

public class model_TableContent  {






    private model_TableWithMultiplicity model_tablewithmultiplicity;




    private model_TableWithoutMultiplicity model_tablewithoutmultiplicity;




    private model_TableWithUnique model_tablewithunique;


    public model_TableContent(
    ) {
    }



    public model_TableWithMultiplicity getModel_tablewithmultiplicity() {
        return model_tablewithmultiplicity;
    }

    public void setModel_tablewithmultiplicity(model_TableWithMultiplicity model_tablewithmultiplicity) {
        this.model_tablewithmultiplicity = model_tablewithmultiplicity;
    }
    public model_TableWithoutMultiplicity getModel_tablewithoutmultiplicity() {
        return model_tablewithoutmultiplicity;
    }

    public void setModel_tablewithoutmultiplicity(model_TableWithoutMultiplicity model_tablewithoutmultiplicity) {
        this.model_tablewithoutmultiplicity = model_tablewithoutmultiplicity;
    }
    public model_TableWithUnique getModel_tablewithunique() {
        return model_tablewithunique;
    }

    public void setModel_tablewithunique(model_TableWithUnique model_tablewithunique) {
        this.model_tablewithunique = model_tablewithunique;
    }

}