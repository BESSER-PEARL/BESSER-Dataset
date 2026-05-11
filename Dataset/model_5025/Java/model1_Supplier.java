





import java.util.List;
import java.util.ArrayList;

public class model1_Supplier extends Address {

    private boolean preferred;





    private model1_Company model1_company;


    public model1_Supplier(
        boolean preferred    ) {
        super(
        );
        this.preferred = preferred;
    }


    public boolean getPreferred() {
        return preferred;
    }

    public void setPreferred(boolean preferred) {
        this.preferred = preferred;
    }

    public model1_Company getModel1_company() {
        return model1_company;
    }

    public void setModel1_company(model1_Company model1_company) {
        this.model1_company = model1_company;
    }

}