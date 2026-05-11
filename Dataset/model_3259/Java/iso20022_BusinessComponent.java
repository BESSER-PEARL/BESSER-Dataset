





import java.util.List;
import java.util.ArrayList;

public class iso20022_BusinessComponent extends BusinessConcept, TopLevelDictionaryEntry, BusinessElementType {






    private List<iso20022_BusinessComponent> iso20022_businesscomponents;




    private iso20022_BusinessComponent iso20022_businesscomponent;


    public iso20022_BusinessComponent(
    ) {
        super(
        );
        this.iso20022_businesscomponents = new ArrayList<>();
    }

    public iso20022_BusinessComponent(
        ArrayList<iso20022_BusinessComponent> iso20022_businesscomponents    ) {
        this.iso20022_businesscomponents = iso20022_businesscomponents;
    }


    public List<iso20022_BusinessComponent> getIso20022_businesscomponents() {
        return iso20022_businesscomponents;
    }

    public void addIso20022_businesscomponent(Iso20022_businesscomponent iso20022_businesscomponent) {
        this.iso20022_businesscomponents.add(iso20022_businesscomponent);
    }
    public iso20022_BusinessComponent getIso20022_businesscomponent() {
        return iso20022_businesscomponent;
    }

    public void setIso20022_businesscomponent(iso20022_BusinessComponent iso20022_businesscomponent) {
        this.iso20022_businesscomponent = iso20022_businesscomponent;
    }

}