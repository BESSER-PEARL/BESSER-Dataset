





import java.util.List;
import java.util.ArrayList;

public class LedsCodeModel_Classifier  {

    private String name;





    private LedsCodeModel_Attribute ledscodemodel_attribute;


    public LedsCodeModel_Classifier(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public LedsCodeModel_Attribute getLedscodemodel_attribute() {
        return ledscodemodel_attribute;
    }

    public void setLedscodemodel_attribute(LedsCodeModel_Attribute ledscodemodel_attribute) {
        this.ledscodemodel_attribute = ledscodemodel_attribute;
    }

}