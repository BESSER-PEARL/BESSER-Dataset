





import java.util.List;
import java.util.ArrayList;

public class testup_D  {

    private String newAttribute;





    private List<testup_AUp> testup_aups;


    public testup_D(
        String newAttribute    ) {
        this.newAttribute = newAttribute;
        this.testup_aups = new ArrayList<>();
    }

    public testup_D(
        String newAttribute        ArrayList<testup_AUp> testup_aups    ) {
        this.newAttribute = newAttribute;
        this.testup_aups = testup_aups;
    }

    public String getNewattribute() {
        return newAttribute;
    }

    public void setNewattribute(String newAttribute) {
        this.newAttribute = newAttribute;
    }

    public List<testup_AUp> getTestup_aups() {
        return testup_aups;
    }

    public void addTestup_aup(Testup_aup testup_aup) {
        this.testup_aups.add(testup_aup);
    }

}