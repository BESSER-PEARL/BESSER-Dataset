





import java.util.List;
import java.util.ArrayList;

public class family_Family extends NamedElement {

    private int numberOfComponents;
    private float familyIncome;





    private List<family_Members> family_memberss;


    public family_Family(
        int numberOfComponents,        float familyIncome    ) {
        super(
        );
        this.numberOfComponents = numberOfComponents;
        this.familyIncome = familyIncome;
        this.family_memberss = new ArrayList<>();
    }

    public family_Family(
        int numberOfComponents,        float familyIncome        ArrayList<family_Members> family_memberss    ) {
        this.numberOfComponents = numberOfComponents;
        this.familyIncome = familyIncome;
        this.family_memberss = family_memberss;
    }

    public int getNumberofcomponents() {
        return numberOfComponents;
    }

    public void setNumberofcomponents(int numberOfComponents) {
        this.numberOfComponents = numberOfComponents;
    }
    public float getFamilyincome() {
        return familyIncome;
    }

    public void setFamilyincome(float familyIncome) {
        this.familyIncome = familyIncome;
    }

    public List<family_Members> getFamily_memberss() {
        return family_memberss;
    }

    public void addFamily_members(Family_members family_members) {
        this.family_memberss.add(family_members);
    }

}